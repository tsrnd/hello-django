from myapp.category.models import Category


class Repository:
    def __init__(self, redis):
        self.redis = redis

    def get_all_category(self):
        result = []
        try:
            cates_db = Category.objects.all()
            for cate in cates_db:
                if self.redis.has_key("cat_" + str(cate.id)) == True:
                    self.redis.set("cat_" + str(cate.id), cate.name)
                result.append({
                    'id': cate.id,
                    'name': cate.name,
                })
        except Exception as err:
            return result, err

        return result, None

    def create(self, name):
        try:
            err = Category.objects.create(name=name)
        except Exception as err:
            return err
        return None
