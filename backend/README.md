Get all blogs:

curl http://localhost:5000/api/blogs

Get specific blog with comments:

curl http://localhost:5000/api/blog/1

Add a comment:

curl -X POST http://localhost:5000/api/blog/1/comment \
  -H "Content-Type: application/json" \
  -d '{"username": "user123", "comment": "Great post!"}'

Upvote a blog:

curl -X POST http://localhost:5000/api/blog/1/like \
  -H "Content-Type: application/json" \
  -d '{"action": "upvote"}'

Downvote a blog:

curl -X POST http://localhost:5000/api/blog/1/like \
  -H "Content-Type: application/json" \
  -d '{"action": "downvote"}'
