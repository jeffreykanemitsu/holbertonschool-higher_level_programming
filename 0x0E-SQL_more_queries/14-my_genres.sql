-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_genres.name FROM tv_genres INNER JOIN tv_show_genres x ON x.genre_id = tv_genres.id INNER JOIN tv_shows y ON x.show_id = y.id WHERE y.title = 'Dexter' ORDER BY tv_genres.name;
