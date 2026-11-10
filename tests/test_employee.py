import pytest

from employee import Employee


def test_format_salary():
    # Arrange
    fry_cook = Employee("SpongeBob", 40_000)

    # Act
    formatted_salary = fry_cook.format_salary()

    # Assert
    assert formatted_salary == "$40,000.00"


def test_raise_salary():
    # Arrange
    cashier = Employee("Squidward", 35_000)

    # Act
    cashier.raise_salary(3)

    # Assert
    assert cashier.salary == 36_050


def test_raise_salary_rejects_non_positive():
    # Arrange
    manager = Employee("Mr Krabs", 1_000_000)

    # Act
    with pytest.raises(ValueError):
        manager.raise_salary(-5)

    # Assert
    assert manager.salary == 1_000_000
