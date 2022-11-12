import _params as pm
import _login_data as lg
import praw


def getposts():
    reddit = praw.Reddit(
        client_id=lg.client_id,
        client_secret=lg.client_secret,
        user_agent=lg.user_agent,
        username=lg.username,
        password=lg.password,
    )
    sub = reddit.subreddit(pm.subreddits)
    slist = []
    for i in sub.top(time_filter=pm.time_filter, limit=pm.posts_checked):
        if (
            not i.over_18
            and not i.locked
            and not i.stickied
            and i.score > pm.min_upvotes
            and i.upvote_ratio > pm.min_ratio
            and (
                (isinstance(i.link_flair_text, str)
                 and "video" in i.link_flair_text)
                or (hasattr(i, "post_hint") and "video" in i.post_hint)
            )
            and "v.redd.it" in i.url
        ):
            slist.append(i)

    slist.sort(key=lambda x: (x.upvote_ratio, x.score), reverse=True)
    return slist


# g = open("text.txt", "w", encoding="utf-8")
# for i in slist:
#    g.write(i.url + "\n")
