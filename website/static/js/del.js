console.log("work");
function deleteImg(imageID) {
   
    fetch("/delete-photo", {
      method: "POST",
      body: JSON.stringify({ imageID: imageID }),
    }).then((_res) => {
      window.location.href = "/pic-verify";
      
    });
  }


//   const delbtn = document.querySelector('.delbtn');
//   console.log(delbtn);

// delbtn.addEventListener('click',function () {
//   console.log('called');
//  var imageID = document.getElementById('id').value;
//  console.log(imageID);
//   deleteImg(imageID);
// });