import requests
import json

def collect( id ):
    url = f"https://www.hs.fi/api/commenting/hs/articles/{id}/comments"
    
    data = requests.get( url )
    data = data.json()
    
    return data['comments']

if __name__ == '__main__':
    collect( 2000010042389 )