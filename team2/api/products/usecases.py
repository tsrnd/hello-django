class ProductUsecase:
    
    def __init__(self, product_repository):
        self.repo = product_repository
    
    def get_products(self):
        return self.repo.get_products()
