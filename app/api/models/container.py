from mongoengine import *
from datetime import datetime
from .items import Items


class Container(Document):
    STATUS_CHOICES = (
        (1, "test1")
    )
    TYPE_CHOICES = (
        (1, "test1"),
        (2, "test2")
    )
    title = StringField(required=True, max_length=250)
    body = StringField(required=True, max_length=350)
    slug = StringField(required=True)
    status = IntField(choices=STATUS_CHOICES, required=False)
    is_active = BooleanField()
    container_type = IntField(required=True, choices=TYPE_CHOICES)
    items = ListField(EmbeddedDocumentField(Items))
    min_score = IntField(default=0)
    time_slice_pattern = StringField(required=False)
    started_at = DateTimeField(required=False)
    expired_at = DateTimeField(required=False)
    created_at = DateTimeField(default=datetime.utcnow())
    average_score = IntField(default=0)
    total_polls = IntField(default=0)
