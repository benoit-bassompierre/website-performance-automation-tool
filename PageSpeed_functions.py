import requests

def get_category_score(url, api_key, strategy, category):
    """
    Function that makes a request to the PageSpeed Insights API for a specific category (performance, accessiblity, best-practices or SEO) and strategy (mobile or desktop)
    """
    api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&strategy={strategy}&key={api_key}&category={category}"
    
    response = requests.get(api_url)
    
    # If the request is successful
    if response.status_code == 200:
        data = response.json()
        lighthouse_scores = data.get('lighthouseResult', {}).get('categories', {})
        
        # extract the score of the category
        if category in lighthouse_scores:
            return int(lighthouse_scores[category]['score'] * 100)
        else:
            print(f"Warning: {category} score not found for {strategy}. Adding 0 as default.")
            return 0
    else:
        print(f"Error fetching data for {category} on {strategy}: {response.status_code}")
        return 0

def get_pagespeed_scores(url, api_key):
    """
    function that calls ‘get_category_score()’ for each category and for mobile then desktop and places the results in a list
    """

    strategies = ["mobile", "desktop"]
    categories = {
        "performance": "performance",
        "accessibility": "accessibility",
        "best-practices": "best-practices",
        "seo": "seo"
    }
    
    scores = []

    for strategy in strategies:
        for category_key, category_value in categories.items():
            score = get_category_score(url, api_key, strategy, category_value)
            scores.append(score)
    
    return scores