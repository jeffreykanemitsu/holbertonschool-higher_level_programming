$.get('https://swapi.co/api/films/?format=json', function (movie) {
  let movies = movie.results;
  for (let titles in movies) {
    $('UL#list_movies').append('<li>' + movies[titles].title + '</li>');
  }
});
