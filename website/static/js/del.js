function deleteImg(imageID) {
   
    fetch("/delete-photo", {
      method: "POST",
      body: JSON.stringify({ imageID: imageID }),
    }).then((_res) => {
      window.location.href = "/pic-verify";
      
    });
  }