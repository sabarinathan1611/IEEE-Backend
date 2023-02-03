menu = document.querySelector(".menu").querySelectorAll("a");
// console.log(menu);

menu.forEach((e) => {
  e.addEventListener("click", function () {
    menu.forEach((nav) => nav.classList.remove("active"));

    this.classList.add("active");
  });
});
//home next button and events prev button
menu = document.querySelector(".menu").querySelectorAll("a");
// console.log(menu);

const even = document.querySelector(".event");
// console.log(even);

const home = document.querySelector(".home");
// console.log(home);

const hnext = document.querySelector(".hnext");
// console.log(hnext);

const eprev = document.querySelector(".eprev");
// console.log(eprev);


hnext.addEventListener("click", function () {
  menu.forEach((nav) => nav.classList.remove("active"));

  even.classList.add("active");
});

eprev.addEventListener("click", function () {
  menu.forEach((nav) => nav.classList.remove("active"));

  home.classList.add("active");
});

//even next button and tech prev button

const tech = document.querySelector(".tech");
// console.log(tech);



const enext = document.querySelector(".enext");
// console.log(enext);

const tprev = document.querySelector(".tprev");
// console.log(eprev);


enext.addEventListener("click", function () {
  menu.forEach((nav) => nav.classList.remove("active"));

  tech.classList.add("active");
});

tprev.addEventListener("click", function () {
  menu.forEach((nav) => nav.classList.remove("active"));

  even.classList.add("active");
});

//tech next button and non-tech prev button

const ntech = document.querySelector(".non-tech");
// console.log(ntech);

const tnext = document.querySelector(".tnext");
// console.log(tnext);

const nprev = document.querySelector(".nprev");
// console.log(nprev);

tnext.addEventListener("click", function () {
  menu.forEach((nav) => nav.classList.remove("active"));

 ntech.classList.add("active");
});

nprev.addEventListener("click", function () {
  menu.forEach((nav) => nav.classList.remove("active"));

  tech.classList.add("active");
});

// non-tech next button and contact prev button

const contact  = document.querySelector(".contact");
// console.log(contact);

const nnext = document.querySelector(".nnext");
// console.log(nnext);

const cprev = document.querySelector(".cprev");
// console.log(cprev);

nnext.addEventListener("click", function () {
  menu.forEach((nav) => nav.classList.remove("active"));

 contact.classList.add("active");
});

cprev.addEventListener("click", function () {
  menu.forEach((nav) => nav.classList.remove("active"));

  ntech.classList.add("active");
});

// onscroll function 

const sections = document.querySelectorAll("section");
console.log(sections);
const navLi = document.querySelectorAll("nav ul li");
console.log(navLi);
window.onscroll = () => {
  var current = "";
  // window.pageYOffset ;

  sections.forEach((section) => {
    const sectionTop = section.offsetTop;
    if (window.pageYOffset >= sectionTop - 60) {
      current = section.getAttribute("id"); }
      // console.log(current ,'current');
      if (current === 'home') {
        menu.forEach((nav) => nav.classList.remove("active"));

        home.classList.add("active");
        console.log('home');
      } else if (current ==='event') {
        menu.forEach((nav) => nav.classList.remove("active"));

        even.classList.add("active");
      } else if (current ==='tech') {
        menu.forEach((nav) => nav.classList.remove("active"));

        tech.classList.add("active");
      }
      else if (current ==='non-tech') {
        menu.forEach((nav) => nav.classList.remove("active"));

        ntech.classList.add("active");
      }else{
        menu.forEach((nav) => nav.classList.remove("active"));

        contact.classList.add("active");
      }
  });

  // navLi.forEach((li) => {
  //   li.classList.remove("active");
  //   if (li.classList.contains(current)) {
  //     li.classList.add("active");
  //   }
  // });
};