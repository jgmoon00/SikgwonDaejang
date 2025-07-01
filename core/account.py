from core.company import Company

class Account:
    def __init__(self, userId: str, name: str, company: Company):
        self.userId = userId
        self.name = name
        self.company = company
