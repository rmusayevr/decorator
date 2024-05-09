def age_limit_6plus(func):
    def wrapper(self, movie):
        if movie.age_limit >= 6:
            return func(self, movie)
        else:
            return f"Sorry, you are not old enough to watch the {movie.name}."

    return wrapper


def age_limit_13plus(func):
    def wrapper(self, movie):
        if movie.age_limit >= 13:
            return func(self, movie)
        else:
            return f"Sorry, you are not old enough to watch the {movie.name}."

    return wrapper


def age_limit_18plus(func):
    def wrapper(self, movie):
        if movie.age_limit >= 18:
            return func(self, movie)
        else:
            return f"Sorry, you are not old enough to watch the {movie.name}."

    return wrapper
