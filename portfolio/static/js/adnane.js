// var i = 1;
// $(".dev img").each(function () {
//   setTimeout(() => {
//     $(".dev img").css("order", "13");
//     $(this).css("order", "0");
//   }, 1000 * i);
//   i++;

// })
const body = document.querySelector(".landing");
for (var i = 0; i <= 100; i++) {
  const blocks = document.createElement("div");
  blocks.classList.add("square");
  body.appendChild(blocks);
}
console.log(-parseInt($('body').width()));
const animateSquare = () => {
  // $(".square").fadeTo("slow", 1);
  anime({
    targets: ".square",
    translateX: () => {
      return anime.random(-$('body').width(), $('body').width());
    },
    translateY: () => {
      return anime.random(-$('body').height(), $('body').height());
    },
    scale: () => {
      return anime.random(1, 5);
    },
    easing: "linear",
    duration: 3000,
    delay: anime.stagger(10),
    complete: animateSquare,
  });
};

// animateSquare();

function animateValue(obj, start, end, duration) {
  let startTimestamp = null;
  const step = (timestamp) => {
    if (!startTimestamp) startTimestamp = timestamp;
    const progress = Math.min((timestamp - startTimestamp) / duration, 1);
    obj.innerHTML = Math.floor(progress * (end - start) + start);
    if (progress < 1) {
      window.requestAnimationFrame(step);
    }
  };
  window.requestAnimationFrame(step);
}
// // const obj = document.querySelectorAll(".cardCounter").forEach(()=>{
  // // console.log(this);
  // })
var items = [];
$(window).ready(() => {
  animateValue($(".cardCounter"), 0,$(".cardCounter").val, 2500);
  $(".cardCounter").each(() => {
    // console.log($(this));
    console.log($(this).innerText);
  });
});
// for(var i = 0;i<=items.length;i++){
// for(o in ){
// }
// }
