from fastapi import (
    APIRouter,
    status,
    HTTPException,
    Body
)
from mongoengine import DoesNotExist
from app.api.routers.helper import poll_helper
from app.api.models.poll import Poll
from app.api.schema.poll import PollSchema

router = APIRouter()


#####################
# #######get########
#####################


@router.get('', status_code=status.HTTP_200_OK)
def get_all_poll():
    polls_list = []
    polls = Poll.objects.all()
    for poll in polls:
        polls_list.append(poll_helper(poll.to_mongo().to_dict()))
    return polls_list


#####################
# #######create########
#####################


@router.post('/', status_code=status.HTTP_200_OK)
def create_poll(new_poll: PollSchema):
    try:
        poll = Poll(**new_poll.dict())
        poll.save()
        return {"success"}
    except Exception as e:
        return f"error:{str(e)}"


#####################
# #######update########
#####################


@router.put('/{poll_id}')
def update_poll_item(poll_id: str, item: PollSchema = Body(...)):
    try:
        info = Poll.objects.get(id=poll_id)
        if info:
            items = item.dict()
            info.update(**items)
            return {"updated successfully"}

    except DoesNotExist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
