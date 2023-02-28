import json
from pytube import YouTube


def lambda_handler(event, context):
    # TODO implement
    youtube_url=event['queryStringParameters']['youtube_url']
    caption_xml_content = youtube_caption.get_caption_str(youtube_url)
    return {
        'statusCode': 200,
        'body': caption_xml_content
    }
def get_caption_str(youtube_url):
    # 创建视频对象
    src = YouTube(youtube_url)
    # 检查是否有字幕可用
    if list(src.captions).__len__() <= 0:
        return "not found captions"
    caption = list(src.captions)[0]

    return caption.xml_captions
