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
    events = {}
    formatted_json = fetch_json(link)
    clear()
    print("Output:")

    # Go through JSON file and update dictionary with number of times an event shows up
    for value in formatted_json:
        event_type = value["type"]
        repo_name = value["repo"]["name"]
        if f"{event_type}_{repo_name}" in events.keys():
            events[f"{event_type}_{repo_name}"] += 1
        else:
            events.update({f"{event_type}_{repo_name}": 1})

        # if event_type == "PublicEvent":
        # print(f"- Changed repository from private to public {repo_name}")
        # if event_type == "WatchEvent":
        # print(f"- Starred repository {repo_name}")
        # if event_type == "PushEvent":
        # print(f"- Pushed commit to {repo_name}")

    for key in events.keys():
        print(key)


main()
