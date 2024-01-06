class CategoryRepository:
    def __init__(self, db, model):
        self.db = db
        self.model = model

    def get_all(self):
        return self.db.query(self.model).all()

    def get_one(self, id):
        return self.db.query(self.model).get(id)

    def create(self, object):
        category = self.model(title=object.title, active=True)
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category

    def update(self, id, object):
        new_category = self.model(title=object.title, active=object.active)
        self.db.query(self.model).filter(self.model.id == id).update(
            {"title": new_category.title, "active": new_category.active},
            synchronize_session=False,
        )
        self.db.commit()
        return self.get_one(id)
