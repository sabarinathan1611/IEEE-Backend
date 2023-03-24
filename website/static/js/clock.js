const line1 = document.querySelector('.line1');
const line2 = document.querySelector('.line2');
const line3 = document.querySelector('.line3');
const sec_dot = document.querySelector('.sec_dot');
const min_dot = document.querySelector('.min_dot');
const hrs_dot = document.querySelector('.hrs_dot');

var deg_sec = 0;
var deg_min = 0;
var deg_hrs = 0;
var countDownDate = new Date("march 31, 2023 00:00:00").getTime();



setInterval(() => {
  
    var date = new Date;

    var sec = date.getSeconds();
    var min = date.getMinutes();
    var hrs = date.getHours();

    var distance = countDownDate - date;

  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    
if (hrs >12) {
    hrs = hrs-12;
    document.getElementById('pm').style.fontSize ='20px';
    document.getElementById('pm').style.color ='#3fb4fc';
    document.getElementById('am').style.fontSize ='18px';
    document.getElementById('am').style.textDecoration = 'line-through';
}else{
    document.getElementById('am').style.fontSize ='20px';
    document.getElementById('am').style.color ='#3fb4fc';
    document.getElementById('pm').style.fontSize ='18px';
    document.getElementById('pm').style.textDecoration = 'line-through';
}

var currhrs = hrs;
var currmin = min/5;
console.log(currmin);
currmin = Math.floor(currmin);
deg_sec = sec*6;
deg_min = min*6;
deg_hrs = hrs*30;
line1.style.transform = 'rotate('+deg_sec+'deg)';
sec_dot.style.transform = 'rotate('+deg_sec+'deg)';
line2.style.transform = 'rotate('+deg_min+'deg)';
min_dot.style.transform = 'rotate('+deg_min+'deg)';
line3.style.transform = 'rotate('+deg_hrs+'deg)';
hrs_dot.style.transform = 'rotate('+deg_hrs+'deg)';


document.getElementById('days-dis').innerHTML = days;
document.getElementById('hrs-dis').innerHTML = hours;
document.getElementById('mins-dis').innerHTML = minutes;
document.getElementById('secs-dis').innerHTML = seconds;

if (currmin === 1) {
    document.getElementById('one').style.color = 'red';

    document.getElementById('two').style.color = 'white';
    document.getElementById('three').style.color = 'white';
    document.getElementById('four').style.color = 'white';
    document.getElementById('five').style.color = 'white';
    document.getElementById('six').style.color = 'white';
    document.getElementById('seven').style.color = 'white';
    document.getElementById('eight').style.color = 'white';
    document.getElementById('nine').style.color = 'white';
    document.getElementById('ten').style.color = 'white';
    document.getElementById('eleven').style.color = 'white';
    document.getElementById('twelve').style.color = 'white';

}else if (currmin === 2) {
    document.getElementById('two').style.color = 'red';

    document.getElementById('one').style.color = 'white';
    document.getElementById('three').style.color = 'white';
    document.getElementById('four').style.color = 'white';
    document.getElementById('five').style.color = 'white';
    document.getElementById('six').style.color = 'white';
    document.getElementById('seven').style.color = 'white';
    document.getElementById('eight').style.color = 'white';
    document.getElementById('nine').style.color = 'white';
    document.getElementById('ten').style.color = 'white';
    document.getElementById('eleven').style.color = 'white';
    document.getElementById('twelve').style.color = 'white';
}else if (currmin === 3) {
    document.getElementById('three').style.color = 'red';

    document.getElementById('two').style.color = 'white';
    document.getElementById('one').style.color = 'white';
    document.getElementById('four').style.color = 'white';
    document.getElementById('five').style.color = 'white';
    document.getElementById('six').style.color = 'white';
    document.getElementById('seven').style.color = 'white';
    document.getElementById('eight').style.color = 'white';
    document.getElementById('nine').style.color = 'white';
    document.getElementById('ten').style.color = 'white';
    document.getElementById('eleven').style.color = 'white';
    document.getElementById('twelve').style.color = 'white';
}else if (currmin === 4) {
    document.getElementById('four').style.color = 'red';

    document.getElementById('two').style.color = 'white';
    document.getElementById('three').style.color = 'white';
    document.getElementById('one').style.color = 'white';
    document.getElementById('five').style.color = 'white';
    document.getElementById('six').style.color = 'white';
    document.getElementById('seven').style.color = 'white';
    document.getElementById('eight').style.color = 'white';
    document.getElementById('nine').style.color = 'white';
    document.getElementById('ten').style.color = 'white';
    document.getElementById('eleven').style.color = 'white';
    document.getElementById('twelve').style.color = 'white';
}else if (currmin === 5) {
    document.getElementById('five').style.color = 'red';

    document.getElementById('two').style.color = 'white';
    document.getElementById('three').style.color = 'white';
    document.getElementById('four').style.color = 'white';
    document.getElementById('one').style.color = 'white';
    document.getElementById('six').style.color = 'white';
    document.getElementById('seven').style.color = 'white';
    document.getElementById('eight').style.color = 'white';
    document.getElementById('nine').style.color = 'white';
    document.getElementById('ten').style.color = 'white';
    document.getElementById('eleven').style.color = 'white';
    document.getElementById('twelve').style.color = 'white';
}else if (currmin === 6) {
    document.getElementById('six').style.color = 'red';

    document.getElementById('two').style.color = 'white';
    document.getElementById('three').style.color = 'white';
    document.getElementById('four').style.color = 'white';
    document.getElementById('five').style.color = 'white';
    document.getElementById('one').style.color = 'white';
    document.getElementById('seven').style.color = 'white';
    document.getElementById('eight').style.color = 'white';
    document.getElementById('nine').style.color = 'white';
    document.getElementById('ten').style.color = 'white';
    document.getElementById('eleven').style.color = 'white';
    document.getElementById('twelve').style.color = 'white';
}else if (currmin === 7) {
    document.getElementById('seven').style.color = 'red';

    document.getElementById('two').style.color = 'white';
    document.getElementById('three').style.color = 'white';
    document.getElementById('four').style.color = 'white';
    document.getElementById('five').style.color = 'white';
    document.getElementById('six').style.color = 'white';
    document.getElementById('one').style.color = 'white';
    document.getElementById('eight').style.color = 'white';
    document.getElementById('nine').style.color = 'white';
    document.getElementById('ten').style.color = 'white';
    document.getElementById('eleven').style.color = 'white';
    document.getElementById('twelve').style.color = 'white';
}else if (currmin === 8) {
    document.getElementById('eight').style.color = 'red';

    document.getElementById('two').style.color = 'white';
    document.getElementById('three').style.color = 'white';
    document.getElementById('four').style.color = 'white';
    document.getElementById('five').style.color = 'white';
    document.getElementById('six').style.color = 'white';
    document.getElementById('seven').style.color = 'white';
    document.getElementById('one').style.color = 'white';
    document.getElementById('nine').style.color = 'white';
    document.getElementById('ten').style.color = 'white';
    document.getElementById('eleven').style.color = 'white';
    document.getElementById('twelve').style.color = 'white';
}else if (currmin === 9) {
    document.getElementById('nine').style.color = 'red';

    document.getElementById('two').style.color = 'white';
    document.getElementById('three').style.color = 'white';
    document.getElementById('four').style.color = 'white';
    document.getElementById('five').style.color = 'white';
    document.getElementById('six').style.color = 'white';
    document.getElementById('seven').style.color = 'white';
    document.getElementById('eight').style.color = 'white';
    document.getElementById('one').style.color = 'white';
    document.getElementById('ten').style.color = 'white';
    document.getElementById('eleven').style.color = 'white';
    document.getElementById('twelve').style.color = 'white';
}else if (currmin === 10) {
    document.getElementById('ten').style.color = 'red';

    document.getElementById('two').style.color = 'white';
    document.getElementById('three').style.color = 'white';
    document.getElementById('four').style.color = 'white';
    document.getElementById('five').style.color = 'white';
    document.getElementById('six').style.color = 'white';
    document.getElementById('seven').style.color = 'white';
    document.getElementById('eight').style.color = 'white';
    document.getElementById('nine').style.color = 'white';
    document.getElementById('one').style.color = 'white';
    document.getElementById('eleven').style.color = 'white';
    document.getElementById('twelve').style.color = 'white';
}else if (currmin === 11) {
    document.getElementById('eleven').style.color = 'red';

    document.getElementById('two').style.color = 'white';
    document.getElementById('three').style.color = 'white';
    document.getElementById('four').style.color = 'white';
    document.getElementById('five').style.color = 'white';
    document.getElementById('six').style.color = 'white';
    document.getElementById('seven').style.color = 'white';
    document.getElementById('eight').style.color = 'white';
    document.getElementById('nine').style.color = 'white';
    document.getElementById('ten').style.color = 'white';
    document.getElementById('one').style.color = 'white';
    document.getElementById('twelve').style.color = 'white';
}else if (currmin === 12) {
    document.getElementById('twelve').style.color = 'red';

    document.getElementById('two').style.color = 'white';
    document.getElementById('three').style.color = 'white';
    document.getElementById('four').style.color = 'white';
    document.getElementById('five').style.color = 'white';
    document.getElementById('six').style.color = 'white';
    document.getElementById('seven').style.color = 'white';
    document.getElementById('eight').style.color = 'white';
    document.getElementById('nine').style.color = 'white';
    document.getElementById('ten').style.color = 'white';
    document.getElementById('eleven').style.color = 'white';
    document.getElementById('one').style.color = 'white';
}

if (currhrs === 1) {
    document.getElementById('one').style.color = 'yellow';
}else if (currhrs === 2) {
    document.getElementById('two').style.color = 'yellow';
}else if (currhrs === 3) {
    document.getElementById('three').style.color = 'yellow';
}else if (currhrs === 4) {
    document.getElementById('four').style.color = 'yellow';
}else if (currhrs === 5) {
    document.getElementById('five').style.color = 'yellow';
}else if (currhrs === 6) {
    document.getElementById('six').style.color = 'yellow';
}else if (currhrs === 7) {
    document.getElementById('seven').style.color = 'yellow';
}else if (currhrs === 8) {
    document.getElementById('eight').style.color = 'yellow';
}else if (currhrs === 9) {
    document.getElementById('nine').style.color = 'yellow';
}else if (currhrs === 10) {
    document.getElementById('ten').style.color = 'yellow';
}else if (currhrs === 11) {
    document.getElementById('eleven').style.color = 'yellow';

}else if (currhrs === 12) {
    document.getElementById('twelve').style.color = 'yellow';

   
}




// if (days <= 0) {
//     document.getElementById('soon').innerText = 'Stay tuned for our next exciting event';
//     document.getElementById('dontmiss').innerText ="- don t miss a moment!";
//     document.getElementById("days").innerHTML = '00';
//     document.getElementById("days").style.color = 'red';
//     document.getElementById("hours").innerHTML = '00';
//     document.getElementById("hours").style.color = 'red';
//     document.getElementById("minutes").innerHTML = '00';
//     document.getElementById("minutes").style.color = 'red';
//     document.getElementById("seconds").innerHTML = '00';
//     document.getElementById("seconds").style.color = 'red';
//     document.getElementById('tech').style.display = 'none';
//     document.getElementById('non-tech').style.display = 'none';
//     document.getElementById('main-nav').style.display = 'none';
//     document.getElementById('timeout-nav').style.display = 'block';
// }




}, 1000);

