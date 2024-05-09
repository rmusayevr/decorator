from pytemplate.domain.models import Movie
from pytemplate.utils.decorator import age_limit_6plus, age_limit_13plus, age_limit_18plus


class Checkout:
    @age_limit_6plus
    def buy_ticket_for_children(self, movie: Movie) -> str:
        return f"You are allowed to watch the {movie.name}. Enjoy it!"

    @age_limit_13plus
    def buy_ticket_for_teens(self, movie: Movie) -> str:
        return f"You are allowed to watch the {movie.name}. Enjoy it!"

    @age_limit_18plus
    def buy_ticket_for_adults(self, movie: Movie) -> str:
        return f"You are allowed to watch the {movie.name}. Enjoy it!"
