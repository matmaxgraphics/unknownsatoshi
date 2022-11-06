//Navbar Toggling
function classToggle() {
  const navs = document.querySelectorAll(".navbar__Items");

  navs.forEach((nav) => nav.classList.toggle("navbar__ToggleShow"));
}

document
  .querySelector(".navbar__Link-toggle")
  .addEventListener("click", classToggle);


/*======share button function========*/
const shareBtn = document.querySelector(".share-btn");
const socialLinks = document.querySelector(".social-sharing");

socialLinks.classList.add("hidden");

shareBtn.addEventListener("click", function () {
  // console.log("button clicked");
  socialLinks.classList.toggle("hidden");
});

