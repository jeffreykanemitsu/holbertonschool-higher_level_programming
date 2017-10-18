-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT tv_shows.title FROM tv_shows INNER JOIN tv_show_genres x ON x.show_id = tv_shows.id INNER JOIN tv_genres y ON x.genre_id = y.id WHERE y.name = 'Comedy' ORDER BY tv_shows.title ASC;
