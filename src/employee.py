class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def format_salary(self):
        return f"${self.salary:,.2f}"

    def raise_salary(self, by_percent):
        pass
