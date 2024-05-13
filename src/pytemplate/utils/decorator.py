from functools import wraps

from pytemplate.domain.models import Movie


def age_limit_6plus(func):
    @wraps(func)
    def wrapper(self, movie: Movie):
        if movie.customer_age >= 6:
            return func(self, movie)
        else:
            return f"Sorry, you are not old enough to watch {movie.name}."

    return wrapper


def age_limit_13plus(func):
    @wraps(func)
    def wrapper(self, movie: Movie):
        if movie.customer_age >= 13:
            return func(self, movie)
        else:
            return f"Sorry, you are not old enough to watch {movie.name}."

    return wrapper


def age_limit_18plus(func):
    @wraps(func)
    def wrapper(self, movie: Movie):
        if movie.customer_age >= 18:
            return func(self, movie)
        else:
            return f"Sorry, you are not old enough to watch {movie.name}."

    return wrapper
