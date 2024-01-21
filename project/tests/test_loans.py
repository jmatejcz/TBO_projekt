import pytest
from datetime import datetime,  timedelta
from project.loans.models import Loan
FAR_PAST_DATE = datetime(1899, 1, 1)
FAR_FUTURE_DATE = datetime.now() + timedelta(days=365 * 10)  # 10 years from now


def test_valid_loan():
    assert Loan(
        customer_name="John Doe", 
        book_name="Sample Book", 
        loan_date=datetime.now(), 
        return_date=datetime.now(), 
        original_author="Jane Doe", 
        original_year_published=2000, 
        original_book_type="Fiction"
    )

def test_invalid_customer_name():
    with pytest.raises(ValueError):
        Loan(
            customer_name="", 
            book_name="Sample Book", 
            loan_date=datetime.now(), 
            return_date=datetime.now(), 
            original_author="Jane Doe", 
            original_year_published=2000, 
            original_book_type="Fiction"
        )

def test_invalid_book_name():
    with pytest.raises(ValueError):
        Loan(
            customer_name="John Doe", 
            book_name="", 
            loan_date=datetime.now(), 
            return_date=datetime.now(), 
            original_author="Jane Doe", 
            original_year_published=2000, 
            original_book_type="Fiction"
        )

def test_invalid_loan_date_type():
    with pytest.raises(TypeError):
        Loan(
            customer_name="John Doe", 
            book_name="Sample Book", 
            loan_date="not a datetime object", 
            return_date=datetime.now(), 
            original_author="Jane Doe", 
            original_year_published=2000, 
            original_book_type="Fiction"
        )

def test_invalid_return_date_type():
    with pytest.raises(TypeError):
        Loan(
            customer_name="John Doe", 
            book_name="Sample Book", 
            loan_date=datetime.now(), 
            return_date="not a datetime object", 
            original_author="Jane Doe", 
            original_year_published=2000, 
            original_book_type="Fiction"
        )

def test_invalid_original_author():
    with pytest.raises(ValueError):
        Loan(
            customer_name="John Doe", 
            book_name="Sample Book", 
            loan_date=datetime.now(), 
            return_date=datetime.now(), 
            original_author="", 
            original_year_published=2000, 
            original_book_type="Fiction"
        )

def test_invalid_original_year_published():
    with pytest.raises(ValueError):
        Loan(
            customer_name="John Doe", 
            book_name="Sample Book", 
            loan_date=datetime.now(), 
            return_date=datetime.now(), 
            original_author="Jane Doe", 
            original_year_published="not an integer", 
            original_book_type="Fiction"
        )

def test_invalid_original_book_type():
    with pytest.raises(ValueError):
        Loan(
            customer_name="John Doe", 
            book_name="Sample Book", 
            loan_date=datetime.now(), 
            return_date=datetime.now(), 
            original_author="Jane Doe", 
            original_year_published=2000, 
            original_book_type=""
        )

def test_book_name_too_short():
    with pytest.raises(ValueError):
        Loan(
            customer_name="John Doe", 
            book_name="ab", 
            loan_date=datetime.now(), 
            return_date=datetime.now(), 
            original_author="Jane Doe", 
            original_year_published=2000, 
            original_book_type="Fiction"
        )

def test_book_name_too_long():
    with pytest.raises(ValueError):
        Loan(
            customer_name="John Doe", 
            book_name="a" * 65,  # 65 characters long
            loan_date=datetime.now(), 
            return_date=datetime.now(), 
            original_author="Jane Doe", 
            original_year_published=2000, 
            original_book_type="Fiction"
        )

def test_customer_name_too_short():
    with pytest.raises(ValueError):
        Loan(
            customer_name="ab", 
            book_name="Sample Book", 
            loan_date=datetime.now(), 
            return_date=datetime.now(), 
            original_author="Jane Doe", 
            original_year_published=2000, 
            original_book_type="Fiction"
        )

def test_customer_name_too_long():
    with pytest.raises(ValueError):
        Loan(
            customer_name="a" * 65,  # 65 characters long
            book_name="Sample Book", 
            loan_date=datetime.now(), 
            return_date=datetime.now(), 
            original_author="Jane Doe", 
            original_year_published=2000, 
            original_book_type="Fiction"
        )

def test_loan_date_too_low():
    with pytest.raises(ValueError):
        Loan(
            customer_name="John Doe", 
            book_name="Sample Book", 
            loan_date=FAR_PAST_DATE, 
            return_date=datetime.now(), 
            original_author="Jane Doe", 
            original_year_published=2000, 
            original_book_type="Fiction"
        )

def test_return_date_too_high():
    with pytest.raises(ValueError):
        Loan(
            customer_name="John Doe", 
            book_name="Sample Book", 
            loan_date=datetime.now(), 
            return_date=FAR_FUTURE_DATE, 
            original_author="Jane Doe", 
            original_year_published=2000, 
            original_book_type="Fiction"
        )

def test_original_year_published_too_low():
    with pytest.raises(ValueError):
        Loan(
            customer_name="John Doe", 
            book_name="Sample Book", 
            loan_date=datetime.now(), 
            return_date=datetime.now(), 
            original_author="Jane Doe", 
            original_year_published=1499,  # Year too low
            original_book_type="Fiction"
        )

def test_original_year_published_too_high():
    with pytest.raises(ValueError):
        Loan(
            customer_name="John Doe", 
            book_name="Sample Book", 
            loan_date=datetime.now(), 
            return_date=datetime.now(), 
            original_author="Jane Doe", 
            original_year_published=datetime.now().year + 1,  # Year in the future
            original_book_type="Fiction"
        )