class CreateMonth:
    def __init__(self, dependencies):
        self.month_repository = dependencies["month_repository"]
        self.db = dependencies["db"]
        self.month_model = dependencies["month_model"]

    def execute(self):
        new_month = self.month_model(year="2024", name="January")
        # Create method to get actual month if not exist or next months if actual exist or can't create new month
        # Create method to get actual year
        month = self.month_repository(self.db, self.month_model).create(new_month)
        return month