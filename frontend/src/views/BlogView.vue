<template>
  <div class="blog">
    <h1 class="primary-color" data-aos="fade-down">Kritserv Blog</h1>
    <table>
      <tbody>
        <tr
          v-for="blog in blogs"
          :key="blog.id"
          @click="$router.push(`/content/${blog.id}`)"
          style="cursor: pointer"
          data-aos="flip-right"
        >
          <td data-aos="flip-right">
            <h2>{{ blog.title }}</h2>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
table {
  width: clamp(300px, 80%, 3000px);
  margin-left: 10%;
  background-color: #111111;
  transition: 0.3s;
  border: None;
}
td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #222222;
  border-right: 2px solid #333333;
  transition: 0.3s;
}

td:hover {
  background-color: #2c3e50;
  transition: 0.3s;
}

.blog {
  margin-top: 65px;
}
</style>

<script>
import axios from "axios";
import DOMPurify from "dompurify";

export default {
  data() {
    return {
      blogs: [],
    };
  },
  mounted() {
    this.fetchBlogs();
  },
  methods: {
    async fetchBlogs() {
      try {
        const response = await axios.get(
          "https://kritserv.pythonanywhere.com/api/blogs"
        );
        this.blogs = response.data.map((blog) => ({
          ...blog,
          content: DOMPurify.sanitize(blog.content), // Sanitize HTML
        }));
      } catch (error) {
        console.error("Error fetching blogs:", error);
      }
    },
  },
};
</script>
