class UpdateCategory:
    def __init__(self, dependencies):
        self.category_repository = dependencies["category_repository"]
        self.db = dependencies["db"]
        self.category_model = dependencies["category_model"]

    def execute(self, id, category):
        category = self.category_repository(self.db, self.category_model).update(id, category)
        return category
