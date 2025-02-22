from api.endpoints.fetch_items import fetch_items,fetch_recommendations_items
from utils.extract_items_infos import extract_items_list

def get_items(request_end: str, pages=1):
    """Fetch and combine items from multiple pages."""
    try:
        pages = int(pages)  # Ensure pages is an integer
    except ValueError:
        raise ValueError(f"Invalid page value: {pages}. It must be an integer.")

    items_list = []
    ## if you want to get items of multiple pages at the time
    # for page in range(1, pages + 1):
    #     results = fetch_items(request_end, page=page)
    #     if results:  # Ensure results are not None or empty
    #         items = extract_items_list(results,request_end)
    #         if items:
    #             items_list.extend(items)  # Append extracted items
    # return items_list

    ## if you want items of one selected page
    results = fetch_items(request_end, page=pages)
    if results:  # Ensure results are not None or empty
        items = extract_items_list(results,request_end)
        if items:
            items_list.extend(items)  # Append extracted items 
    return items_list

def get_recommendations_items(request_end: str,id=1, pages=1):
    """Fetch and combine items from multiple pages."""
    items_list = []
    results = fetch_recommendations_items(request_end,id, page=pages)
    if results:  # Ensure results are not None or empty
        items = extract_items_list(results,request_end)
        items_list.extend(items)  # Append extracted items
    return items_list
    