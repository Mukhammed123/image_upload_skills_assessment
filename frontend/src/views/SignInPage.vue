<template>
    <div class="signin">
        <div class="sign-in-wrapper">
            <div class="sign-in-instructions">
                <div class="list-container">
                    <ol>
                        <li v-for="(item, index) in instructions" :key="index">{{ item }}</li>
                    </ol>
                </div>
            </div>
            <div class="sign-in-inputs">
                <div class="inputs-container">
                    <h2>Sign In</h2>
                    <div class="username-container">
                        <input v-model="username" type="text" placeholder="username" required />
                    </div>
                    <div class="password-container">
                        <input v-model="password" type="password" placeholder="password" required />
                    </div>
                    <div class="submit-btn-container">
                        <a-button type="primary" size="large" :loading="loading" @click="submit">Submit</a-button>
                    </div>
                    <p class="switch-p" @click="registerPage()">
                        Don't have an account? Create one!
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import jwt_decode from "jwt-decode";
import { defineComponent, ref } from "vue";
import { useRouter } from "vue-router";
import { api } from "@/axios-instance";
import axios from "axios";
import { useStore } from "@/stores/rootStore";

export default defineComponent({
    name: "SignInPage",
    setup() {
        const store = useStore();
        const router = useRouter();
        const username = ref("");
        const password = ref("");
        const loading = ref(false);
        const instructions = [
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor",
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco",
            "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur"
        ]
        const submit = async () => {
            if (username.value.length > 0 && password.value.length > 7) {
                loading.value = true;
                const data = {
                    username: username.value,
                    password: password.value,
                };
                try {
                    const response = await axios.post("http://localhost:8000/api/user/token/", data);
                    if (response.status === 200) {
                        localStorage.setItem("accessToken", "Bearer " + response.data.access);
                        store.setAccessToken("Bearer " + response.data.access);
                        router.push({ path: "/" });
                    }
                } catch (err) {
                    console.log(err);
                }
                loading.value = false;
            }
        };

        const registerPage = () => {
            router.push({ path: "/register" });
        };

        return {
            username,
            password,
            instructions,
            loading,
            submit,
            registerPage,
        };
    },
});
</script>
  
<style scoped>
.submit-btn {
    background-color: rgb(29, 109, 229);
    color: white;
    padding: .5em 1em;
    border: 0;
    font-size: 1.1em;
    cursor: pointer;
    border-radius: 8px;
}

.submit-btn:hover {
    background-color: rgb(27, 105, 221);
}

.sign-in-instructions {
    display: flex;
    justify-content: center;
    align-items: center;
}

.list-container {
    padding: 1em .2em;
    background-color: white;
    border-radius: 10px;
    width: 86%;
}

.sign-in-inputs {
    display: flex;
    align-items: center;
    justify-content: center;
}

.switch-p {
    text-align: center;
}

button {
    margin-top: .5em;
    border-radius: 5px;
}

button:hover {
    background-color: rgb(10, 127, 217);
}

.submit-btn-container,
.username-container,
.password-container {
    display: flex;
    justify-content: center;
}

.inputs-container {
    background-color: white;
    border-radius: 10px;
    width: 86%;
    padding: .5em 0;
}

.inputs-container>h2 {
    text-align: center;
}

input {
    display: block;
    margin: .5em 0;
    font-size: 1.3em;
    border-radius: 5px;
    border: 0.5px solid gray;
    padding: 0.3em 0.6em;
    width: 70%;
}

input:focus {
    outline: none;
}

.signin {
    min-height: 100vh;
    display: block;
    background-color: rgb(228, 234, 240);
}

.sign-in-wrapper {
    display: grid;
    width: 100%;
    min-height: 100vh;
    grid-template-columns: 1.1fr .9fr;
    grid-template-rows: 100%;
}

.switch-p {
    margin: 1.5em 0;
    cursor: pointer;
    color: rgb(0, 181, 0);
}
</style>
  