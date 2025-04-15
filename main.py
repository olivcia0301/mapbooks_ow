users:list=[
    {"name":"Oliwia","location": "Warszawa","posts": 267},
    {"name":"Julka","location": "Pogroszyn","posts": 767},
    {"name":"Kamil","location": "Kraków","posts": 578},
    {"name":"Filip","location": "Giżycko","posts": 274},
]




print(f"Witaj {users[0]["name"]}")

for user in users:
    print(f"Twój znajomy{users[0]["name"]} z {user["location"]} opublikował {user["posts"]} postów.")
