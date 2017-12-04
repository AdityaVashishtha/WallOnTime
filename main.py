import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter
from PIL import ImageEnhance

import quoteLoader
import imageLoader
import newsLoader

# CONSTANT Declaration for usage -----START
FONT_COLOR = (200,230,255)
FONT_SIZE = 25
FONT_SIZE_FEEDS = 20
FONT_APPLE_GARAMOND = "/usr/share/fonts/truetype/raleway-elementary/Raleway-Light.ttf"
BOX_SIZE = (1500,100,1900,400)
NEWS_BOX_SIZE = (1500,450,1900,1030)
RESIZE_FACTOR_LOGO = 1
IMAGE_URL = "https://source.unsplash.com/random/1920x1080"
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
# TODO # 4. Merger                              #
# TODO # 5. Constant Storage                    #
# # # Structuring END ###########################

imageLoader.loadImage(IMAGE_URL,IMAGE_PATH)

img = Image.open("images/wallie.jpeg")
img = img.convert("RGBA")
font = ImageFont.truetype(FONT_APPLE_GARAMOND , FONT_SIZE)

quote_logo_img = Image.open("images/quote-left.png")
quote_logo_img = quote_logo_img.resize((int(quote_logo_img.size[0]*RESIZE_FACTOR_LOGO),int(quote_logo_img.size[1]*RESIZE_FACTOR_LOGO)))
quote_logo_img = quote_logo_img.convert("RGBA")
quote_alpha = quote_logo_img.split()[3]

im = img.crop(BOX_SIZE)
im = im.filter(ImageFilter.BLUR)
im = im.convert("RGBA")
tmp = Image.new('RGBA', im.size, (0,0,0,0))
draw = ImageDraw.Draw(tmp)
draw.rectangle(((0, 0), im.size), fill=(50,50,50,127))
im = Image.alpha_composite(im, tmp)
draw = ImageDraw.Draw(im)
draw.text((100,25), imageText , FONT_COLOR, font=font)
draw.text((150,250),author,FONT_COLOR,font=font)
img.paste(im,(1500,100,1900,400))

news_im = img.crop(NEWS_BOX_SIZE)
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
        feed_line = feed_line+' '+w
        if(word_count >= 4 or char_count >= 24):
            feed_line += "\n"
            word_count = 1
            char_count = 1                  
    draw.text((158,30+(110*(count-1))), feed_line , FONT_COLOR, font=font)        
    news_im.paste(temp_im,(30,30+(110*(count-1))))
    img.paste(news_im,NEWS_BOX_SIZE)
    count += 1

img.paste(quote_logo_img,(1520,120),mask=quote_alpha)
img.save("images/wallie_final.jpeg")