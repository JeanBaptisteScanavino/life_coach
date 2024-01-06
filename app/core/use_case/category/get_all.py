class GetAllCategory:
    def __init__(self, dependencies):
        self.category_repository = dependencies["category_repository"]
        self.db = dependencies["db"]
        self.category_model = dependencies["category_model"]

    def execute(self):
        categories = self.category_repository(self.db, self.category_model).get_all()
        return categories
