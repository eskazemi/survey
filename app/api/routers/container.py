from fastapi import (
    APIRouter,
    status,
    Body,
    HTTPException,
    Request
)
from app.api.models import Container
from app.api.schema.container import ContainerSchema, DeActivePoll
from .helper import *
from bson import ObjectId
from mongoengine.errors import DoesNotExist, ValidationError

router = APIRouter()


#####################
# #######get########
#####################
@router.get('', status_code=status.HTTP_200_OK)
def get_all_container(re: Request):
    container_list = []
    containers = (Container.objects.all())
    for obj in containers:
        container_list.append(container_helper((obj.to_mongo().to_dict())))
    return container_list


@router.get('/{container_id}')
def get_container(poll_id: str):
    try:
        info = (Container.objects.get(id=ObjectId(poll_id))).to_mongo().to_dict()
        # converting query result into valid python dict
        return container_helper(info)
    except DoesNotExist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


#####################
# #######create########
#####################


@router.post('/')
def create_container(new_container: ContainerSchema):
    obj = Container(**new_container.dict())
    obj.save()
    return {"message": "success", "status": status.HTTP_200_OK}


#####################
# #######update########
#####################

@router.patch('/{container_id}')
def deative_Container(container_id: str, item: DeActivePoll = Body(...)):
    try:
        obj = Container.objects.get(id=container_id)
        new_info = item.is_active
        obj.update(is_active=new_info)
        obj.save()
        return {"true"}
    except DoesNotExist:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    except ValidationError:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.put('/update/{container_id}')
def update_container(container_id: str, item: ContainerSchema = Body(...)):
    try:
        obj = Container.objects.get(id=container_id)
        items = item.dict()
        obj.update(**items)
        return {"message": "updated successfully", "status": status.HTTP_200_OK}
    except DoesNotExist:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    except ValidationError:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
