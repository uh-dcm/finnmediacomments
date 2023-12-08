import requests
import json

def collect( id ):
    url = f"https://www.hs.fi/api/commenting/hs/articles/{id}/comments"
    
    data = requests.get( url )
    data = data.json()

    return data['comments']

def to_4cat_csv( comments , output ):
    df = pd.DataFrame( comments ).flatten()

    newdf = pd.DataFrame()
    newdf['body'] = df['comment']
    newdf['author'] = df['userIdentity'].apply( lambda userIdentity: userIdentity['displayName'] )
    newdf['timestamp'] = df['createdAt'].apply(  lambda date: datetime.fromtimestamp(  date/1000 ).strftime("%Y-%m-%d %H:%M:%S") )
    newdf['id'] = df['id']
    newdf['thread'] = df['articleId']

    newdf.to_csv( output )

if __name__ == '__main__':
    collect( 2000010042389 )