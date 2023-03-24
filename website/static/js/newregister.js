console.log('form js working...!');

const next = document.querySelector('.next');
const next2 = document.querySelector('.next');
const prev = document.querySelector('.prev');
const front = document.querySelector('.front_form');
const back = document.querySelector('.back_form');
const front_form = document.querySelector('.front-form');
const back_form = document.querySelector('.back-form');
const mem_check = document.querySelector('#member');
const username = document.querySelector('#name');
const rollno = document.querySelector('#rollno');
const dept = document.querySelector('#dept');
const year = document.querySelector('#year');
const member = document.querySelector('#member');


mem_check.addEventListener('change', function () {

  var yes = document.getElementById('member').value;

  if (yes === 'yes') {
    document.getElementById('upload').style.display = 'block';
  } else if (yes === 'no') {
    document.getElementById('upload').style.display = 'none';
    error_box.style.scale = '0';
    error_msg.innerHTML = '';
  } else {
    alert('select the option');
  }

});

next.addEventListener('click', function () {
  var yes = document.getElementById('member').value;
  if (username.value === '') {
    var msg = 'fill the name field';
    error(msg);
    console.log('name checked..!');
  } else if (rollno.value === '') {
    var msg = 'fill the rollno field';
    error(msg);
    console.log('rollno checked..!');
  } else if (dept.value === '') {
    var msg = 'select the department ';
    error(msg);
    console.log('department checked..!');
  } else if (year.value === '') {
    var msg = 'select the year';
    error(msg);
    console.log('year checked..!');
  } else if (member.value === '') {
    var msg = 'select the ieee member';
    error(msg);
    console.log('ieee  checked..!');
  } else if (yes === 'yes') {
    document.getElementById('upload').style.display = 'block';
    if (document.getElementById('uploaded').value.length === 0) {
      var msg = 'upload the file';
      error(msg);
    } else {
      front.style.left = '-1000px';
      back.style.left = '20px';
      submit.style.display = 'block';
      prev.style.display = 'block';
      next.style.display = 'none';
    }
  } else {
    front.style.left = '-1000px';
    back.style.left = '20px';
    submit.style.display = 'block';
    prev.style.display = 'block';
    next.style.display = 'none';
  }
});
prev.addEventListener('click', function () {
  front.style.left = '20px';
  back.style.left = '1000px';
  next.style.display = 'block';
  prev.style.display = 'none';
  submit.style.display = 'none';
});



const teamcheck = document.getElementById('teamcheck');
const techteamcheck = document.getElementById('techteamcheck');


teamcheck.addEventListener('click', function () {
  if (teamcheck.checked === true) {
    var msg = 'each and every team members should register seperately with same team name !';
    error(msg);
  } else {
    error_box.style.scale = '0';
    error_msg.innerHTML = '';
  }
});


techteamcheck.addEventListener('click', function () {
  if (techteamcheck.checked === true) {
    var msg = 'each and every team members should register seperately with same team name !';
    error(msg);
  } else {
    error_box.style.scale = '0';
    error_msg.innerHTML = '';
  }
});





const error_box = document.querySelector('.error_box');
const error_msg = document.querySelector('#error_msg');
const close_btn = document.querySelector('.close_btn');

function error(msg) {
  error_box.style.scale = '1';
  error_msg.innerHTML = msg;
}
close_btn.addEventListener('click', function () {
  error_box.style.scale = '0';
  error_msg.innerHTML = '';
})


// check box //

var checkarr = [];

const checkboxes = document.querySelectorAll('input[type="checkbox"]');




checkboxes.forEach((checkbox) => {
  checkbox.addEventListener("change", () => {
    const numChecked = Array.from(checkboxes).reduce(
      (acc, checkbox) => acc + (checkbox.checked ? 1 : 0),
      0

    );
    if (numChecked > 2) {
      checkbox.checked = false;
      var msg = "You can register only two events .";
      error(msg);
    }
  });
});

const techboxes = document.querySelectorAll(".tech");
console.log(techboxes);
let count = 0;
techval = document.getElementById("techval");
techboxes.forEach((tech) => {
  tech.addEventListener("change", () => {
    const numChecked = Array.from(techboxes).reduce(
      (acc, tech) => acc + (tech.checked ? 1 : 0),
      0
    );
    if (numChecked >= 1) {
      techval.value = 1
    } else {
      techval.value = 0
    }
    console.log("tech Count: ", techval.value);
  });
});

const nontechboxes = document.querySelectorAll(".nontech");
console.log(nontechboxes);
let noncount = 0;
nontechval = document.getElementById("nontechval");
nontechboxes.forEach((nontech) => {
  nontech.addEventListener("change", () => {
    const numChecked = Array.from(nontechboxes).reduce(
      (acc, nontech) => acc + (nontech.checked ? 1 : 0),
      0
    );
    if (numChecked >= 1) {
      nontechval.value = 1
    } else {
      nontechval.value = 0
    }
    console.log("non Count: ", nontechval.value);
  });
});


// only one team participate //

const oneteam = document.querySelectorAll('.team_events');
console.log('oneteam ' + oneteam);

oneteam.forEach((checkbox) => {
  checkbox.addEventListener("change", () => {
    const numChecked = Array.from(oneteam).reduce(
      (acc, checkbox) => acc + (checkbox.checked ? 1 : 0),
      0
    );
    if (numChecked > 1) {
      checkbox.checked = false;
      //   checkboxcheck();
      var msg = "You can only participate on one team event only !";
      error(msg);
    }

    if (numChecked >= 1) {
      document.getElementById('teamname_field').style.display = 'block';
      document.getElementById('teammember_field').style.display = 'block';
    } else {
      document.getElementById('teamname_field').style.display = 'none';
      document.getElementById('teammember_field').style.display = 'none';
    }
  });
});


const submit = document.querySelector('.submit');
const techteam = document.querySelector('.techteam');
const nontechteam = document.querySelector('.nontechteam');
console.log(techteam);
console.log(nontechteam);
console.log(nontechteam.checked);

submit.addEventListener('click', function () {



  if (techteam.checked === true || nontechteam.checked === true) {
    var teamname = document.getElementById('teamname').value;
    var teammembers = document.getElementById('teammember').value;



    if (teamname === '') {
      submit.type = 'button';
      var msg = 'fillout the team name....!'
      error(msg);
    } else if (teammembers === '') {
      submit.type = 'button';
      var msg = 'fillout the team members....!'
      error(msg);
    } else {
      submit.type = 'submit';
    }
  } else {
  
    checking();
  }

});




var ch = [];
function checking() {
  checkboxes.forEach((checkbox) => {

    const numChecked = Array.from(checkboxes).reduce(
      (acc, checkbox) => acc + (checkbox.checked ? 1 : 0),
      0

    );

    if (checkbox.checked === true) {
      ch.push('1');
      console.log(ch);

    }


    if (ch.length === 0) {
      console.log(ch.length);
      var msg = 'register atleast in one event...'
      error(msg);
      submit.type = 'button';
    } else {
      submit.type = 'submit';
    }


  });
}
