import urllib as URL

def loadImage(image_url,image_path):
    print "downloading image started ....."
    page = URL.urlopen(image_url)
    image_info = page.info()    
    raw_data = page.read()
    print "downloading image stop, writing to file ....."
    image_file = open(image_path,"w")
    image_file.write(raw_data)
    page.close()
    image_file.close()

