class ProductSerializer:
    @staticmethod
    def serialize(product):
        return {
            'id': product.id,
            'name': product.name,
            "image_url": product.im_url,
        }

    @staticmethod
    def serializes(products):
        result = []
        for product in products:
            result.append({
                'id': product.id,
                'name': product.name,
            })
        return result
