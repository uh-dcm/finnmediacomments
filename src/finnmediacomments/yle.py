import requests
import json

def collect( id ):
    app_key = 'sfYZJtStqjcANSKMpSN5VIaIUwwcBB6D'
    app_id = 'yle-comments-plugin'
    url = f"https://comments.api.yle.fi/v1/topics/{id}/comments/accepted?app_id={app_id}&app_key={app_key}&parent_limit=100"
    
    data = requests.get( url )
    data = data.json()

    return data

if __name__ == '__main__':
    print( len( collect( '74-20063567' ) ) )