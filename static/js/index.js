const tween = gsap.timeline();
var count = $(".cardContainer").children().length;
console.log(count);
tween.to(".cardContainer", {
  duration: 1,
  ease: "power1.inOut",
  motionPath: {
    path: [{ x: -window.innerWidth * (count - 1), y: 0 }],
    curviness: 0,
    autoRotate: false,
  },
});

const controller = new ScrollMagic.Controller();

const scene = new ScrollMagic.Scene({
  triggerElement: ".animation",
  duration: count * 1500,
  triggerHook: 0,
})
  .setTween(tween)
  .setPin(".animation")
  .addTo(controller);
