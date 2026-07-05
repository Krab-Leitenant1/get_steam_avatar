import requests
key = input("Enter your API Key: ")
id = int(input("Enter your following ID: "))
r = requests.get(url=f'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={key}&steamids={id}')
if r.status_code == 200:
    avat =requests.get(r.json()['response']['players'][0]['avatarfull'])
    if avat.status_code == 200:
        with open('avatar.png', 'wb') as f:
            f.write(avat.content)
            print('File saved as avatar.png')
    else:
        print('Error Code: ' + str(r.status_code))
else:
    print('Cahnge API Key or SteamID')