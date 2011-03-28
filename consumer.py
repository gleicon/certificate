from hotqueue import HotQueue
from PIL import Image, ImageDraw, ImageFont
import os

# same dir as the htmls (must be public)
DESTDIR = "/var/www/certs.frontend.dir/%s"

WWW_USER_ID = 33
WWW_GROUP_ID = 33

queue = HotQueue("myqueue", host="localhost", port=6379, db=0)

@queue.worker
def wtf(o):
    print 'Creating certificate for %s' % o['name']
    write_image(o['name'], DESTDIR % o['img_path'])

def write_image(wot, out_img):
    orig = '/opt/certificate/certificate.png'
    wot = wot[:20]
    img = Image.open(orig) #.convert("RGB")
    out = Image.new("RGB", (img.size[0], img.size[1]))
    draw = ImageDraw.ImageDraw(img)
    font = ImageFont.truetype('/opt/certificate/Certificate_BoldItalic.ttf', 40)
    textwidth, textheight = font.getsize(wot)
    draw.setfont(font)
    draw.text((150, 400), wot, fill=(0,0,0))
    img.save(out_img)
    os.chown(out_img, WWW_USER_ID, WWW_GROUP_ID)  

if __name__ == '__main__':
    wtf()

