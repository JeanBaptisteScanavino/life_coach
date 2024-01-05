class MonthRepository:
    def __init__(self, db, model):
        self.db = db
        self.model = model

    def get_all(self):
        return self.db.query(self.model).all()

    def get_one(self, id):
        return self.db.query(self.model).get(id)

    def create(self, object):
        month = self.model(year=object.year, name=object.name, active=True)
        self.db.add(month)
        self.db.commit()
        self.db.refresh(month)
        return month
