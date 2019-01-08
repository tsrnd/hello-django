class Usecase():
    def __init__(self, repository):
        self.repository = repository

    def get_all_category(self):
        return self.repository.get_all_category()

    def create(self, name):
        return self.repository.create(name)
