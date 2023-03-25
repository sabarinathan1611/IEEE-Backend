menu = document.querySelector(".menu").querySelectorAll("a");
// console.log(menu);

menu.forEach((e) => {
  e.addEventListener("click", function () {
    menu.forEach((nav) => nav.classList.remove("active"));

    this.classList.add("active");
  });
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