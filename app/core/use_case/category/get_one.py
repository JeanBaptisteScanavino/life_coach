class GetOneCategory:
    def __init__(self, dependencies):
        self.category_repository = dependencies["category_repository"]
        self.db = dependencies["db"]
        self.category_model = dependencies["category_model"]

    def execute(self, category_id):
        category = self.category_repository(self.db, self.category_model).get_one(category_id)
        return category
