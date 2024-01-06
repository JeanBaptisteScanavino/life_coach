class UpdateSkill:
    def __init__(self, dependencies):
        self.skill_repository = dependencies["skill_repository"]
        self.db = dependencies["db"]
        self.skill_model = dependencies["skill_model"]

    def execute(self, id, skill):
        skill = self.skill_repository(self.db, self.skill_model).update(id, skill)
        return skill
