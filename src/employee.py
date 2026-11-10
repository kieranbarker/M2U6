class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def format_salary(self):
        return f"${self.salary:,.2f}"

    def raise_salary(self, by_percent):
        if by_percent <= 0:
            raise ValueError("by_percent must be positive")
        increase = self.salary * by_percent / 100
        self.salary += increase
