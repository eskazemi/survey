from mongoengine import *


class Items(EmbeddedDocument):
    TYPE_CHOICES = (
        ("stepper", 0),
        ("group", 1),
        ("checkbox", 2),
        ("switch", 3),
        ("text", 4),
        ("rate", 5),
        ("mobile", 6),
    )
    type = StringField(choices=TYPE_CHOICES, required=True)
    title = StringField(required=True, max_length=250)
    body = StringField(required=True, max_length=350)
    position = IntField(default=0)
    required = BooleanField(required=False)
    score = IntField(max_value=5, min_value=0)
    children = ListField(EmbeddedDocumentField('Items'))

