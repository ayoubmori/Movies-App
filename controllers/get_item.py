from api.endpoints.fetch_item import fetch_item
from services.extract_item_infos import extract_item_info
from services.const import FIND_MOVIE

def get_item(request_end = FIND_MOVIE,id=1):
    results = fetch_item(request_end,id=id)
    if results:
        item_info = extract_item_info(results)
        return item_info
    return None
    