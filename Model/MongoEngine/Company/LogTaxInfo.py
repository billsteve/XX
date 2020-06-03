from mongoengine import *


class TaxInfo(Document):
    web_key = StringField(required=True, max_length=50)
    tax = IntField()

    @staticmethod
    def getByWebKey(web_key):
        return TaxInfo.objects(web_key=web_key)

    @staticmethod
    def saveToMongo(item):
        data = TaxInfo(web_key=item.web_key, tax=1)
        res = data.save()
        print(res)
