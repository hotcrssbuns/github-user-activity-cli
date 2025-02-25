from urllib import request, error
import json
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def fetch_json(link):
    try:
        resp = request.urlopen(link)
        data = resp.read()
        string_data = data.decode("UTF-8")
        json_data = json.loads(string_data)
        return json_data
    except error.HTTPError as e:
        print(f"HTTP Error occured")


def main():
    username = input("github-activity ")
    link = f"https://api.github.com/users/{username}/events"
    formatted_json = fetch_json(link)
    clear()
    print("Output:")

    for value in formatted_json:
        event_type = value["type"]
        repo_name = value["repo"]["name"]

        if event_type == "PublicEvent":
            print(f"- Changed repository from private to public {repo_name}")
        if event_type == "WatchEvent":
            print(f"- Starred repository {repo_name}")
        if event_type == "PushEvent":
            print(f"- Pushed commit to {repo_name}")


main()
