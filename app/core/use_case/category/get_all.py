class GetAllCategory:
    def __init__(self, dependencies):
        self.category_repository = dependencies["category_repository"]
        self.db = dependencies["db"]
        self.model = dependencies["category_model"]

    def get_all_category(self):
        categories = self.category_repository(self.db, self.model).get_all()
        return categories
