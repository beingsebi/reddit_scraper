import reddit
import database as db
import util
import scrape
import build_post

ls = reddit.getposts()
util.print_params(len(ls))
post = db.get_final_post(ls)

if post is None:
    print("Did not find any video to post")
else:
    count = 10
    downloaded = 0
    while count > 0:
        try:
            link = util.get_json_link(post)
            link = scrape.get_link(link)
            print(link)
            build_post.build_post(link)
            # further use of the video
            db.insert_post(post, 1)
            count = 0
            downloaded = 1
        except Exception as e:
            print(e)
            db.insert_post(post, 0)
            count -= 1

    if downloaded:
        print("Video downloaded successfully")
    else:
        print("Wasn't able to download any video")
