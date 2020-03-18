#!/usr/bin/env python3 

from slack_webhook import Slack
import os

hook=os.getenv("SLACK_WEBHOOK")
text=os.getenv("SLACK_TEXT")

slack = Slack(url=hook)

slack.post(text=text)
