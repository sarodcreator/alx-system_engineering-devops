import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}  # Set a User-Agent header to avoid 429 Too Many Requests error
    
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract the number of subscribers
        subscribers = data['data']['subscribers']
        
        return subscribers
    else:
        # If subreddit not found or other issue, return 0
        return 0

