import json
import youtube_caption

def lambda_handler(event, context):
    # TODO implement
    youtube_url=event['queryStringParameters']['youtube_url']
    caption_xml_content = youtube_caption.get_caption_str(youtube_url)
    return {
        'statusCode': 200,
        'body': caption_xml_content
    }
