from urllib import request, error
import json
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def is_json_empty(json):
    return len(json) == 0


def fetch_json(link):
    try:
        resp = request.urlopen(link)
        data = resp.read()
        string_data = data.decode("UTF-8")
        json_data = json.loads(string_data)
        return json_data
    except error.HTTPError as e:
        print(f"Error occured: {e}")


def main():
    while True:
        username = input("github-activity ")
        link = f"https://api.github.com/users/{username}/events"
        events = {}
        formatted_json = fetch_json(link)
        if is_json_empty(formatted_json):
            print("Error: Not a legitimate account. Try another")
        else:
            break
    clear()
    print("Output:")

    # Go through JSON file and update dictionary with number of times an event shows up
    try:
        for value in formatted_json:
            event_type = value["type"]
            repo_name = value["repo"]["name"]
            action = value.get("payload", {}).get("action")

            if f"{event_type}_{repo_name}" in events.keys():
                events[f"{event_type}_{repo_name}"] += 1
            else:
                events.update({f"{event_type}_{repo_name}": 1})
    except TypeError as e:
        print(f"Error: {e}")

    for key, value in events.items():
        event_type, repo_name = key.split("_")
        if event_type == "PublicEvent":
            print(f"- Changed repository from private to public {repo_name}")
        if event_type == "WatchEvent":
            print(f"- Starred repository {repo_name}")
        if event_type == "PushEvent":
            if value > 1:
                print(f"- Pushed commit {value} times to {repo_name}")
            else:
                print(f"- Pushed commit 1 time to {repo_name}")
        if event_type == "CommitCommentEvent":
            print(f"- Created commit comment on {repo_name}")
        if event_type == "CreateEvent":
            print(f"- Created git branch for {repo_name}")
        if event_type == "DeleteEvent":
            print(f"- Deleted git branch for {repo_name}")
        if event_type == "ForkEvent":
            print(f"- Forked {repo_name}")
        if event_type == "GollumEvent":
            print(f"- Created/Updated wiki page for {repo_name}")
        if event_type == "IssueCommentEvent":
            print(f"- Created Pull Request comment for {repo_name}")
        if event_type == "IssuesEvent":
            print(f"- {action} issue for {repo_name}")
        if event_type == "MemberEvent":
            print(f"- {action} user for {repo_name}")
        if event_type == "PullRequestEvent":
            print(f"- {action} Pull Request for {repo_name}")
        if event_type == "PullRequestReviewEvent":
            print(f"- {action} Pull Request Review for {repo_name}")
        if event_type == "PullRequestReviewCommentEvent":
            print(f"- {action} Pull Request Review Comment for {repo_name}")
        if event_type == "PullRequestReviewThreadEvent":
            print(f"- {action} Comment Thread for {repo_name}")
        if event_type == "ReleaseEvent":
            print(f"- {action} release event for {repo_name}")
        if event_type == "SponsorshipEvent":
            print(f"- {action} Sponsorship Listing for {repo_name}")


main()
