class CreateCategory:
    def __init__(self, dependencies):
        self.category_repository = dependencies["category_repository"]
        self.db = dependencies["db"]
        self.model = dependencies["category_model"]

    def create_category(self, category):
        category = self.category_repository(self.db, self.model).create(category)
        return category