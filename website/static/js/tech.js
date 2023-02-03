const li1 = document.querySelector('.li1');
const li2 = document.querySelector('.li2');
const li3 = document.querySelector('.li3');
const li4 = document.querySelector('.li4');
// console.log(li1);

const event1 = document.querySelector('.event1-description');
const event2 = document.querySelector('.event2-description');
const event3 = document.querySelector('.event3-description');
const event4 = document.querySelector('.event4-description');

// console.log(event4);


li1.addEventListener('click', function(){
    event1.style.scale = 1;
    event2.style.scale = 0;
    event3.style.scale = 0;
    event4.style.scale = 0;
});

li2.addEventListener('click', function(){
    event1.style.scale = 0;
    event2.style.scale = 1;
    event3.style.scale = 0;
    event4.style.scale = 0;
});

li3.addEventListener('click', function(){
    event1.style.scale = 0;
    event2.style.scale = 0;
    event3.style.scale = 1;
    event4.style.scale = 0;
});

li4.addEventListener('click', function(){
    event1.style.scale = 0;
    event2.style.scale = 0;
    event3.style.scale = 0;
    event4.style.scale = 1;
});