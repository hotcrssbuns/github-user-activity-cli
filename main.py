from urllib import request
import json


def fetch_json(link):
    resp = request.urlopen(link)
    data = resp.read()
    string_data = data.decode("UTF-8")
    json_data = json.loads(string_data)
    return json.dumps(json_data, indent=2)


username = input("github-activity ")

link = f"https://api.github.com/users/{username}/events"

formatted_json = fetch_json(link)

print(formatted_json)
