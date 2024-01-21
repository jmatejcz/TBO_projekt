from project.books.models import Book
import pytest

def test_valid_input():
    assert Book(name="kubi", author="pawel", year_published=2000, book_type="criminal")

def test_invalid_name_type():
    with pytest.raises(ValueError):
        Book(name=123, author="pawel", year_published=2000, book_type="criminal")

def test_name_too_short():
    with pytest.raises(ValueError):
        Book(name="ab", author="pawel", year_published=2000, book_type="criminal")

def test_name_too_long():
    with pytest.raises(ValueError):
        Book(name="a" * 41, author="pawel", year_published=2000, book_type="criminal")

def test_author_not_string():
    with pytest.raises(ValueError):
        Book(name="kubi", author=123, year_published=2000, book_type="criminal")

def test_year_published_not_int():
    with pytest.raises(ValueError):
        Book(name="kubi", author="pawel", year_published="2000", book_type="criminal")

def test_year_published_too_high():
    with pytest.raises(ValueError):
        Book(name="kubi", author="pawel", year_published=2024, book_type="criminal")

def test_year_published_too_low():
    with pytest.raises(ValueError):
        Book(name="kubi", author="pawel", year_published=-1, book_type="criminal")

def test_book_type_not_string():
    with pytest.raises(ValueError):
        Book(name="kubi", author="pawel", year_published=2000, book_type=123)