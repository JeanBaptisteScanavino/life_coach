class GetAllSkill:
    def __init__(self, dependencies):
        self.skill_repository = dependencies["skill_repository"]
        self.db = dependencies["db"]
        self.skill_model = dependencies["skill_model"]

    def execute(self):
        print("TEST",self.skill_model)
        skill = self.skill_repository(self.db, self.skill_model).get_all()
        return skill
