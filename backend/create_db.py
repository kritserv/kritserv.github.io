import sqlite3

def init_db():
    conn = sqlite3.connect('rate_limits.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS rate_limits (
            ip_address TEXT,
            endpoint TEXT,
            request_count INTEGER,
            window_start TEXT,
            PRIMARY KEY (ip_address, endpoint)
        )
    ''')
    conn.commit()
    conn.close()

    conn = sqlite3.connect('blogs.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS blogs (
            id INTEGER,
            name TEXT,
            title TEXT,
            content TEXT,
            likes INTEGER,
            PRIMARY KEY (id)
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS blogs_comment (
            id INTEGER,
            username TEXT,
            comment TEXT,
            blogid INTEGER,
            PRIMARY KEY (id)
        )
    ''')
    conn.commit()
    conn.close()
