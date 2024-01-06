class DeleteSkill:
    def __init__(self, dependencies):
        self.skill_repository = dependencies["skill_repository"]
        self.db = dependencies["db"]
        self.skill_model = dependencies["skill_model"]

    def execute(self, id):
        try:
            self.skill_repository(self.db, self.skill_model).delete(id)
            return 'OK'
        except Exception:
            return Exception
