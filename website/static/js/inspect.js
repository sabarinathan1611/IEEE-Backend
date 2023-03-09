document.addEventListener('keydown', function(event) {
    if (event.keyCode == 123) { // 123 is the keyCode for F12 key
      event.preventDefault();
      return false;
    }
  });
  document.addEventListener('keydown', function(event) {
    if (event.keyCode == 73) { // 123 is the keyCode for F12 key
      event.preventDefault();
      return false;
    }
  });
  document.addEventListener('keydown', function(event) {
    if (event.keyCode == 105) { // 123 is the keyCode for F12 key
      event.preventDefault();
      return false;
    }
  });
  document.addEventListener('contextmenu', function(event) {
    event.preventDefault();
    return false;
  });