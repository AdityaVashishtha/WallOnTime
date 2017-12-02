import PIL
import urllib as URL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter
from PIL import ImageEnhance

# CONSTANT Declaration for usage -----START
FONT_COLOR = (200,230,255)
FONT_SIZE = 30
FONT_APPLE_GARAMOND = "/usr/share/fonts/AppleGaramond-LightItalic.ttf"
BOX_SIZE = (1500,100,1900,400)
NEWS_BOX_SIZE = (1500,450,1900,980)
RESIZE_FACTOR_LOGO = 1
# CONSTANT Declaration for usage -----END
imageText='''
The life is not Easy but it is 
not difficult either..
        
                    -  ABC Jones
'''


# # # Structuring START #########################
# TODO # 1. Quote Loader                        #
# TODO # 2. News Loader                         #
# TODO # 3. Image Loader                        #
# TODO # 4. Merger                              #
# TODO # 5. Constant Storage                    #
# # # Structuring END ###########################


# print "downloading image started ....."
# page = URL.urlopen("https://source.unsplash.com/random/1920x1080")
# image_info = page.info()
# print image_info
# raw_data = page.read()
# print "downloading image stop, writing to file ....."
# image_file = open("images/wallie.jpeg","w")
# image_file.write(raw_data)
# page.close()
# image_file.close()

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
img.paste(im,(1500,100,1900,400))

news_im = img.crop(NEWS_BOX_SIZE)
news_im = news_im.filter(ImageFilter.BLUR)
news_im = news_im.convert("RGBA")
tmp = Image.new('RGBA', news_im.size, (0,0,0,0))
draw = ImageDraw.Draw(tmp)
draw.rectangle(((0, 0), news_im.size), fill=(50,50,50,127))
news_im = Image.alpha_composite(news_im, tmp)
img.paste(news_im,NEWS_BOX_SIZE)

img.paste(quote_logo_img,(1520,120),mask=quote_alpha)
img.save("images/wallie_final.jpeg")