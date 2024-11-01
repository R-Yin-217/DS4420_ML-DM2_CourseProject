import requests
import pandas as pd

client_id = 'a7KEQKNiEocEUvfGV6ViKA'
secret = 'El6eYl7_04TO66AgvAu75sjpg5Ef4g'
names = [
    "UpperWestSide", "Harlem", "EastVillage", "Greenpoint", "Bushwick", "Williamsburg", 
    "BedStuy", "ChelseaNYC", "LongIslandCity", 
    "SunnysideQueens", "Soho", "Flushing", "FinancialDistrict", "Hellskitchen", "DUMBO", 
    "ParkSlope", "FortGreene", "RedHookBK", "CobbleHill", "CrownHeights", "EastHarlem", 
    "DowntownBrooklyn", "WashingtonHeights", "Inwood", "Flatbush", "ProspectHeights", "Tribeca", 
    "Gramercy", "BatteryParkCity", "ChinatownNYC", "KipsBay", "GreenwichVillage", "LenoxHill",
    "LowerEastSide", "EastFlatbush", "Bensonhurst", "SheepsheadBay", "DykerHeights",
    "DitmasPark", "Gowanus", "CarrollGardens", "BayRidge", "SunsetPark", "ForestHills", 
    "RegoPark", "JacksonHeights", "CoronaNY", "RockawayBeach", "Woodside", "Ridgewood", 
    "JamaicaNYC", "Astoria", "Woodhaven", "MiddleVillage", "BrooklynHeights", 'FarRockaway', "EastVillage"
]

# URL of the API
base_url = 'https://oauth.reddit.com/r/'
params = {'limit': 1000}
auth = requests.auth.HTTPBasicAuth(client_id, secret)

data = {
    'grant_type': 'password',
    'username': 'Intelligent_Willow95',
    'password': 'Masa3na3Masa3na3!'
}

# Get the token
headers = {'User-Agent': 'MyRedditApp/0.0.1'}
res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
TOKEN = res.json()['access_token']

# Add token to headers
headers['Authorization'] = f'bearer {TOKEN}'

# Initialize an empty DataFrame
df = pd.DataFrame()

# Loop through each subreddit name
for n in names:
    url = base_url + n + "/new"  # Create the full URL for each subreddit
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()['data']['children']
        data = [d for d in data if d['data'].get('selftext', '').strip()]

        print(f"Fetching data from: {url}")
        
        for d in data:
            text = d['data'].get('selftext', '')
            upvote_ratio =d['data'].get('upvote_ratio', "")  # Use .get() to handle missing data gracefully
            temp = pd.DataFrame({'neighborhood': [n], 'upvote_ratio': [upvote_ratio], 'text': [text]})
            
            df = pd.concat([df, temp], ignore_index=True)
    else:
        print(f"Failed to fetch data for {n}: {response.status_code}")
        print(response.json())  # This will give more info about the error if something goes wrong

# Save to CSV
csv_file_path = "/Users/mackmorgan/Desktop/reddit_data.csv"
df.to_csv(csv_file_path, index=False)

# url = base_url + "DUMBO/new"
# response = requests.get(url, headers=headers, params=params)
# data = response.json()['data']['children']
# filtered_data = [d for d in data if d['data'].get('selftext', '').strip()]
# print(filtered_data)