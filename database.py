import sqlite3
import scrape
import util


def create_table_dont_call_again_xadedasvadhassdasdabhaa2s123124559asdaasdfffzzz():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(
        """
    CREATE TABLE IF NOT EXISTS posts (
	id TEXT NOT NULL UNIQUE,
	author TEXT NOT NULL,
	created_utc TEXT NOT NULL,
	permalink TEXT NOT NULL,
	url TEXT NOT NULL,
   	upvote_ratio REAL NOT NULL,
    score INTEGER NOT NULL,
    subreddit TEXT

)
# "ALTER TABLE posts ADD COLUMN posted INTEGER"
    """
    )
    conn.commit()
    conn.close()


def check_if_exists(post):
    idstr = str(post.id)
    axls = []
    axls.append(idstr)
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT rowid FROM posts WHERE id = ?", axls)
    if len(c.fetchall()):
        conn.close()
        return True
    else:
        conn.close()
        return False


def insert_post(post, okay):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    p = (
        str(post.id),
        str(post.author),
        str(post.created_utc),
        str(post.permalink),
        str(post.url),
        float(post.upvote_ratio),
        int(post.score),
        str(post.subreddit),
        int(okay),
    )
    c.execute("INSERT INTO posts VALUES (?,?,?,?,?,?,?,?,?)", p)
    conn.commit()
    conn.close()


def print_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT *from posts")
    for t in c.fetchall():
        print(t)
    conn.commit()
    conn.close()


def get_final_post(ls):
    p = None
    for i in ls:
        if not check_if_exists(i):
            t = int(scrape.get_duration(util.get_json_link(i)))
            if t > 15 and t < 125:
                p = i
                break
    return p
