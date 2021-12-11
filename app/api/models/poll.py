from mongoengine import *
from datetime import datetime
from mongoengine import signals
from app.api.models import Container


class Poll(Document):
    """
    create pollItem
    """
    container_id = StringField(required=True)
    container_type = IntField(required=True)
    mobile = StringField()
    unit = StringField()
    score = IntField(default=0)
    data = DynamicField(required=True)
    created_at = DateTimeField(default=datetime.now)

    def _extraction_score(self):
        """
        Extract scores from data in the data field and add scores to score field in pollItem
        """
        if isinstance(self.data, dict):
            for k in self.data.keys():
                if k == 'score':
                    self.score += self.data[k]
        elif isinstance(self.data, list):
            for num in range(len(self.data)):
                x = self.data[num]
                for k in x.keys():
                    if k == 'score':
                        self.score += x[k]

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        """
        calculation total_polls and average_score fields a container
        """
        container = Container.objects.get(id=document.poll_id)
        total_polls = container.total_polls + 1
        if container['average_score'] == 0:
            container.average_score = document.score
            container.total_polls = total_polls
            container.save()
        else:
            old_average = container.average_score
            new_average = ((old_average * (total_polls - 1)) + document.score) / total_polls
            container.average_score = new_average
            container.total_polls = total_polls
            container.save()

    def save(self, *args, **kwargs):
        self._extraction_score()
        return super(Poll, self).save(*args, **kwargs)


signals.post_save.connect(Poll.post_save, sender=Poll)




