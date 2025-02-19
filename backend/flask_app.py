from flask import Flask, render_template, jsonify, request, abort
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS

from my_password import my_username, my_password
import sqlite3
from rate_limiter import rate_limit
from create_db import init_db

app = Flask(__name__)
auth = HTTPBasicAuth()

CORS(app, origins=["https://kritserv.pythonanywhere.com", "http://localhost:8080", "https://kritserv.github.io"])
users = {
    my_username: my_password,
}

def get_db():
    conn = sqlite3.connect('blogs.db')
    conn.row_factory = sqlite3.Row
    return conn

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

# Admin routes - all require authentication
@app.route('/')
@rate_limit(max_requests=50, window_minutes=60)
def home():
    return render_template('index.html')

@app.route('/edit')
@auth.login_required
def edit_data():
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT b.*, COUNT(bc.id) as comment_count FROM blogs b LEFT JOIN blogs_comment bc ON b.id = bc.blogid GROUP BY b.id')
    blogs = c.fetchall()
    c.execute('SELECT * FROM blogs_comment')
    comments = c.fetchall()
    conn.close()
    return render_template('edit_data.html',
                         blogs=blogs,
                         comments=comments)

@app.route('/admin/blog', methods=['POST'])
def create_blog():
    data = request.json
    conn = get_db()
    c = conn.cursor()
    c.execute('INSERT INTO blogs (name, title, content, likes) VALUES (?, ?, ?, 0)',
              (data['name'], data['title'], data['content']))
    conn.commit()
    blog_id = c.lastrowid
    conn.close()
    return jsonify({'id': blog_id, 'message': 'Blog created successfully'})

@app.route('/admin/blog/<int:blog_id>', methods=['PUT'])
def update_blog(blog_id):
    data = request.json
    conn = get_db()
    c = conn.cursor()
    c.execute('UPDATE blogs SET name=?, title=?, content=? WHERE id=?',
              (data['name'], data['title'], data['content'], blog_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Blog updated successfully'})

@app.route('/admin/blog/<int:blog_id>', methods=['DELETE'])
def delete_blog(blog_id):
    conn = get_db()
    c = conn.cursor()
    c.execute('DELETE FROM blogs WHERE id=?', (blog_id,))
    c.execute('DELETE FROM blogs_comment WHERE blogid=?', (blog_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Blog deleted successfully'})

@app.route('/admin/comment/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    conn = get_db()
    c = conn.cursor()
    c.execute('DELETE FROM blogs_comment WHERE id=?', (comment_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Comment deleted successfully'})

@app.route('/api/blogs', methods=['GET'])
@rate_limit(max_requests=50, window_minutes=60)
def get_blogs():
    conn = get_db()
    c = conn.cursor()
    c.execute('''
        SELECT b.*, COUNT(bc.id) as comment_count
        FROM blogs b
        LEFT JOIN blogs_comment bc ON b.id = bc.blogid
        GROUP BY b.id
    ''')
    blogs = [dict(row) for row in c.fetchall()]
    conn.close()
    return jsonify(blogs)

@app.route('/api/blog/<int:blog_id>', methods=['GET'])
@rate_limit(max_requests=50, window_minutes=60)
def get_blog(blog_id):
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM blogs WHERE id=?', (blog_id,))
    blog = c.fetchone()
    if not blog:
        abort(404)

    c.execute('SELECT * FROM blogs_comment WHERE blogid=?', (blog_id,))
    comments = [dict(row) for row in c.fetchall()]

    blog_data = dict(blog)
    blog_data['comments'] = comments
    conn.close()
    return jsonify(blog_data)

@app.route('/api/blog/<int:blog_id>/comment', methods=['POST'])
@rate_limit(max_requests=50, window_minutes=60)
def add_comment(blog_id):
    data = request.json
    if not data or 'username' not in data or 'comment' not in data:
        abort(400)

    conn = get_db()
    c = conn.cursor()
    c.execute('INSERT INTO blogs_comment (username, comment, blogid) VALUES (?, ?, ?)',
              (data['username'], data['comment'], blog_id))
    conn.commit()
    comment_id = c.lastrowid
    conn.close()
    return jsonify({'id': comment_id, 'message': 'Comment added successfully'})

@app.route('/api/blog/<int:blog_id>/like', methods=['POST'])
@rate_limit(max_requests=50, window_minutes=60)
def update_likes(blog_id):
    data = request.json
    if not data or 'action' not in data:
        abort(400)

    change = 1 if data['action'] == 'upvote' else -1

    conn = get_db()
    c = conn.cursor()
    c.execute('UPDATE blogs SET likes = likes + ? WHERE id = ?', (change, blog_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Likes updated successfully'})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
