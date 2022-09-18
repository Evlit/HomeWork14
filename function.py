# Домашка 14
# Модуль функций
import json
import sqlite3


def found_movie_by_name(name_movie):
    """
    Поиск самого нового фильма по названию

    """
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = ("SELECT title,country,release_year,listed_in,description FROM netflix "
                    "WHERE title = ? AND release_year = (select max(release_year) from netflix WHERE title = ?)")
    cur.execute(sqlite_query, (name_movie, name_movie))
    executed_query = cur.fetchall()
    if len(executed_query) == 0:
        dict_result = {}
    else:
        dict_result = {'title': executed_query[0][0], 'country': executed_query[0][1],
                       'release_year': executed_query[0][2], 'genre': executed_query[0][3],
                       'description': executed_query[0][4]}
    con.close()
    return dict_result


def found_movie_by_year(first_date, end_date):
    """
    Поиск фильма в диапазоне дат

    """
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = "SELECT title,release_year FROM netflix  WHERE release_year BETWEEN ? AND ? LIMIT 100"
    cur.execute(sqlite_query, (first_date, end_date))
    executed_query = cur.fetchall()
    con.close()

    title_year = []
    for row in executed_query:
        dict_result = {'title': row[0], 'release_year': row[1]}
        title_year.append(dict_result)
    return title_year


def found_movie_by_rating(name_rating):
    """
    Поиск фильмов по возрастному рейтингу
    """
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()

    if name_rating == 'family':
        sqlite_query = "SELECT title,rating,description FROM netflix WHERE rating in ('G', 'PG', 'PG-13')"
    elif name_rating == 'adult':
        sqlite_query = "SELECT title,rating,description FROM netflix WHERE rating in ('R','NC-17')"
    elif name_rating == 'children':
        sqlite_query = "SELECT title,rating,description FROM netflix WHERE rating in ('G')"
    else:
        sqlite_query = "SELECT title,rating,description FROM netflix WHERE rating in ('XXXXXXX')"

    cur.execute(sqlite_query)
    executed_query = cur.fetchall()
    con.close()

    raiting_list = []
    for row in executed_query:
        dict_result = {'title': row[0], 'rating': row[1], 'description': row[2]}
        raiting_list.append(dict_result)
    return raiting_list


def found_movie_by_genre(name_genre):
    """
    Поиск фильмов по жанру
    """
    name_genre = '%' + name_genre + '%'
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = "SELECT title,description FROM netflix WHERE listed_in LIKE ? ORDER BY release_year DESC LIMIT 10"
    cur.execute(sqlite_query, (name_genre,))
    executed_query = cur.fetchall()
    con.close()

    genre_list = []
    for row in executed_query:
        dict_result = {'title': row[0], 'description': row[1]}
        genre_list.append(dict_result)
    return genre_list


def found_actor(name1, name2):
    """
    Вывод списка актеров, снимавшихся более 2 раз
    с актерами, указанными в параметрах
    """
    nameq1 = '%' + name1 + '%'
    nameq2 = '%' + name2 + '%'
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = "SELECT title,netflix.cast  FROM netflix WHERE netflix.cast LIKE ? AND netflix.cast LIKE ?"
    cur.execute(sqlite_query, (nameq1, nameq2))
    executed_query = cur.fetchall()
    con.close()

    cast_list = []
    for row in executed_query:
        cast_list = cast_list + row[1].split(',')
    cast_list = [x.strip(' ') for x in cast_list]

    partner_list = []
    for actor in set(cast_list):
        if cast_list.count(actor) > 2 and actor not in (name1, name2):
            partner_list.append(actor)
    return partner_list


def found_movie_by_param(type_, year_, genre):
    """
    Поиск и вывод фильмов по типу, году выпуска и жанру в JSON

    """
    genre = '%' + genre + '%'
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = "SELECT title,description FROM netflix  WHERE type = ? AND release_year = ? AND listed_in LIKE ? "
    cur.execute(sqlite_query, (type_, year_, genre))
    executed_query = cur.fetchall()
    con.close()

    genre_list = []
    for row in executed_query:
        dict_result = {'title': row[0], 'description': row[1]}
        genre_list.append(dict_result)
    return json.dumps(genre_list)
