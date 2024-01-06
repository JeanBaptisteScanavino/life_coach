class DeactivateCategory:
    def __init__(self, dependencies):
        self.category_repository = dependencies["category_repository"]
        self.db = dependencies["db"]
        self.category_model = dependencies["category_model"]

    def execute(self, id):
        category = self.category_repository(self.db, self.category_model).get_one(id)
        category.active = False
        new_category = self.category_repository(self.db, self.category_model).update(
            id, category
        )
        return new_category
