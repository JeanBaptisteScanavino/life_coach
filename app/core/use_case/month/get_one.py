class GetOnemonth:
    def __init__(self, dependencies):
        self.month_repository = dependencies["month_repository"]
        self.db = dependencies["db"]
        self.month_model = dependencies["month_model"]

    def execute(self, month_id):
        month = self.month_repository(self.db, self.month_model).get_one(month_id)
        return month
