from dataclasses import dataclass


@dataclass
class Movie:
    name: str
    age_limit: int


def movie_factory(name: str, age_limit: int) -> Movie:
    return Movie(name, age_limit)
