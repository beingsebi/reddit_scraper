import requests


def get_link(link):
    text = requests.get(
        link, headers={"User-agent": "<console:undeniably_not_a_bot:1.0>"}
    ).json()
    text = text[0]["data"]["children"][0]["data"]["secure_media"]["reddit_video"][
        "fallback_url"
    ]
    return text


def get_duration(link):
    text = requests.get(
        link, headers={"User-agent": "<console:undeniably_not_a_bot:1.0>"}
    ).json()
    text = text[0]["data"]["children"][0]["data"]["secure_media"]["reddit_video"][
        "duration"
    ]
    return text
