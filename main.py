from urllib import request, error
import json


def fetch_json(link):
    try:
        resp = request.urlopen(link)
        data = resp.read()
        string_data = data.decode("UTF-8")
        json_data = json.loads(string_data)
        return json.dumps(json_data, indent=2)
    except error.HTTPError as e:
        print(f"HTTP Error occured")


def main():
    username = input("github-activity ")
    link = f"https://api.github.com/users/{username}/events"
    formatted_json = fetch_json(link)

    print(formatted_json)


main()
