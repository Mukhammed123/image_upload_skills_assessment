import { defineStore } from "pinia";

export const useStore = defineStore({
  id: "root",
  state: () => ({
    accessToken: "",
    userData: {},
  }),
  actions: {
    setUserData(data) {
      this.userData = data;
    },
    setAccessToken(token) {
      this.accessToken = token;
    },
  },

});
