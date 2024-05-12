from io import StringIO
from unittest.mock import patch

from pytemplate.entrypoints.cli.main import main
from src.pytemplate.domain.models import Movie, movie_factory
from src.pytemplate.service.checkout import Checkout


def test_init_movie():
    movie = Movie("The Matrix", 15)
    assert movie.name == "The Matrix"
    assert movie.customer_age == 15


def test_movie_factory():
    name, customer_age = "Dune: Part Two", 21
    movie = movie_factory(name, customer_age)
    assert isinstance(movie, Movie)
    assert movie.name == name
    assert movie.customer_age == customer_age


def test_buy_ticket_for_children_allowed():
    checkout = Checkout()
    movie = Movie("Migration", 6)
    result = checkout.buy_ticket_for_children(movie)
    assert result == "You are allowed to watch Migration."


def test_buy_ticket_for_children_not_allowed():
    checkout = Checkout()
    movie = Movie("Migration", 4)
    result = checkout.buy_ticket_for_children(movie)
    assert result == "Sorry, you are not old enough to watch Migration."


def test_buy_ticket_for_teens_allowed():
    checkout = Checkout()
    movie = Movie("Easy A", 13)
    result = checkout.buy_ticket_for_teens(movie)
    assert result == "You are allowed to watch Easy A."


def test_buy_ticket_for_teens_not_allowed():
    checkout = Checkout()
    movie = Movie("Easy A", 10)
    result = checkout.buy_ticket_for_teens(movie)
    assert result == "Sorry, you are not old enough to watch Easy A."


def test_buy_ticket_for_adults_allowed():
    checkout = Checkout()
    movie = Movie("The Nice Guys", 18)
    result = checkout.buy_ticket_for_adults(movie)
    assert result == "You are allowed to watch The Nice Guys."


def test_buy_ticket_for_adults_not_allowed():
    checkout = Checkout()
    movie = Movie("The Nice Guys", 16)
    result = checkout.buy_ticket_for_adults(movie)
    assert result == "Sorry, you are not old enough to watch The Nice Guys."


@patch("builtins.input", side_effect=["Ponyo", 8, 6])
def test_main_allowed_6plus(mock_input):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        main()
        assert mock_stdout.getvalue().strip() == "You are allowed to watch Ponyo."


@patch("builtins.input", side_effect=["Ponyo", 4, 6])
def test_main_not_allowed_6plus(mock_input):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        main()
        assert mock_stdout.getvalue().strip() == "Sorry, you are not old enough to watch Ponyo."


@patch("builtins.input", side_effect=["Monster", 14, 13])
def test_main_allowed_13plus(mock_input):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        main()
        assert mock_stdout.getvalue().strip() == "You are allowed to watch Monster."


@patch("builtins.input", side_effect=["Monster", 12, 13])
def test_main_not_allowed_13plus(mock_input):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        main()
        assert mock_stdout.getvalue().strip() == "Sorry, you are not old enough to watch Monster."


@patch("builtins.input", side_effect=["The Hunt", 21, 18])
def test_main_allowed_18plus(mock_input):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        main()
        assert mock_stdout.getvalue().strip() == "You are allowed to watch The Hunt."


@patch("builtins.input", side_effect=["The Hunt", 15, 18])
def test_main_not_allowed_18plus(mock_input):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        main()
        assert mock_stdout.getvalue().strip() == "Sorry, you are not old enough to watch The Hunt."


@patch("builtins.input", side_effect=["The Hunt", 21, 0])
def test_main_invalid_action(mock_input):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        main()
        assert mock_stdout.getvalue().strip() == "Invalid action! Please choose 6/13/18."
