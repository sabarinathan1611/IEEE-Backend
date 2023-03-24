const filter = document.querySelector('#filter');

const event1 = document.querySelector('.event1');
const event2 = document.querySelector('.event2');
const event3 = document.querySelector('.event3');
const event4 = document.querySelector('.event4');
const event5 = document.querySelector('.event5');
const event6 = document.querySelector('.event6');
const event7 = document.querySelector('.event7');
const event8 = document.querySelector('.event8');
const event9 = document.querySelector('.event9');

filter.addEventListener('change',function(){
var filterVal = document.getElementById('filter').value;
  if (filterVal === 'event1') {
    event1.style.display = 'block';

    event2.style.display = 'none';
    event3.style.display = 'none';
    event4.style.display = 'none';
    event5.style.display = 'none';
    event6.style.display = 'none';
    event7.style.display = 'none';
    event8.style.display = 'none';
    event9.style.display = 'none';
  }else  if (filterVal === 'event2') {
    event2.style.display = 'block';

    event1.style.display = 'none';
    event3.style.display = 'none';
    event4.style.display = 'none';
    event5.style.display = 'none';
    event6.style.display = 'none';
    event7.style.display = 'none';
    event8.style.display = 'none';
    event9.style.display = 'none';
  }else  if (filterVal === 'event3') {
    event3.style.display = 'block';

    event2.style.display = 'none';
    event1.style.display = 'none';
    event4.style.display = 'none';
    event5.style.display = 'none';
    event6.style.display = 'none';
    event7.style.display = 'none';
    event8.style.display = 'none';
    event9.style.display = 'none';
  }else  if (filterVal === 'event4') {
    event4.style.display = 'block';

    event2.style.display = 'none';
    event3.style.display = 'none';
    event1.style.display = 'none';
    event5.style.display = 'none';
    event6.style.display = 'none';
    event7.style.display = 'none';
    event8.style.display = 'none';
    event9.style.display = 'none';
  }else  if (filterVal === 'event5') {
    event5.style.display = 'block';

    event2.style.display = 'none';
    event3.style.display = 'none';
    event4.style.display = 'none';
    event1.style.display = 'none';
    event6.style.display = 'none';
    event7.style.display = 'none';
    event8.style.display = 'none';
    event9.style.display = 'none';
  }else  if (filterVal === 'event6') {
    event6.style.display = 'block';

    event2.style.display = 'none';
    event3.style.display = 'none';
    event4.style.display = 'none';
    event5.style.display = 'none';
    event1.style.display = 'none';
    event7.style.display = 'none';
    event8.style.display = 'none';
    event9.style.display = 'none';
  }else  if (filterVal === 'event7') {
    event7.style.display = 'block';

    event2.style.display = 'none';
    event3.style.display = 'none';
    event4.style.display = 'none';
    event5.style.display = 'none';
    event6.style.display = 'none';
    event1.style.display = 'none';
    event8.style.display = 'none';
    event9.style.display = 'none';
  }else  if (filterVal === 'event8') {
    event8.style.display = 'block';

    event2.style.display = 'none';
    event3.style.display = 'none';
    event4.style.display = 'none';
    event5.style.display = 'none';
    event6.style.display = 'none';
    event7.style.display = 'none';
    event1.style.display = 'none';
    event9.style.display = 'none';
  }else  if (filterVal === 'event9') {
    event9.style.display = 'block';

    event2.style.display = 'none';
    event3.style.display = 'none';
    event4.style.display = 'none';
    event5.style.display = 'none';
    event6.style.display = 'none';
    event7.style.display = 'none';
    event8.style.display = 'none';
    event1.style.display = 'none';
  }else if (filterVal === 'all') {
    event9.style.display = 'block';

    event2.style.display = 'block';
    event3.style.display = 'block';
    event4.style.display = 'block';
    event5.style.display = 'block';
    event6.style.display = 'block';
    event7.style.display = 'block';
    event8.style.display = 'block';
    event1.style.display = 'block';
  }else{
    alert('select any option to filter !' );
  }

});