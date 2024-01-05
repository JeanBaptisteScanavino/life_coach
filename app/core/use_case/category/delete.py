class DeactivateCategory:
    def __init__(self, dependencies):
        self.category_repository = dependencies["category_repository"]
        self.db = dependencies["db"]
        self.model = dependencies["category_model"]

    def deactivate_category(self, id):
        category = self.category_repository(self.db, self.model).get_one(id)
        category.active = False
        new_category = self.category_repository(self.db, self.model).update(
            id, category
        )
        return new_category
