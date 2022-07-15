$(document).ready(function () {
  $(".input-field").focusout(function () {
    // Make Floating Label More Accurate
    var inputValue = $(this).val();
    if (inputValue === "") {
      $(this).removeClass("has-value");
    } else {
      $(this).addClass("has-value");
    }
  });
});