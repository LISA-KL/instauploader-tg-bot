from instagrapi import Client

api = Client()
# api.login("suzume.says", "password")


# api.dump_settings('insta.coo')

api.load_settings("insta.cookie")


def get_media_info(url):

    mpk = api.media_pk_from_url("https://www.instagram.com/reel/C1RgkuYrocp/?utm_source=ig_web_copy_link")

    # print(mpk)

    minfo = api.media_info(mpk)
    return minfo.video_url, minfo.caption_text, minfo.user.username

    # print(minfo.video_url)
    # print(minfo.caption_text)