from project.books.models import Book
import pytest

# Test IDs for parametrization
HAPPY_PATH_ID = "happy_path"
EDGE_CASE_ID = "edge_case"
ERROR_CASE_ID = "error_case"
SQL_INJECTION_ID = "sql_injection"
JS_INJECTION_ID = "js_injection"
EXTREME_CASE_ID = "extreme_case"

# Happy path test values
happy_path_params = [
    (HAPPY_PATH_ID, "The Great Gatsby", "F. Scott Fitzgerald", 1925, "Novel"),
    (HAPPY_PATH_ID, "1984", "George Orwell", 1949, "Dystopian"),
    (HAPPY_PATH_ID, "To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    (HAPPY_PATH_ID, "X" * 64, "X" * 64, 1960, "Fiction"),
]

# Error case test values
error_case_params = [
    (ERROR_CASE_ID, None, "Author", 2023, "Type"),
    (ERROR_CASE_ID, "", "Author", 2023, "Type"),
    (ERROR_CASE_ID, "\t", "Author", 2023, "Type"),
    (ERROR_CASE_ID, " ", "Author", 2023, "Type"),
    (ERROR_CASE_ID, "\n", "Author", 2023, "Type"),
    (ERROR_CASE_ID, "Valid Name", None, 2023, "Type"),
    (ERROR_CASE_ID, "Valid Name", "!@#$%^&*()", 2023, "Type"),
    (ERROR_CASE_ID, "Valid Name", "\n", 2023, "Type"),
    (ERROR_CASE_ID, "Valid Name", " ", 2023, "Type"),
    (ERROR_CASE_ID, "Valid Name", "\t", 2023, "Type"),
    (ERROR_CASE_ID, "Valid Name", "", 2023, "Type"),
    (ERROR_CASE_ID, "Valid Name", "Author", "Year", "Type"),
    (ERROR_CASE_ID, "Valid Name", "Author", -1, "Type"),
    (ERROR_CASE_ID, "Valid Name", "Author", 0, "Type"),
    (ERROR_CASE_ID, "Valid Name", "Author", None, "Type"),
    (ERROR_CASE_ID, "Valid Name", "Author", 1990, None),
    (ERROR_CASE_ID, "Valid Name", "Author", 1990, ""),
    (ERROR_CASE_ID, "Valid Name", "Author", 1990, "\t"),
    (ERROR_CASE_ID, "Valid Name", "Author", 1990, " "),
    (ERROR_CASE_ID, "Valid Name", "Author", 1990, "\n"),
    (ERROR_CASE_ID, "Valid Name", "Author", 1990, "!@#$%^&*()"),
    (ERROR_CASE_ID, "Valid Name", "Author", 10000, "Type"),
]

# Edge case test values
edge_case_params = [
    (EDGE_CASE_ID, "A", "B", 1, "C"),  # Minimal valid input
    (EDGE_CASE_ID, " " * 64, " " * 64, 1, " " * 20),  # Max length spaces
    (EDGE_CASE_ID, "X" * 64, "X" * 64, 1, "X" * 20),  # Max length characters
]

# SQL injection test values
sql_injection_params = [
    (SQL_INJECTION_ID, "-- or # ", "-- or # ", 1990, "Type"),
    (SQL_INJECTION_ID, "' OR 1 = 1 -- -'", "' OR 1 = 1 -- -'", 1990, "Type"),
    (SQL_INJECTION_ID, "1' ORDER BY 1--+", "1' ORDER BY 1--+", 1990, "Type"),
    (
        SQL_INJECTION_ID,
        "' UNION SELECT sum(columname) from tablename --",
        "' UNION SELECT sum(columname) from tablename --",
        1990,
        "Type",
    ),
    (
        SQL_INJECTION_ID,
        ", (select * from (select(sleep(10)))a) --",
        ", (select * from (select(sleep(10)))a) --",
        1990,
        "Type",
    ),
]

js_injection_params = [
    (JS_INJECTION_ID, "<script>alert('TestName')</script>", "Author", 1990, "Type"),
    (JS_INJECTION_ID, "TestName", "<script>alert('Author')</script>", 1990, "Type"),
]

extreme_case_params = [
    (EXTREME_CASE_ID, "X" * 10000, "X" * 10000, 10000, "X" * 10000),
    (EXTREME_CASE_ID, "X" * 100000, "X" * 100000, 100000, "X" * 100000),
    (EXTREME_CASE_ID, "X" * 1000000, "X" * 1000000, 1000000, "X" * 1000000),
]


# Parametrized test for happy path
@pytest.mark.parametrize(
    "test_id, name, author, year_published, book_type", happy_path_params
)
def test_book_creation_happy_path(test_id, name, author, year_published, book_type):
    book = Book(name, author, year_published, book_type)

    # Assert
    assert book.name == name
    assert book.author == author
    assert book.year_published == year_published
    assert book.book_type == book_type
    assert book.status == "available"


# Parametrized test for edge cases
@pytest.mark.parametrize(
    "test_id, name, author, year_published, book_type", edge_case_params
)
def test_book_creation_edge_cases(test_id, name, author, year_published, book_type):
    book = Book(name, author, year_published, book_type)

    # Assert
    assert book.name == name
    assert book.author == author
    assert book.year_published == year_published
    assert book.book_type == book_type
    assert book.status == "available"


# Parametrized test for error cases
@pytest.mark.parametrize(
    "test_id, name, author, year_published, book_type", error_case_params
)
def test_book_creation_error_cases(test_id, name, author, year_published, book_type):
    with pytest.raises(ValueError):
        Book(name, author, year_published, book_type)


@pytest.mark.parametrize(
    "test_id, name, author, year_published, book_type", sql_injection_params
)
def test_book_sql_injection(test_id, name, author, year_published, book_type):
    with pytest.raises(ValueError):
        Book(name, author, year_published, book_type)


@pytest.mark.parametrize(
    "test_id, name, author, year_published, book_type", js_injection_params
)
def test_book_js_injection(test_id, name, author, year_published, book_type):
    with pytest.raises(ValueError):
        Book(name, author, year_published, book_type)


@pytest.mark.parametrize(
    "test_id, name, author, year_published, book_type", extreme_case_params
)
def test_book_creation_extreme_cases(test_id, name, author, year_published, book_type):
    with pytest.raises(ValueError):
        Book(name, author, year_published, book_type)


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
