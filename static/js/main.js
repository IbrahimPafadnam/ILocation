
// Date du copyright
const date = new Date();
document.querySelector(".year").innerHTML = date.getFullYear();

setTimeout(function () {
  $("#message").fadeOut("slow");
}, 3000);

$(".col-md-6.col-lg-4.mb-4").click(function () {
  window.location = $(this).find("a").attr("href");
  return false;
});

$(".card.listing-preview").hover(
  function () {
    var card_image = this.getElementsByClassName("card-img-top listing")[0];

    card_image.style.filter = "none";
    card_image.style.filter = "brightness(100%)";
    card_image.transition = ".5s";

    var price = this.getElementsByClassName(
      "badge badge-secondary text-white"
    )[0];

    price.style.color = "rgba(255,255,255,1)";
    price.style.background = "#242729";
    price.style.transition = ".5s";
  },
  function () {
    this.style.transform = "scale(1)";
    var card_image = this.getElementsByClassName("card-img-top listing")[0];
    card_image.style.filter = "brightness(60%)";
    card_image.style.transition = ".5s";
    card_image.style.removeProperty("height");

    var price = this.getElementsByClassName(
      "badge badge-secondary text-white"
    )[0];

    price.style.color = "#fff";
    price.style.background = "none";
  }
);


var myNav = document.getElementsByClassName(
  "navbar navbar-expand-lg navbar-dark bg-primary sticky-top"
)[0];

window.onscroll = function () {

  if ($(window).scrollTop() != 0) {
    myNav.style.boxShadow = "0px 1px 4px 0px rgba(0, 0, 0, 1)";

  } else {
    myNav.style.removeProperty("box-shadow");
  }

  if ($(window).scrollTop() >= 260) {
  } else {
    myNav.style.background = "#0c0d0e";
    myNav.style.background = "#262f35";
    myNav.style.transition = ".7s";
  }
};


$(document).ready(function() {
  //Set the carousel options
  $('#quote-carousel').carousel({
    pause: true,
    interval: 4000,
  });
});   
