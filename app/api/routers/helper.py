def container_helper(poll) -> dict:
    """
    :param poll: dict
    :return: dict
    """
    return {
        "id": str(poll['_id']),
        "title": poll.get('title'),
        "body": poll.get('body'),
        "slug": poll.get('slug'),
        "container_type": poll.get('container_type'),
        "items": poll.get('items'),
        "status": poll.get('status'),
        "is_active": poll.get('is_active'),
        "min_score": poll.get('min_score'),
        "time_slice_pattern": poll.get('time_slice_pattern'),
        "started_at": poll.get('started_at'),
        "created_at": poll.get('created_at'),
        "average_score": poll.get('average_score'),
        "total_polls": poll.get('total_polls'),
    }


def poll_helper(poll_item):
    """
    :param poll_item:
    :return: dict
    """
    return {
        "id": str(poll_item['_id']),
        "poll_id": poll_item.get("poll_id"),
        "poll_type": poll_item.get("poll_type"),
        "mobile": poll_item.get('mobile'),
        "stage": poll_item.get('stage'),
        "score": poll_item.get('score'),
        "data": poll_item.get('data'),
    }
