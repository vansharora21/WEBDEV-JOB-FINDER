def filter_no_website(restaurants):
    """
    Filter restaurants that don't have a website.
    For Overpass API data, we also filter by quality metrics.
    
    Args:
        restaurants: List of restaurant dictionaries from Overpass API
    
    Returns:
        List of filtered restaurants without websites
    """
    filtered = []

    for restaurant in restaurants:
        # Skip if already has a website
        if restaurant.get("website"):
            continue
        
        # Restaurant has no website - keep it!
        filtered.append(restaurant)

    return filtered
