// JavaScript
var menus = document.querySelectorAll('.menu');
menus.forEach(function(menu) {
  menu.addEventListener('click', function() {
    this.classList.add('active');
  });
});

var dialogs = document.querySelectorAll('dialog');
dialogs.forEach(function(dialog) {
  dialog.addEventListener('close', function() {
    menus.forEach(function(menu) {
      menu.classList.remove('active');
    });
  });
});
