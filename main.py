import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter
from PIL import ImageEnhance
import os
import json

import quoteLoader
import imageLoader
import newsLoader

#Loading configs from file
CONFIG = {}
with open('./config.json') as f:
    CONFIG = json.load(f)
THEME = CONFIG["image"]["theme"]
RESOLUTION = CONFIG["image"]["resolution"]
CARD_COLOR = (CONFIG["card"]["color"][0],CONFIG["card"]["color"][1],CONFIG["card"]["color"][2],CONFIG["card"]["color"][3])
FONT_TYPE = CONFIG["font"]["fontLocation"]
FONT_SIZE = CONFIG["font"]["fontSize"]
FONT_COLOR = (CONFIG["card"]["fontColor"][0],CONFIG["card"]["fontColor"][1],CONFIG["card"]["fontColor"][2])
FONT_SIZE_FEEDS = CONFIG["font"]["fontSizeFeeds"]
BOX_SIZE = (CONFIG["card"]["quoteBoxSize"]["left"],
            CONFIG["card"]["quoteBoxSize"]["top"],
            CONFIG["card"]["quoteBoxSize"]["right"],
            CONFIG["card"]["quoteBoxSize"]["bottom"])
NEWS_BOX_SIZE = (CONFIG["card"]["feedBoxSize"]["left"],
                    CONFIG["card"]["feedBoxSize"]["top"],
                    CONFIG["card"]["feedBoxSize"]["right"],
                    CONFIG["card"]["feedBoxSize"]["bottom"])
MARGIN = 20
QUOTE_START_CORDINATE = (CONFIG["card"]["quoteBoxSize"]["left"]+MARGIN,
                    CONFIG["card"]["quoteBoxSize"]["top"]+MARGIN)
IMAGE_URL = "https://source.unsplash.com/random/"+ RESOLUTION +"?"+ THEME
FONT_APPLE_GARAMOND = FONT_TYPE 
RESIZE_FACTOR_LOGO = 1
print IMAGE_URL
IMAGE_PATH = "images/wallie.jpeg"
# CONSTANT Declaration for usage -----END
imageText='''
The life is not Easy but it is 
not difficult either..
        
                    -  ABC Jones
'''

imageText,author = quoteLoader.loadQuote()

# # # Structuring START #########################
# DONE # 1. Quote Loader                        #
# DONE # 2. News Loader                         #
# DONE # 3. Image Loader                        #
# DONE # 4. Merger                              #
# TODO # 5. Constant and OOPS conversion        #
# TODO # 6. Merging with the GUI and service    #
# # # Structuring END ###########################

imageLoader.loadImage(IMAGE_URL,IMAGE_PATH)

img = Image.open("images/wallie.jpeg")
img = img.convert("RGBA")
font = ImageFont.truetype(FONT_TYPE , FONT_SIZE)

quote_logo_img = Image.open("images/quote-left.png")
quote_logo_img = quote_logo_img.resize((int(quote_logo_img.size[0]*RESIZE_FACTOR_LOGO),int(quote_logo_img.size[1]*RESIZE_FACTOR_LOGO)))
quote_logo_img = quote_logo_img.convert("RGBA")
quote_alpha = quote_logo_img.split()[3]

im = img.crop(BOX_SIZE)
im = im.filter(ImageFilter.BLUR)
im = im.filter(ImageFilter.BLUR)
im = im.filter(ImageFilter.BLUR)
im = im.filter(ImageFilter.BLUR)
im = im.filter(ImageFilter.BLUR)
im = im.convert("RGBA")
tmp = Image.new('RGBA', im.size, (0,0,0,0))
draw = ImageDraw.Draw(tmp)
draw.rectangle(((0, 0), im.size), fill=CARD_COLOR)
im = Image.alpha_composite(im, tmp)
draw = ImageDraw.Draw(im)
draw.text((100,25), imageText , FONT_COLOR, font=font)
draw.text((150,250),author,FONT_COLOR,font=font)
img.paste(im,BOX_SIZE)

'''Feeds Loading Stopped Currently
news_im = img.crop(NEWS_BOX_SIZE)
news_im = news_im.filter(ImageFilter.BLUR)
news_im = news_im.filter(ImageFilter.BLUR)
news_im = news_im.filter(ImageFilter.BLUR)
news_im = news_im.filter(ImageFilter.BLUR)
news_im = news_im.filter(ImageFilter.BLUR)
news_im = news_im.convert("RGBA")
tmp = Image.new('RGBA', news_im.size, (0,0,0,0))
draw = ImageDraw.Draw(tmp)
draw.rectangle(((0, 0), news_im.size), fill=(50,50,50,127))
news_im = Image.alpha_composite(news_im, tmp)
img.paste(news_im,NEWS_BOX_SIZE)

font = ImageFont.truetype(FONT_APPLE_GARAMOND , FONT_SIZE_FEEDS)
feeds = newsLoader.loadFeeds()
count = 1
feeds_count = len(feeds)
for feed in feeds:
    print feed    
    draw = ImageDraw.Draw(news_im)
    temp_im = Image.open('images/temp_img/feed_'+str(feeds_count - count + 1)+'.jpg')
    temp_im.thumbnail((128,128))    
    feed_line = ''
    word_count = 0
    char_count = 0
    for w in feed.split():
        word_count = word_count + 1
        char_count += len(w)
        if(word_count >= 4 or char_count >= 20):
            feed_line += "\n"
            word_count = 0
            char_count = 0  
        feed_line = feed_line+' '+w                
    draw.text((168,30+(110*(count-1))), feed_line , FONT_COLOR, font=font)        
    news_im.paste(temp_im,(30,30+(110*(count-1))))
    img.paste(news_im,NEWS_BOX_SIZE)
    count += 1
Feeds Loading Stopped Currently'''

img.paste(quote_logo_img,QUOTE_START_CORDINATE,mask=quote_alpha)
img.save("images/wallie_final.jpeg")

os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:$PWD/images/wallie_final.jpeg")
