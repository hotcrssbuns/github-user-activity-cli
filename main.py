from urllib import request
import json

username = input("github-activity ")

link = f"https://api.github.com/users/{username}/events"

resp = request.urlopen(link)

data = resp.read()

string_data = data.decode("UTF-8")

json_data = json.loads(string_data)

formatted_json = json.dumps(json_data, indent=2)

print(formatted_json)
