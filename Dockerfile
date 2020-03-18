FROM python:3-slim

COPY . /src
WORKDIR /src

RUN pip install -r requirements.txt
ENV SLACK_WEBHOOK ""
ENV SLACK_TEXT ""

CMD /src/slack.py