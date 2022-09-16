import requests
import Ascii_Art_Maker

headers = {
    'User-Agent': 'My User Agent 1.0',
}
url_input = input("What Subreddit would you like to visit?\nr/")
response = requests.get(
    f"https://www.reddit.com/r/{url_input}/.json", headers=headers
)
response_data = response.json()
subreddit_content = response_data["data"]["children"]

for i, entry in enumerate(subreddit_content):
    post_data = entry["data"]

    if post_data.get("post_hint") == "image":
        is_image = True
        address = post_data["url_overridden_by_dest"]
    else:
        is_image = False

    print(post_data["title"])
    print("")
    if is_image:
        Ascii_Art_Maker.main(address)
        with open('ascii_image.txt', 'r') as image:
             print(image.read())
