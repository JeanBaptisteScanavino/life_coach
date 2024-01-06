class GetAllWaitingList:
    def __init__(self, dependencies):
        self.waiting_list_repository = dependencies["waiting_list_repository"]
        self.db = dependencies["db"]
        self.waiting_list_model = dependencies["waiting_list_model"]

    def execute(self):
        categories = self.waiting_list_repository(self.db, self.waiting_list_model).get_all()
        return categories
