import os
import random
import string


myseed = ""
video_name = ""
audio_name = ""
post_name = ""


def download_video(link):
    global myseed
    global video_name
    global audio_name
    global post_name
    myseed = "".join(random.choice(string.ascii_lowercase) for _ in range(7))
    video_name = f"videos/my_video_{myseed}.mp4"
    audio_name = f"videos/my_audio_{myseed}.mp4"
    post_name = f"videos/my_post_{myseed}.mp4"
    cmd = 'ffmpeg -i "' + link + \
        f'" -c:v libx264 -preset fast -crf 22 "{video_name}"'
    os.system(cmd)


def transform(str):

    ind1 = ind2 = 0
    for i in range(len(str)):
        if str[i] == "_":
            ind1 = i
            break
    for i in range(len(str) - 1, -1, -1):
        if str[i] == ".":
            ind2 = i
            break
    str = str[: ind1 + 1] + "audio" + str[ind2:]
    return str


def download_audio(link):
    global audio_name
    try:
        cmd = (
            'ffmpeg -i "'
            + transform(link)
            + f'" -c:v libx264 -preset fast -crf 22 "{audio_name}"'
        )
        os.system(cmd)
    except:
        print("No audio retrieved")


def merge_video_n_audio():
    global video_name
    global audio_name
    global post_name
    if os.path.exists(video_name) and os.path.exists(audio_name):
        cmd = f'ffmpeg -i "{video_name}" -i "{audio_name}" -c copy "{post_name}"'
        os.system(cmd)
    else:
        if os.path.exists(video_name):
            os.rename(video_name, post_name)


def build_post(link):
    download_video(link)
    download_audio(link)
    merge_video_n_audio()
    if os.path.exists(video_name):
        os.remove(video_name)
    if os.path.exists(audio_name):
        os.remove(audio_name)
