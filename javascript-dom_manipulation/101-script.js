document.addEventListener('DOMContentLoaded', function () {
  const translateButton = document.getElementById('btn_translate');
  const languageSelect = document.getElementById('language_code');
  const helloDiv = document.getElementById('hello');

  translateButton.addEventListener('click', function () {
    const languageCode = languageSelect.value;
    if (languageCode) {
      const apiUrl = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;
      fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
          if (data.hello) {
            helloDiv.textContent = data.hello;
          } else {
            helloDiv.textContent = 'Translation not found';
          }
        })
        .catch(error => {
          console.error('Error:', error);
          helloDiv.textContent = 'An error occurred';
        });
    } else {
      helloDiv.textContent = 'Please select a language';
    }
  });
});
