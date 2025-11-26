console.log("JS подключен!");
document.addEventListener('DOMContentLoaded', function() {
  const btn = document.querySelector('button');
  btn.addEventListener('click', function() {
    alert('Привет, Arman!');
  });
});

