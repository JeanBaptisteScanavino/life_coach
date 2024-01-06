class WaitingListRepository:
    def __init__(self, db, model):
        self.db = db
        self.model = model

    def get_all(self):
        return self.db.query(self.model).all()

    # def get_one(self, id):
    #     return self.db.query(self.model).get(id)

    def create(self, object):
        waiting_list = self.model(value=object.value, category_id=object.category_id)
        self.db.add(waiting_list)
        self.db.commit()
        self.db.refresh(waiting_list)
        return waiting_list

    def delete(self, id: int):
        # Create exeption : try find element then delete?
        try:
            self.db.query(self.model).filter(self.model.id == id).delete(synchronize_session=False)
            self.db.commit()
        except Exception:
            return Exception

    # def update(self, id, object):
    #     new_category = self.model(title=object.title, active=object.active)
    #     self.db.query(self.model).filter(self.model.id == id).update(
    #         {"title": new_category.title, "active": new_category.active},
    #         synchronize_session=False,
    #     )
    #     self.db.commit()
    #     return self.get_one(id)
