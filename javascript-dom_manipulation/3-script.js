document.querySelector('#toggle_header').addEventListener('click', function() {
  const headerElement = document.querySelector('header');
  if (headerElement.classList.contains('red')) {
      headerElement.classList.replace('red', 'green');
  } else {
      headerElement.classList.replace('green', 'red');
  }
});
