<template>
  <div class="post-blocks">
    <div class="wrapper">
      <a-card v-for="(post, postIndex) in postsData" :key="`${post.id}-${postIndex}`" class="post">
        <div class="user-block">
          <span>
            <span class="post-date">{{ new Date(post.created_at).toLocaleString() }}</span>
          </span>
        </div>
        <hr />
        <div class="body-container">
          <div class="files-container">
            <div class="media">
              <img :src="'http://' + getBaseUrl() + post.url" style="width: 100%" />
            </div>
            <br />
          </div>
          <div class="location-container">
            <h1>{{ post.location }}</h1>
          </div>
          <p>
            {{ post.content }}
          </p>
        </div>
        <hr />
      </a-card>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { BarsOutlined, CloseOutlined, SendOutlined } from '@ant-design/icons-vue';

export default defineComponent({
  name: "PostBlocks",
  components: { BarsOutlined, CloseOutlined, SendOutlined },
  props: {
    postsData: { type: Array, default: undefined },
  },
  setup() {
    const getBaseUrl = () => "localhost:8000/";

    return {
      getBaseUrl
    };
  },
});
</script>

<style scoped>
/* .comment-container {
  transform: rotate(180deg);
}

.comments-wrapper {
  transform: rotate(180deg);
} */
hr {
  /* margin: 0; */
}

.comment-action {
  width: 100%;
  cursor: pointer;
  display: flex;
  justify-content: center;
  padding: .4em 0;
}

.comment-action:hover {
  background-color: rgb(241, 241, 241);
}

.post-date {
  font-size: .8em;
  color: rgb(101, 101, 101);
}

.ant-dropdown-link:hover {
  background-color: rgb(242, 242, 242);
}

.ant-dropdown-link {
  margin-left: 1em;
}

.comments-wrapper {
  max-height: 350px;
  overflow-y: auto;
}

.comment-content {
  display: flex;
}

.comment-input-block {
  display: flex;
  border-radius: 5px;
  padding: 0.5em 1em;
  background-color: rgb(242, 242, 242);
}

.comment-input-block>input {
  flex-grow: 1;
  border: 0;
  background-color: rgb(242, 242, 242);
}

.comment-input-block>input:focus {
  outline: none;
}

.comment-container {
  display: flex;
}

.post {
  margin: 2em 0;
  border-radius: 10px;
  border: 1px solid rgb(199, 196, 196);
}

.post-blocks {
  display: flex;
  justify-content: center;
}

.wrapper {
  width: 650px;
}

h1 {
  text-align: center;
}

.actions-block {
  display: flex;
}

.user-block {
  display: flex;
  justify-content: space-between;
  position: relative;
}

.comment-user {
  display: flex;
  flex-flow: row;
}

.comment-user>span {
  margin: 0 1em;
}

* {
  box-sizing: border-box;
}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Hide the images by default */
.mySlides {
  display: none;
  height: 600px;
  overflow: hidden;
}

/* Next & previous buttons */
.prev,
.next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  margin-top: -22px;
  padding: 16px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover,
.next:hover {
  background-color: rgba(0, 0, 0, 0.8);
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* The dots/bullets/indicators */

.dots-container {
  display: flex;
  justify-content: center;
}

.dot {
  cursor: pointer;
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active,
.dot:hover {
  background-color: #717171;
}

/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 1.5s;
}

@keyframes fade {
  from {
    opacity: 0.4;
  }

  to {
    opacity: 1;
  }
}
</style>
