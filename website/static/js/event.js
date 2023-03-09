var countDownDate = new Date("march 14, 2023 00:00:00").getTime();
var x = setInterval(function () {
  var now = new Date().getTime();
  var distance = countDownDate - now;

  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  if (seconds < 10) {
    seconds =   seconds;
    document.getElementById("seconds").style.color = "red";
  }
  if (seconds > 10) {
    document.getElementById("seconds").style.color = "white";
  }
  if (minutes < 10) {
    minutes =  minutes;
    document.getElementById("minutes").style.color = "red";

  }
  if (minutes > 10) {
    document.getElementById("minutes").style.color = "white";
  }
  if (hours < 10) {
    hours =  hours;
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
    days =  days;
    document.getElementById("days").style.color = "red";
  }
  
  document.getElementById("days").innerHTML = days;
  document.getElementById("hours").innerHTML = hours;
  document.getElementById("minutes").innerHTML = minutes;
  document.getElementById("seconds").innerHTML = seconds;
  

 if (days <= 0) {
  document.getElementById('soon').innerText = 'Stay tuned for our next exciting event';
  document.getElementById('dontmiss').innerText ="- don t miss a moment!";
  document.getElementById("days").innerHTML = '00';
  document.getElementById("days").style.color = 'red';
  document.getElementById("hours").innerHTML = '00';
  document.getElementById("hours").style.color = 'red';
  document.getElementById("minutes").innerHTML = '00';
  document.getElementById("minutes").style.color = 'red';
  document.getElementById("seconds").innerHTML = '00';
  document.getElementById("seconds").style.color = 'red';
  document.getElementById('tech').style.display = 'none';
  document.getElementById('non-tech').style.display = 'none';
  document.getElementById('main-nav').style.display = 'none';
  document.getElementById('timeout-nav').style.display = 'block';
 }
}, 1000);




