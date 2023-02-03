var countDownDate = new Date("feb 10, 2023 00:00:00").getTime();
var x = setInterval(function () {
  var now = new Date().getTime();
  var distance = countDownDate - now;

  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  if (seconds < 10) {
    seconds = "0" + seconds;
    document.getElementById("seconds").style.color = "red";
  }
  if (seconds > 10) {
    document.getElementById("seconds").style.color = "white";
  }
  if (minutes < 10) {
    minutes = "0" + minutes;
    document.getElementById("minutes").style.color = "red";

  }
  if (minutes > 10) {
    document.getElementById("minutes").style.color = "white";
  }
  if (hours < 10) {
    hours = "0" + hours;
    document.getElementById("hours").style.color = "red";

  }
  if (hours <= 4) {
    document.getElementById("hours").style.color = "red";
    if (seconds < 10) {
      document.getElementById("seconds").style.color = "red";
    }
    if (minutes < 10) {
      document.getElementById("minutes").style.color = "red";
    }
  }
  if (hours > 10) {
    document.getElementById("hours").style.color = "white";
  }
  if (days < 10) {
    days = "0" + days;
    document.getElementById("days").style.color = "red";
  }

  document.getElementById("days").innerHTML = days;
  document.getElementById("hours").innerHTML = hours;
  document.getElementById("minutes").innerHTML = minutes;
  document.getElementById("seconds").innerHTML = seconds;
}, 1000);
