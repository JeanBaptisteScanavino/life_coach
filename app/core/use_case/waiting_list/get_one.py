# class GetOneCategory:
#     def __init__(self, dependencies):
#         self.category_repository = dependencies["category_repository"]
#         self.db = dependencies["db"]
#         self.model = dependencies["category_model"]

#     def get_one_category(self, category_id):
#         category = self.category_repository(self.db, self.model).get_one(category_id)
#         return category
