
let days =document.querySelector('.days');
let hours = document.querySelector('.hours');
let minutes = document.querySelector('.minutes');
let seconds = document.querySelector('.seconds')

let dd = document.getElementById('dd');
let hh = document.getElementById('hh');
let mm = document.getElementById('mm');
let ss = document.getElementById('ss');

let day_dot = document.querySelector('.day_dot');
let hrs_dot = document.querySelector('.hrs_dot');
let min_dot = document.querySelector('.min_dot');
let sec_dot = document.querySelector('.sec_dot');

let endDate = '08/11/2023 00:00:00';
//             mm/dd/yyyy 00.00.00//

let x = setInterval(function(){
let now = new Date(endDate).getTime();
let countDown = new Date().getTime();
let distance = now - countDown;

let d = Math.floor(distance/(1000 * 60 * 60 * 24));
let h = Math.floor((distance%(1000 * 60 * 60 * 24))/(1000 * 60 * 60));
let m = Math.floor((distance%(1000 * 60 * 60 ))/(1000 * 60));
let s = Math.floor((distance%(1000 * 60  ))/(1000));

days.innerHTML = d + '<br><span class="dhms_n">Days</span>';
hours.innerHTML = h + '<br><span class="dhms_n">hours</span>';
minutes.innerHTML = m + '<br><span class="dhms_n">minutes</span>';
seconds.innerHTML = s + '<br><span class="dhms_n">seconds</span>';

dd.style.strokeDashoffset = 305- (305* d) / 365;
hh.style.strokeDashoffset = 305- (305* h) / 24;
mm.style.strokeDashoffset = 305- (305* m) / 60;
ss.style.strokeDashoffset = 305- (305* s) / 60;

day_dot.style.transform = `rotateZ(${d * 0.986}deg)`;
hrs_dot.style.transform = `rotateZ(${h * 15}deg)`;
min_dot.style.transform = `rotateZ(${m * 6}deg)`;
sec_dot.style.transform = `rotateZ(${s * 6}deg)`;

if (distance <0) {
alert('Finished...!')
}

});



(function(){
    'use strict';
    let item = document.querySelectorAll('.timeline_ul .timeline_li');
    function isElementInViewport(el){
        var rect = el.getBoundingClientRect();
        return(
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= 
            (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <=
            (window.innerWidth || document.documentElement.clientWidth)
        );
        
    }

    function callBackFunction(){
        for(let i = 0; i < item.length; i++){
            if (isElementInViewport(item[i])) {
               
                item[i].classList.add('in_view');
                
            }else{
                item[i].classList.remove('in_view');
        }
    }
    }

    window.addEventListener('load',callBackFunction);
    window.addEventListener('resize',callBackFunction);
    window.addEventListener('scroll',callBackFunction);

})();
