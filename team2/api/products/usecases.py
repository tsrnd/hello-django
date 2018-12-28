class ProductUsecase:
    
    def __init__(self, product_repository):
        self.repo = product_repository
    
    def get_products(self):
        return self.repo.get_products()

    def get_product(self, _id):
        product = self.repo.get_product(_id)
        if product is None:
            return None, 404
        return product, 200
