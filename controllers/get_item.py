from api.endpoints.fetch_item import fetch_item, fetch_item_images
from utils.extract_item_infos import extract_item_info , extract_item_images

def get_item(request_end: str, id):
    results = fetch_item(request_end, id=id)
    if results:
        item_info = extract_item_info(results)
        return item_info
    return None


def get_item_images(request_end: str, id):
    results = fetch_item_images(request_end, id=id)
    if results:
        item_images = extract_item_images(results)
        return item_images
    return None