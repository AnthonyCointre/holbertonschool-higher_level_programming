fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => response.json())
  .then((data) => {
    const movies = data.results;
    const list = document.querySelector('#list_movies');

    movies.forEach((movie) => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      list.appendChild(listItem);
    });
  })
  .catch((error) => {
    console.error('Error:', error);
    const list = document.querySelector('#list_movies');
    const listItem = document.createElement('li');
    listItem.textContent = 'Failed to load movies';
    list.appendChild(listItem);
  });
