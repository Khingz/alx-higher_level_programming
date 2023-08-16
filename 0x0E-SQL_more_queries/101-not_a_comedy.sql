-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_shows.title AS title FROM tv_shows
WHERE tv_shows.id NOT IN
(
SELECT tv_show_genres.show_id FROM tv_show_genres
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
)
ORDER BY title;

