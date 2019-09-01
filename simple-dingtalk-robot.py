#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: python 2.7.13
# @author: keria(runchen.brc@alibaba-inc.com)
# @date: 2019/08/19
import json
import urllib2

# 钉钉自定义机器人，文档地址：https://open-doc.dingtalk.com/microapp/serverapi2/qf2nxq
DINGTALK_ROBOT_SEND_MESSAGE_API = 'https://oapi.dingtalk.com/robot/send?access_token='

# 机器人token
DINGTALK_ACCESS_TOKEN = '******'

# 需要发送的钉钉消息内容
DINGTALK_MESSAGE_CONTENT = '******'


# 发送钉钉消息通知
def send_message_to_dingtalk(response_url, content):
    header = {
        "Content-Type": "application/json ;charset=utf-8 "
    }

    json_string = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "at": {
            "atMobiles": None,
            "isAtAll": 1
        }
    }

    json_message = json.dumps(json_string)

    post_request = urllib2.Request(url=response_url, data=json_message, headers=header)
    urllib2.urlopen(post_request)


def main():
    # 发送钉钉消息通知
    response_url = DINGTALK_ROBOT_SEND_MESSAGE_API + DINGTALK_ACCESS_TOKEN
    send_message_to_dingtalk(response_url, DINGTALK_MESSAGE_CONTENT)


if __name__ == '__main__':
    main()
