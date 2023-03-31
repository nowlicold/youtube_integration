import json
import pytube
from pytube import YouTube

def lambda_handler(event, context):
    # 如果action_type为空，则设置默认值
    action_type = event['body'].get('action_type', 'youtube_caption')

    # 获取请求中的youtube_url
    youtube_url = event['body'].get('youtube_url', '')

    if not youtube_url:
        return {
            'statusCode': 400,
            'body': 'Bad Request: Missing youtube_url parameter'
        }

    try:
        if action_type == "youtube_caption":
            caption_xml_content = get_caption_str(youtube_url)
            return {
                'statusCode': 200,
                'body': caption_xml_content
            }
        elif action_type == "youtube_real_url":
            youtube_real_url = get_youtube_real_url(youtube_url)
            return {
                'statusCode': 200,
                'body': {
                    'youtube_real_url' : youtube_real_url
                }
            }
        else:
            return {
                'statusCode': 400,
                'body': f'Bad Request: Invalid action_type {action_type}'
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Server Error: {str(e)}'
        }


def get_caption_str(youtube_url):
    # 创建视频对象
    src = YouTube(youtube_url)
    # 检查是否有字幕可用
    captions = src.captions
    if 'en' in captions:
        caption = captions['en']
    elif 'zh-Hans' in captions:
        caption = captions['zh-Hans']
    else:
        return "not found captions"
    return caption.xml_captions


def get_youtube_real_url(youtube_url):
    video = pytube.YouTube(youtube_url)
    best = video.streams.get_highest_resolution()

    return best.url

if __name__ == '__main__':
    event = json.loads('''
    {
    "body": {
        "youtube_url": "https://www.youtube.com/watch?v=sZDpJHl6amo",
        "action_type": "youtube_real_url"
    },
    "resource": "/{proxy+}",
    "path": "/path/to/resource",
    "httpMethod": "POST",
    "isBase64Encoded": true,
    "queryStringParameters": {
        "foo": "bar"
    },
    "multiValueQueryStringParameters": {
        "foo": [
            "bar"
        ]
    },
    "pathParameters": {
        "proxy": "/path/to/resource"
    },
    "stageVariables": {
        "baz": "qux"
    },
    "headers": {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "en-US,en;q=0.8",
        "Cache-Control": "max-age=0",
        "CloudFront-Forwarded-Proto": "https",
        "CloudFront-Is-Desktop-Viewer": "true",
        "CloudFront-Is-Mobile-Viewer": "false",
        "CloudFront-Is-SmartTV-Viewer": "false",
        "CloudFront-Is-Tablet-Viewer": "false",
        "CloudFront-Viewer-Country": "US",
        "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Custom User Agent String",
        "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
        "X-Amz-Cf-Id": "cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA==",
        "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
        "X-Forwarded-Port": "443",
        "X-Forwarded-Proto": "https"
    },
    "multiValueHeaders": {
        "Accept": [
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        ],
        "Accept-Encoding": [
            "gzip, deflate, sdch"
        ],
        "Accept-Language": [
            "en-US,en;q=0.8"
        ],
        "Cache-Control": [
            "max-age=0"
        ],
        "CloudFront-Forwarded-Proto": [
            "https"
        ],
        "CloudFront-Is-Desktop-Viewer": [
            "true"
        ],
        "CloudFront-Is-Mobile-Viewer": [
            "false"
        ],
        "CloudFront-Is-SmartTV-Viewer": [
            "false"
        ],
        "CloudFront-Is-Tablet-Viewer": [
            "false"
        ],
        "CloudFront-Viewer-Country": [
            "US"
        ],
        "Host": [
            "0123456789.execute-api.us-east-1.amazonaws.com"
        ],
        "Upgrade-Insecure-Requests": [
            "1"
        ],
        "User-Agent": [
            "Custom User Agent String"
        ],
        "Via": [
            "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)"
        ],
        "X-Amz-Cf-Id": [
            "cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA=="
        ],
        "X-Forwarded-For": [
            "127.0.0.1, 127.0.0.2"
        ],
        "X-Forwarded-Port": [
            "443"
        ],
        "X-Forwarded-Proto": [
            "https"
        ]
    },
    "requestContext": {
        "accountId": "123456789012",
        "resourceId": "123456",
        "stage": "prod",
        "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
        "requestTime": "09/Apr/2015:12:34:56 +0000",
        "requestTimeEpoch": 1428582896000,
        "identity": {
            "cognitoIdentityPoolId": null,
            "accountId": null,
            "cognitoIdentityId": null,
            "caller": null,
            "accessKey": null,
            "sourceIp": "127.0.0.1",
            "cognitoAuthenticationType": null,
            "cognitoAuthenticationProvider": null,
            "userArn": null,
            "userAgent": "Custom User Agent String",
            "user": null
        },
        "path": "/prod/path/to/resource",
        "resourcePath": "/{proxy+}",
        "httpMethod": "POST",
        "apiId": "1234567890",
        "protocol": "HTTP/1.1"
    }
}
    ''')

    # print(event['body']['query_str'])

    print(lambda_handler(event, None))
