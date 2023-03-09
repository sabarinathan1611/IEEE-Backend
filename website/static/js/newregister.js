// const checkboxes = document.querySelectorAll('input[type="checkbox"]');

// checkboxes.forEach((checkbox) => {
//   checkbox.addEventListener("change", () => {
//     const numChecked = Array.from(checkboxes).reduce(
//       (acc, checkbox) => acc + (checkbox.checked ? 1 : 0),
//       0
//     );
//     if (numChecked > 2) {
//       checkbox.checked = false;
//       alert("You can only check up to 2 checkboxes.");
//     }
//   });
// });

// const techboxes = document.querySelectorAll(".tech");
// console.log(techboxes);
// let count = 0;
// techval = document.getElementById("techval");
// techboxes.forEach((tech) => {
//   tech.addEventListener("change", () => {
//     const numChecked = Array.from(techboxes).reduce(
//       (acc, tech) => acc + (tech.checked ? 1 : 0),
//       0
//     );
//     if (numChecked >= 1) {
//      techval.value =  1
//     }else{
//       techval.value =  0
//     }
//     console.log("tech Count: ", techval.value);
//   });
// });

// const nontechboxes = document.querySelectorAll(".nontech");
// console.log(nontechboxes);
// let noncount = 0;
// nontechval = document.getElementById("nontechval");
// nontechboxes.forEach((nontech) => {
//   nontech.addEventListener("change", () => {
//     const numChecked = Array.from(nontechboxes).reduce(
//       (acc, nontech) => acc + (nontech.checked ? 1 : 0),
//       0
//     );
//     if (numChecked >= 1) {
//      nontechval.value =  1
//     }else{
//       nontechval.value =  0
//     }
//     console.log("non Count: ", nontechval.value);
//   });
// });

      const front_form = document.querySelector(".front-form");
      const back_form = document.querySelector(".back-form");

     

      const submit = document.querySelector(".submit");

      submit.addEventListener("click", function () {
        alert("queries has been submittes!");
      });

// const yes = document.getElementById('yes');
// console.log(yes);
// const no = document.getElementById('no');
// var memberid = document.getElementById('memberid');
// console.log(no);

// yes.addEventListener('click',function () {
//    alert('you have to bring your member id with you');
//    memberid.style.scale = 1;
// });

// no.addEventListener('click',function(){
//     memberid.style.scale = 0;
//     memberid.value = 'no';
// });

function mem() {
  document.getElementById("member-id").style.scale = 1;
  console.log("member");
  confirm("you should bring your member id copy with you for the event");
}

function nonmem() {
  document.getElementById("member-id").style.scale = 0;
  console.log("non-member");
}




// checkbox function//

const checkboxes = document.querySelectorAll('input[type="checkbox"]');

checkboxes.forEach((checkbox) => {
  checkbox.addEventListener("change", () => {
    const numChecked = Array.from(checkboxes).reduce(
      (acc, checkbox) => acc + (checkbox.checked ? 1 : 0),
      0
    );
    if (numChecked > 2) {
      checkbox.checked = false;
      alert("You can only check up to 2 checkboxes.");
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
     techval.value =  1
    }else{
      techval.value =  0
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
     nontechval.value =  1
    }else{
      nontechval.value =  0
    }
    console.log("non Count: ", nontechval.value);
  });
});


const techteamevent = document.querySelector('#teameventtech');
var techteameventval = document.getElementById('teameventtech');

techteamevent.addEventListener('input',function (){
 if (techteameventval.checked == true) {
  document.getElementById('techteam').style.scale = 1;
  document.getElementById('techmember').style.scale = 1;
 }else{
  document.getElementById('techteam').style.scale = 0;
  document.getElementById('techmember').style.scale = 0;
 }
});

const nontechteamevent = document.querySelector('#teamevent');
var nontechteameventval = document.getElementById('teamevent');

nontechteamevent.addEventListener('input',function (){
  if (nontechteameventval.checked == true) {
   document.getElementById('teamname').style.scale = 1;
   document.getElementById('teammember').style.scale = 1;
  }else{
    document.getElementById('teamname').style.scale = 0;
    document.getElementById('teammember').style.scale = 0;
  }
 });

function checkboxcheck(){
  if (techteameventval.checked == true) {
    document.getElementById('techteam').style.scale = 1;
    document.getElementById('techmember').style.scale = 1;
   }else{
    document.getElementById('techteam').style.scale = 0;
    document.getElementById('techmember').style.scale = 0;
   }
   if (nontechteameventval.checked == true) {
    document.getElementById('teamname').style.scale = 1;
    document.getElementById('teammember').style.scale = 1;
   }else{
     document.getElementById('teamname').style.scale = 0;
     document.getElementById('teammember').style.scale = 0;
   }
}


//  only two team events contraints

const oneteam = document.querySelectorAll('.teambox');
console.log(oneteam);

oneteam.forEach((checkbox) => {
  checkbox.addEventListener("change", () => {
    const numChecked = Array.from(oneteam).reduce(
      (acc, checkbox) => acc + (checkbox.checked ? 1 : 0),
      0
    );
    if (numChecked > 1) {
      checkbox.checked = false;
      checkboxcheck();
      alert("You can only participate on one team event only !");
    }
  });
});

