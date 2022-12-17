<template>
    <div class="register-page">
        <div class="register-page-wrapper">
            <div class="left-side">
                <div class="list-container">
                    <ol>
                        <li v-for="(item, index) in instructions" :key="index">{{ item }}</li>
                    </ol>
                </div>
            </div>
            <div class="right-side">
                <div class="inputs-container">
                    <div class="input-container">
                        <input v-model="username" type="text" placeholder="username" required />
                    </div>
                    <div class="input-container">
                        <input v-model="firstName" type="text" placeholder="First name" required />
                    </div>
                    <div class="input-container"><input v-model="lastName" type="text" placeholder="Last name"
                            required /></div>
                    <div class="input-container"><input v-model="email" type="text" placeholder="Email" required />
                    </div>
                    <div class="input-container"><input v-model="password" type="password" placeholder="password"
                            required />
                    </div>
                    <div class="input-container"><input v-model="confirmPassword" type="password"
                            placeholder="Confirm password" required /></div>
                    <div class="input-container"><button class="submit-btn" :loading="loading"
                            @click="registerSubmit">Submit</button></div>
                    <p class="switch-p" @click="signIn">
                        Already have an account? Sign in.
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import { defineComponent, ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

export default defineComponent({
    name: "RegisterPage",
    setup() {
        const username = ref("");
        const password = ref("");
        const firstName = ref("");
        const lastName = ref("");
        const email = ref("");
        const confirmPassword = ref("");
        const router = useRouter();
        const loading = ref(false);
        const instructions = [
            "All fields must be filled",
            "Password has to be at least 8 symbols",
            "After creating your account you will neeed to log in to enter the system"
        ]
        const registerSubmit = async () => {
            loading.value = true;
            const data = {
                username: username.value,
                password: password.value,
                first_name: firstName.value,
                last_name: lastName.value,
                email: email.value,
            };
            if (
                !Object.keys(data).some((el) => data[el].length === 0) &&
                password.value === confirmPassword.value
            ) {
                try {
                    const response = await axios.post("http://localhost:8000/api/user/register/", data);
                    if (response.status === 201) router.push({ path: '/sign-in' });
                } catch (err) {
                    console.log(err);
                }
            } else {
                console.log("A field is empty");
            }
            loading.value = false;
        };
        const signIn = () => {
            router.push({ path: '/sign-in' });
        }
        return {
            username,
            password,
            firstName,
            lastName,
            email,
            loading,
            confirmPassword,
            instructions,
            signIn,
            registerSubmit
        }
    }
});
</script>
  
<style scoped>
button.submit-btn:hover {
    background-color: rgb(10, 127, 217);
}

.submit-btn {
    background-color: rgb(29, 109, 229);
    color: white;
    padding: .5em 1em;
    border: 0;
    font-size: 1.1em;
    cursor: pointer;
}

button {
    background-color: rgb(14, 138, 232);
    color: white;
    border: 0;
    border-radius: 5px;
    font-size: 1.4em;
    cursor: pointer;
    margin: .5em;
}

.input-container {
    display: flex;
    justify-content: center;
}

p {
    text-align: center;
    color: rgb(0, 181, 0);
    cursor: pointer;
    margin: 0;
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

.left-side,
.right-side {
    display: flex;
    align-items: center;
    justify-content: center;
}

.inputs-container {
    padding: .5em 0 1em;
    width: 86%;
    background-color: white;
    border-radius: 10px;
}

.register-page {
    min-height: 100vh;
    background-color: rgb(228, 234, 240);
}

.register-page-wrapper {
    display: grid;
    grid-template-columns: 1fr .9fr;
    min-height: 100vh;
}

input {
    display: block;
}

.list-container {
    padding: 1em .2em;
    background-color: white;
    border-radius: 10px;
    width: 86%;
}
</style>