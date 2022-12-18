<template>
  <div id="components-modal-demo-position">
    <a-modal :visible="showAddDialog" title="Upload Image" centered @cancel="close" :footer="null">
      <div v-if="imgUrl" class="upload-img-container">
        <img :src="getBaseURL() + imgUrl" alt="uploaded" width="450" />
      </div>
      <p>
        <input :value="location" type="text" placeholder="Location" required class="regular-input" disabled />
      </p>
      <p>
        <span class="tagged-people" v-for="(name, index) in taggedPeople" :key="`${name}-${index}`">{{ name }}
          {{ index + 1 < taggedPeople.length ? ', ' : '' }} </span>
      </p>
      <textarea :value="content" type="text" placeholder="Description" disabled></textarea>
    </a-modal>
  </div>
</template>
  
<script>
import { defineComponent } from "vue";
import { CloseOutlined } from "@ant-design/icons-vue";

export default defineComponent({
  name: "ShowDetailsDialog",
  components: { CloseOutlined },
  props: {
    showAddDialog: { type: Boolean, default: false },
    imgUrl: { type: String, default: undefined },
    location: { type: String, default: undefined },
    content: { type: String, default: undefined },
    taggedPeople: { type: Array, default: undefined }
  },
  setup(props, context) {
    const getBaseURL = () => "http://localhost:8000/";
    const close = () => {
      context.emit("close");
    }
    return {
      close,
      getBaseURL
    }
  }
});
</script>
  
<style scoped>
.tagged-people {
  font-size: 1.2em;
}

.tag-people-p {
  display: flex;
}

#uploadFile {
  border: 0;
  margin-top: .5em;
}

textarea {
  margin: 1em 0;
  padding: 0.3em;
  border-radius: 5px;
}

textarea:focus {
  outline: none;
}

.regular-input {
  border: 0;
  border-bottom: 1px solid rgb(188, 187, 187);
  font-size: 1.3em;
  margin-top: 1em;
}

.regular-input:focus {
  outline: none;
}

input {
  width: 100%;
  border: 0.5px solid black;
}

textarea {
  width: 100%;
  height: 200px;
}

.video-container {
  position: relative;
}

.video-container>button {
  position: absolute;
  z-index: 10;
  right: 25px;
}

.upload-img-container {
  position: relative;
  text-align: center;
  margin: .5em 0;
}

.upload-img-container>button {
  position: absolute;
  z-index: 10;
  right: 25px;
}

.doc-container {
  margin: 1em 0;
}

.doc-container>button {
  margin-left: 0.2em;
}
</style>
  