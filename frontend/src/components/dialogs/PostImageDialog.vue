<template>
  <div id="components-modal-demo-position">
    <a-modal :visible="showAddDialog" title="Upload Image" centered :maskClosable="false" @ok="submit" @cancel="cancel">
      <div v-if="uploadedImgURL" class="upload-img-container">
        <a-button type="gray-2" shape="circle" @click="removeImg(index)">
          <template #icon>
            <CloseOutlined />
          </template>
        </a-button>
        <img :src="uploadedImgURL.url" alt="uploaded" width="450" />
      </div>
      <input type="file" accept="image/*" @input="uploadFile" multiple id="uploadFile" />
      <p>
        <input v-model="location" type="text" placeholder="Location" required class="regular-input" />
      </p>
      <p>
        <span v-for="(name, index) in taggedPeople" :key="`${name}-${index}`">{{ name }} {{ index + 1 <
            taggedPeople.length ? ', ' : ''
        }} </span>
      </p>
      <p class="tag-people-p">
        <input v-model="tagName" class="regular-input" type="text" placeholder="Tag someone (one at a time)" />
        <a-button @click="tagPerson()" style="margin-top: 1em">Tag</a-button>
      </p>
      <textarea v-model="content" type="text" placeholder="Description" required></textarea>
    </a-modal>
  </div>
</template>

<script>
import { defineComponent, ref } from "vue";
import { CloseOutlined } from "@ant-design/icons-vue";
import { useStore } from "@/stores/rootStore";
import axios from "axios";

export default defineComponent({
  name: "AddEditPostDialog",
  components: { CloseOutlined },
  props: {
    showAddDialog: { type: Boolean, default: false },
  },
  setup(props, context) {
    const location = ref("");
    const content = ref("");
    const taggedPeople = ref([]);
    const tagName = ref("");
    const uploadedImgURL = ref(undefined);
    const store = useStore();

    const submit = async () => {
      if (uploadedImgURL) {
        const data = {
          description: content.value,
          filename: uploadedImgURL.value.file.name,
          location: location.value,
          people: taggedPeople.value,
        }
        const formData = new FormData();
        formData.append(
          "file",
          uploadedImgURL.value.file
        );
        formData.append(
          "details",
          JSON.stringify(data)
        )
        try {
          const response = await axios.post("http://localhost:8000/api/images/", formData, {
            headers: {
              "Content-Type": "multipart/form-data",
              "Authorization": store.accessToken
            },
          });
          console.log(response);
          context.emit("submit");
          cancel();
        } catch (err) {
          console.log(err);
        }
      }
    };

    const uploadFile = (e) => {
      const file = e.target.files[0];
      const type = file.type.split("/")[0];
      createFile(file, type);
    };

    const createFile = (file, type) => {
      const reader = new FileReader();
      reader.onload = (e) => {
        const data = {
          url: e.target.result,
          file: file,
          type: type,
        };
        uploadedImgURL.value = data;
      };
      reader.readAsDataURL(file);
    };

    const removeImg = () => {
      const reader = new FileReader();
      reader.abort(uploadedImgURL.value.url);
      uploadedImgURL.value = undefined;
      const input = document.getElementById("uploadFile");
      input.value = "";
    };

    const tagPerson = () => {
      if (tagName.value.length > 0) {
        taggedPeople.value.push(tagName.value);
        tagName.value = "";
      }
    }

    const cancel = () => {
      location.value = "";
      content.value = "";
      uploadedImgURL.value = undefined;
      context.emit("close");
    };

    return {
      location,
      content,
      tagName,
      taggedPeople,
      uploadedImgURL,
      tagPerson,
      submit,
      cancel,
      uploadFile,
      removeImg,
    };
  },
});
</script>

<style scoped>
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
