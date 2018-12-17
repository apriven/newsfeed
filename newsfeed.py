from bottle import route, run, template, static_file
import feedparser
import ssl
import json

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context
feed = feedparser.parse("http://feeds.feedburner.com/movieweb_news")

news = []
for i in feed.entries:
    news.append({"title": i.title, "link": i.link})


@route('/')
def index():
    return template("newsfeed.html", root='')


@route('/CSS/<filename:re:.*\.css>')
def css(filename):
    return static_file(filename, root='CSS')


@route('/pics/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='pics')


@route('/getall')
def getall():
    return json.dumps(news)


def main():
    run(host='localhost', port=7002)


if __name__ == "__main__":
    main()


# print(news[0]["title"])
