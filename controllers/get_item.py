from api.endpoints.fetch_item import fetch_item
from utils.extract_item_infos import extract_item_info
from api.endpoints.config import FIND_MOVIE


def get_item(request_end: str, id):
    results = fetch_item(request_end, id=id)
    if results:
        item_info = extract_item_info(results)
        return item_info
    return None
