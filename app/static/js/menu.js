const toggleButton = document.querySelector(".nav-icon")
const navLinks = document.querySelector(".nav-panel")

toggleButton.addEventListener("click", () => {
    navLinks.classList.toggle("active")
})