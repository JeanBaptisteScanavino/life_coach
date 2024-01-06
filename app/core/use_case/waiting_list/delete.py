class DeleteWaitingList:
    def __init__(self, dependencies):
        self.waiting_list_repository = dependencies["waiting_list_repository"]
        self.db = dependencies["db"]
        self.waiting_list_model = dependencies["waiting_list_model"]

    def execute(self, id):
        try:
            self.waiting_list_repository(self.db, self.waiting_list_model).delete(id)
            return 'OK'
        except Exception:
            return Exception
