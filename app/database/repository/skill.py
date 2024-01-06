class SkillRepository:
    def __init__(self, db, model):
        self.db = db
        self.model = model

    def get_all(self):
        print("ARG", self.model)
        return self.db.query(self.model).all()

    def get_one(self, id):
        return self.db.query(self.model).get(id)

    def create(self, object):
        print("ZOUUUV")
        skill = self.model(value=object.value, category_id=object.category_id, month_id=object.month_id, status="TODO")
        self.db.add(skill)
        self.db.commit()
        self.db.refresh(skill)
        return skill

    def delete(self, id: int):
        # Create exeption : try find element then delete?
        try:
            self.db.query(self.model).filter(self.model.id == id).delete(synchronize_session=False)
            self.db.commit()
        except Exception:
            return Exception

    def update(self, id, object):
        newskill = self.model(value=object.value, category_id=object.category_id, month_id=object.month_id, status=object.status)
        self.db.query(self.model).filter(self.model.id == id).update(
            {"value": newskill.value, "category_id": newskill.category_id, "month_id": newskill.month_id, "status": newskill.status},
            synchronize_session=False,
        )
        self.db.commit()
        return self.get_one(id)
