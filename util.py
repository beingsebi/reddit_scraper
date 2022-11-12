import _params as params


def print_params(sz):
    print("retrieved " + str(sz) + " posts from " + params.subreddits)
    print("time_filter = " + params.time_filter)
    print("posts_checked = " + str(params.posts_checked))
    print("min_upvotes = " + str(params.min_upvotes))
    print("min_ratio = " + str(params.min_ratio))


def get_json_link(post):
    link = "https://www.reddit.com" + post.permalink + ".json"
    return link
