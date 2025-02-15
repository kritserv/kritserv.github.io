<template>
  <div class="nav-desktop">
    <nav>
      <span v-if="$route.path != '/'">
        <router-link to="/">Home</router-link>
        |
      </span>
      <span v-if="$route.path == '/'"
        ><a style="color: #42b983" href="#">Top</a> | <a href="#work">Work</a> |
        <a href="#education">Education</a> |
      </span>
      <router-link to="/contact">Contact</router-link> |
      <router-link to="/blog">Blog</router-link>
    </nav>
  </div>
  <div class="nav-mobile">
    <nav>
      <template v-if="$route.path != '/'">
        <router-link to="/">
          <i class="sprite nav-icon home-icon"></i>
        </router-link>
      </template>
      <template v-if="$route.path == '/'">
        <a style="color: #42b983" href="#">
          <i class="sprite nav-icon home-icon"></i>
        </a>
        <a href="#work">
          <i class="sprite nav-icon work-icon"></i>
        </a>
        <a href="#education">
          <i class="sprite nav-icon education-icon"></i>
        </a>
      </template>
      <router-link to="/contact">
        <i class="sprite nav-icon contact-icon"></i>
      </router-link>
      <router-link to="/blog">
        <i class="sprite nav-icon blog-icon"></i>
      </router-link>
    </nav>
  </div>
  <transition name="fade" mode="out-in">
    <router-view />
  </transition>
</template>
<style>
html {
  margin: 0;
  padding: 0;
  background: black;
  scroll-behavior: smooth;
  overflow-x: hidden;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffffff;
  overflow: hidden;
}
.sprite {
  width: 128px;
  height: 128px;
  display: block;
}
nav {
  z-index: 1;
  position: fixed;
  background: transparent;
  backdrop-filter: blur(10px);
}
@media only screen and (max-width: 600px) {
  .nav-desktop {
    display: none;
  }
  nav {
    bottom: 0;
    width: 100%;
    display: flex;
    overflow-x: hidden;
  }
  .nav-mobile nav > div,
  .nav-mobile nav > a {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .nav-icon {
    zoom: 0.2;
    margin: 0 auto;
    margin-bottom: 35px;
  }
  .home-icon {
    background: url("assets/spritesheet.png") -0px -0px;
  }
  .work-icon {
    background: url("assets/spritesheet.png") -128px -0px;
  }
  .education-icon {
    background: url("assets/spritesheet.png") -256px -0px;
  }
  .contact-icon {
    background: url("assets/spritesheet.png") -384px -0px;
  }
  .blog-icon {
    background: url("assets/spritesheet.png") -512px -0px;
  }
}
@media only screen and (min-width: 600px) {
  .nav-mobile {
    display: none;
  }
  nav {
    padding: 25px;
    top: 0;
    width: 100%;
    text-align: left;
  }
  nav a {
    font-weight: bold;
    color: #2c3e50;
  }
  nav a.router-link-exact-active {
    color: #42b983;
  }
}

th {
  background: #2c3e50;
}
.primary-color {
  color: #42b983;
}
hr {
  border: 4px solid #42b983;
  border-radius: 25px;
}
.openinnewtab {
  background: url("assets/spritesheet.png") -640px -0px;
  zoom: 0.2;
}
.github {
  background: url("assets/spritesheet.png") -768px -512px;
  zoom: 0.2;
}
</style>
