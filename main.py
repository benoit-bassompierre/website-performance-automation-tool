from PageSpeed_functions import get_pagespeed_scores


api_key = "insert api key"
url = "insert URL"


scores = get_pagespeed_scores(url, api_key)

if scores:
    print("Scores:", scores)


