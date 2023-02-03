function send() {
  var String, name;
  var mail;
  var phnum;
  var mess;
  var phlen;
  name = document.getElementById("name").value;
  mail = document.getElementById("mail").value;
  phnum = document.getElementById("phnum").value;
  mess = document.getElementById("mess").value;
  phlen = phnum.length;

  if (name == "") {
    alert("Kindly enter your name..!");
  } else if (phnum == "") {
    alert("Kindly enter your phone number..!");
  } 
  else if (phlen < "10") {
    alert("Check your phone number it is less then 10..!");
  }else if (mail == "") {
    alert("Kindly enter your mail..!");
  } else if (mess == "") {
    alert("Empty request.. Type any query in this page..!");
  } else {
    alert("Thank you '" + name + "' keep in touch...");
  }
}
