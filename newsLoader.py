import urllib as URL
import json
import imageLoader

def loadFeeds():
    URL_NAME="https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Ffeeds.feedburner.com%2Fd0od"
    site = URL.urlopen(URL_NAME)
    data = site.read()
    feeds = []
    print "loading feeds ...."
    json_data = json.loads(data)
    count = 3
    for item in json_data['items']:
        feeds.append(item['title'])
        imageLoader.loadImage(item['description'].split('src="')[1].split("\"")[0],'images/temp_img/feed_'+str(count)+'.jpg')
        count -= 1
        if count <= 0:
            break
    print "feeds loaded!!"
    return feeds

