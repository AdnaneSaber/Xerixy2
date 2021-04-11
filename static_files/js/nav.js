let collapseButton = document.getElementById("navCollapse");
let closeNav = document.getElementById("closeNav");
collapseButton.addEventListener("click", function () {
  toggleNav(true);
});
closeNav.addEventListener("click", function () {
  toggleNav(false);
});
function toggleNav(open) {
  let navLinks = document.getElementById("navLinks");
  let closeNav = document.getElementById("closeNav");
  if (open) {
    navLinks.style.left = 0;
    navLinks.style.display = "flex";
    closeNav.style.display = "block";
  } else {
    navLinks.style.left = "100%";
    navLinks.style.display = "none";
    closeNav.style.display = "none";
  }
}
