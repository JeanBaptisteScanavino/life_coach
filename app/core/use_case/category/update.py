class UpdateCategory:
    def __init__(self, dependencies):
        self.category_repository = dependencies["category_repository"]
        self.db = dependencies["db"]
        self.model = dependencies["category_model"]

    def update_category(self, id, category):
        category = self.category_repository(self.db, self.model).update(id, category)
        return category
