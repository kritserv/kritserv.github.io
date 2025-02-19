<template>
  <div v-if="blog" class="blog-content">
    <br /><br />
    <h1 class="primary-color">{{ blog.title }}</h1>
    <div v-html="blog.content"></div>
    <p><strong>Likes:</strong> {{ blog.likes }}</p>

    <button class="vote" @click="upvote"><i class="sprite upvote"></i></button>
    <button class="vote" @click="downvote">
      <i class="sprite downvote"></i>
    </button>

    <h3>Comments</h3>
    <div v-for="comment in blog.comments" :key="comment.id" class="comment">
      <p>
        <strong>{{ comment.username }}</strong
        >: {{ comment.comment }}
      </p>
    </div>

    <h3>Add a Comment</h3>
    <input v-model="newUsername" placeholder="Your name" />
    <textarea v-model="newComment" placeholder="Your comment"></textarea>
    <button @click="postComment">Post Comment</button>
  </div>
  <p v-else>Loading...</p>
  <!-- Display this while waiting for the API response -->
</template>

<script>
import { ref, watch, computed, onMounted } from "vue";
import axios from "axios";
import DOMPurify from "dompurify";
import { useRoute } from "vue-router";

export default {
  setup() {
    // Use `useRoute()` to get the route object
    const route = useRoute();

    // Create a reactive reference for the blog
    const blog = ref(null);
    const newUsername = ref("");
    const newComment = ref("");

    // Computed property to extract the blog ID from the route
    const blogId = computed(() => route.params.id);

    // Fetch the blog when the component is mounted or when the route changes
    const fetchBlog = async () => {
      try {
        const response = await axios.get(
          `https://kritserv.pythonanywhere.com/api/blog/${blogId.value}`
        );

        if (response.data) {
          blog.value = {
            ...response.data,
            content: DOMPurify.sanitize(response.data.content),
          };
        } else {
          console.error("Blog not found!");
          blog.value = null;
        }
      } catch (error) {
        if (error.response && error.response.status === 429) {
          // 429 Too Many Requests: Inform user to wait
          alert(
            "You have made too many requests. Please wait for an hour and try again."
          );
        } else {
          // For other errors, show the error message
          console.error("Error fetching blog:", error);
        }
        blog.value = null;
      }
    };

    // Watch for changes in the route to refetch the blog
    watch(blogId, () => {
      fetchBlog();
    });

    // Watch for changes in the blog object and update the page title
    watch(blog, (newBlog) => {
      if (newBlog && newBlog.title) {
        document.title = newBlog.title; // Set the document title to the blog title
      }
    });

    // Fetch the blog when the component is mounted
    onMounted(() => {
      fetchBlog();
    });

    const postComment = async () => {
      if (!newUsername.value || !newComment.value) {
        return alert("Please enter both fields!");
      }

      try {
        await axios.post(
          `https://kritserv.pythonanywhere.com/api/blog/${blogId.value}/comment`,
          {
            username: newUsername.value,
            comment: newComment.value,
          }
        );
        newUsername.value = "";
        newComment.value = "";
        fetchBlog(); // Refresh comments
      } catch (error) {
        console.error("Error posting comment:", error);
      }
    };

    const upvote = async () => {
      try {
        await axios.post(
          `https://kritserv.pythonanywhere.com/api/blog/${blogId.value}/like`,
          { action: "upvote" }
        );
        fetchBlog(); // Refresh likes
      } catch (error) {
        console.error("Error upvoting:", error);
      }
    };

    const downvote = async () => {
      try {
        await axios.post(
          `https://kritserv.pythonanywhere.com/api/blog/${blogId.value}/like`,
          { action: "downvote" }
        );
        fetchBlog(); // Refresh likes
      } catch (error) {
        console.error("Error downvoting:", error);
      }
    };

    return {
      blog,
      newUsername,
      newComment,
      postComment,
      upvote,
      downvote,
    };
  },
};
</script>

<style scoped>
.blog-content {
  max-width: 600px;
  margin: auto;
  padding: 20px;
}
.comment {
  border-top: 1px solid #ddd;
  padding: 10px;
}
input,
textarea {
  display: block;
  width: 100%;
  margin-bottom: 10px;
}
button {
  margin-right: 10px;
}
button.vote {
  background: None;
  border: None;
}
button.vote:hover {
  cursor: pointer;
}
i {
  zoom: 0.3;
}
.upvote {
  background: url("../assets/spritesheet.png") -896px -384px;
}
.downvote {
  background: url("../assets/spritesheet.png") -1024px -384px;
}
</style>
