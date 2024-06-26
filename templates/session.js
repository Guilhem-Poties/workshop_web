function setUser(id) {
    window.localStorage.setItem("user") = id;
}
async function getUser() {
    const user = await fetch("/", {method: "POST", body: window.localStorage.getItem("user")});
}