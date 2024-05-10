def age_limit_6plus(func):
    def wrapper(self, movie):
        if movie.customer_age >= 6:
            return func(self, movie)
        else:
            return f"Sorry, you are not old enough to watch {movie.name}."

    return wrapper


def age_limit_13plus(func):
    def wrapper(self, movie):
        if movie.customer_age >= 13:
            return func(self, movie)
        else:
            return f"Sorry, you are not old enough to watch {movie.name}."

    return wrapper


def age_limit_18plus(func):
    def wrapper(self, movie):
        if movie.customer_age >= 18:
            return func(self, movie)
        else:
            return f"Sorry, you are not old enough to watch {movie.name}."

    return wrapper
