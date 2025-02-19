// Add authentication credentials
const credentials = "{{ my_username }}:{{ my_password }}";
const authHeader = "Basic " + btoa(credentials);

async function createBlog() {
  const name = document.getElementById("new-name").value;
  const title = document.getElementById("new-title").value;
  const content = document.getElementById("new-content").value;

  try {
    const response = await fetch("/admin/blog", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: authHeader,
      },
      body: JSON.stringify({ name, title, content }),
    });
    if (response.ok) {
      location.reload();
    } else {
      alert("Error creating blog: " + response.statusText);
    }
  } catch (error) {
    console.error("Error:", error);
    alert("Error creating blog: " + error.message);
  }
}

async function updateBlog(blogId) {
  const name = document.getElementById(`name-${blogId}`).value;
  const title = document.getElementById(`title-${blogId}`).value;
  const content = document.getElementById(`content-${blogId}`).value;

  try {
    const response = await fetch(`/admin/blog/${blogId}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        Authorization: authHeader,
      },
      body: JSON.stringify({ name, title, content }),
    });
    if (response.ok) {
      location.reload();
    } else {
      alert("Error updating blog: " + response.statusText);
    }
  } catch (error) {
    console.error("Error:", error);
    alert("Error updating blog: " + error.message);
  }
}

async function deleteBlog(blogId) {
  if (!confirm("Are you sure you want to delete this blog?")) return;

  try {
    const response = await fetch(`/admin/blog/${blogId}`, {
      method: "DELETE",
      headers: {
        Authorization: authHeader,
      },
    });
    if (response.ok) {
      document.getElementById(`blog-${blogId}`).remove();
    } else {
      alert("Error deleting blog: " + response.statusText);
    }
  } catch (error) {
    console.error("Error:", error);
    alert("Error deleting blog: " + error.message);
  }
}

async function deleteComment(commentId) {
  if (!confirm("Are you sure you want to delete this comment?")) return;

  try {
    const response = await fetch(`/admin/comment/${commentId}`, {
      method: "DELETE",
      headers: {
        Authorization: authHeader,
      },
    });
    if (response.ok) {
      document.getElementById(`comment-${commentId}`).remove();
    } else {
      alert("Error deleting comment: " + response.statusText);
    }
  } catch (error) {
    console.error("Error:", error);
    alert("Error deleting comment: " + error.message);
  }
}
