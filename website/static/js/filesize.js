var uploadField = document.getElementById("uploaded");

uploadField.onchange = function() {
    if(this.files[0].size > 3000000){
       var msg = 'file size is too large .....!'
       error(msg);
       this.value = "";
    };
};

const errorbox = document.querySelector('.error_box');
const errormsg = document.querySelector('#error_msg');
const closebtn = document.querySelector('.close_btn');

function error(msg) {
  errorbox.style.scale = '1';
  errormsg.innerHTML = msg;
}
close_btn.addEventListener('click', function () {
  errorbox.style.scale = '0';
  errormsg.innerHTML = '';
});