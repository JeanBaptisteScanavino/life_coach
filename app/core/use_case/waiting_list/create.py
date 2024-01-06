class CreateWaitingList:
    def __init__(self, dependencies):
        self.waiting_list_repository = dependencies["waiting_list_repository"]
        self.db = dependencies["db"]
        self.waiting_list_model = dependencies["waiting_list_model"]

    def execute(self, waiting_list):
        waiting_list = self.waiting_list_repository(self.db, self.waiting_list_model).create(waiting_list)
        return waiting_list