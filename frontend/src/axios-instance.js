import axios from "axios";
import { useStore } from "@/stores/rootStore";

export const baseURL = "localhost:8000/";

const api = axios.create({
    baseURL: "http://" + baseURL + "api/",
    timeout: 2000,
});

api.interceptors.request.use((request) => {
    const store = useStore();
    request.headers.Authorization = store.accessToken ?? "";
    return request;
});

export { api };
