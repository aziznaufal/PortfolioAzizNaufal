class TransactionDTO:
    def __init__(self, id, description, amount, category):
        self.id = id
        self.description = description
        self.amount = amount
        self.category = category

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "amount": self.amount,
            "category": self.category
        }

    @staticmethod
    def from_dict(data):
        return TransactionDTO(
            id=data.get("id"),
            description=data.get("description"),
            amount=data.get("amount"),
            category=data.get("category")
        )
