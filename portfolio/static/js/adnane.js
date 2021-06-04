var i = 1;
$(".dev img").each(function () {
  setTimeout(() => {
    $(".dev img").css("order", "13");
    $(this).css("order", "0");
  }, 1000 * i);
  i++;
})