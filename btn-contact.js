const btnContact = document.querySelector(".btn-contact");
const footer = document.querySelector("footer");

window.addEventListener("scroll", function () {
  if (
    window.innerHeight + window.scrollY >=
    document.body.offsetHeight - footer.offsetHeight
  ) {
    btnContact.style.opacity = "0";
  } else {
    btnContact.style.opacity = "1";
  }
});
