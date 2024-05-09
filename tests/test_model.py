from src.pytemplate.domain.models import Movie, movie_factory
from src.pytemplate.service.checkout import Checkout


def test_init_movie():
    movie = Movie("The Matrix", 15)
    assert movie.name == "The Matrix"
    assert movie.age_limit == 15


def test_movie_factory():
    name, age_limit = "Dune: Part Two", 2024
    movie = movie_factory(name, age_limit)
    assert isinstance(movie, Movie)
    assert movie.name == name
    assert movie.age_limit == age_limit


def test_buy_ticket_for_children_allowed():
    checkout = Checkout()
    movie = Movie(name="Children's Movie", age_limit=6)
    result = checkout.buy_ticket_for_children(movie)
    assert result == "You are allowed to watch the Children's Movie. Enjoy it!"


def test_buy_ticket_for_children_not_allowed():
    checkout = Checkout()
    movie = Movie(name="Children's Movie", age_limit=4)
    result = checkout.buy_ticket_for_children(movie)
    assert result == "Sorry, you are not old enough to watch the Children's Movie."


def test_buy_ticket_for_teens_allowed():
    checkout = Checkout()
    movie = Movie(name="Teenage Movie", age_limit=15)
    result = checkout.buy_ticket_for_teens(movie)
    assert result == "You are allowed to watch the Teenage Movie. Enjoy it!"


def test_buy_ticket_for_teens_not_allowed():
    checkout = Checkout()
    movie = Movie(name="Teenage Movie", age_limit=10)
    result = checkout.buy_ticket_for_teens(movie)
    assert result == "Sorry, you are not old enough to watch the Teenage Movie."


def test_buy_ticket_for_adults_allowed():
    checkout = Checkout()
    movie = Movie(name="Adult Movie", age_limit=18)
    result = checkout.buy_ticket_for_adults(movie)
    assert result == "You are allowed to watch the Adult Movie. Enjoy it!"


def test_buy_ticket_for_adults_not_allowed():
    checkout = Checkout()
    movie = Movie(name="Adult Movie", age_limit=16)
    result = checkout.buy_ticket_for_adults(movie)
    assert result == "Sorry, you are not old enough to watch the Adult Movie."
