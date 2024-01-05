class GetAllMonth:
    def __init__(self, dependencies):
        self.month_repository = dependencies["month_repository"]
        self.db = dependencies["db"]
        self.month_model = dependencies["month_model"]

    def get_all_month(self):
        categories = self.month_repository(self.db, self.month_model).get_all()
        return categories
