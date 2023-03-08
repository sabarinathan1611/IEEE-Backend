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
