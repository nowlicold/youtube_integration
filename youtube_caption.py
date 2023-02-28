from pytube import YouTube


def get_caption_str(youtube_url):
    # 创建视频对象
    src = YouTube(youtube_url)
    # 检查是否有字幕可用
    if list(src.captions).__len__() <= 0:
        return "not found captions"
    caption = list(src.captions)[0]

    return caption.xml_captions
