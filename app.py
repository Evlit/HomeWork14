# Домашка 14
# Модуль вьшек

from flask import Flask, jsonify

from HomeWork14.function import found_movie_by_name, found_movie_by_year, found_movie_by_rating, found_movie_by_genre

app = Flask(__name__)


@app.route('/movie/<title>')
def get_movie_title_json(title):
    """
    вывод фильма по названию в формате JSON
    """
    executed_query = found_movie_by_name(title)
    if len(executed_query) == 0:
        return "<h1>Фильм с таким названием не найден</h1>"
    return jsonify(executed_query)


@app.route('/movie/<first_date>/to/<end_date>')
def get_movie_year_to_year(first_date, end_date):
    """
    вывод фильмов в диапозоне дат
    """
    executed_query = found_movie_by_year(first_date, end_date)
    if len(executed_query) == 0:
        return "<h1>Фильмов в этом диапозоне дат нет</h1>"
    return executed_query


@app.route('/rating/<category>')
def get_movie_by_raiting(category):
    """
    вывод фильмов по возрастным категориям
    """
    executed_query = found_movie_by_rating(category)
    if len(executed_query) == 0:
        return "<h1>Допустимые категории children, family или adult</h1>"
    return executed_query


@app.route('/genre/<genre>')
def get_movie_by_genre(genre):
    """
    вывод фильмов по жанру
    """
    executed_query = found_movie_by_genre(genre)
    if len(executed_query) == 0:
        return "<h1>Нет фильмов этого жанра</h1>"
    return jsonify(executed_query)


@app.errorhandler(404)
def page_not_found(error):
    """
    Обработка ошибки 404 - страница не найдена
    """
    return "<h1>Страница не найдена, ошибка 404</h1>"


@app.errorhandler(500)
def server_err(error):
    """
    Обработка ошибки 500 - внутренняя ошибка сервера
    """
    return "<h1>Внутренняя ошибка сервера 500 </h1>"


if __name__ == '__main__':
    app.run()
