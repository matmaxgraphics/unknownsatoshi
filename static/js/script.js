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
const shareIcon = document.querySelector(".ri-share-line");
const shareLink = document.querySelectorAll(".sharing-link");

socialLinks.classList.add("hidden");

shareBtn.addEventListener("click", function () {
  // console.log("button clicked");
  socialLinks.classList.toggle("hidden");
  shareIcon.classList.add("ri-close-line");
  shareIcon.classList.toggle("ri-share-line");
});

for (let i = 0; i < shareLink.length; i++){
  shareLink[i].addEventListener("click", function () {
    // console.log('button clicked');
    socialLinks.classList.add("hidden");
    shareIcon.classList.toggle("ri-share-line");
  });
}
