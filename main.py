# Модуль для проверки результатов работы функций без вьюшек
from HomeWork14.function import found_actor, found_movie_by_param

# executed_query = found_actor('Jack Black', 'Dustin Hoffman')
executed_query = found_movie_by_param('Movie', '2017', 'Drama')

print(executed_query)
