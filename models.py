import mongoengine as me


class Book(me.Document):
    name = me.StringField(required=True)
    author = me.StringField(required=True)
    publishing_house = me.StringField(required=True)
    year = me.IntField(required=True)
    # example isbn 978-5-4461-0846-6
    isbn = me.StringField()
    # example bbk 32.973 / 84P7 / 84(2Рус+Рус)6-44
    bbk = me.StringField()
    meta = {
        'collection': 'book',
    }