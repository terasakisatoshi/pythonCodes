import codecs
import re
import urllib.parse
import urllib.request
import os
import socket
from PIL import Image
from scipy.misc import imread,imsave
socket.setdefaulttimeout(10)
Image.MAX_IMAGE_PIXELS = None


def collect_data():
    if not os.path.exists("portrait"):
        os.mkdir("portrait")
    if not os.path.exists("train"):
        os.mkdir("train")

    base_url = 'http://commons.wikipedia.org'
    url = base_url + '/wiki/Category:17th-century_oil_portraits_of_standing_women_at_three-quarter_length'
    suburl = base_url+'/wiki/File:'
    next_page = url

    while len(next_page) > 0:
        url = next_page
        next_page = ''
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            title = re.findall(r'<title>([\s\S]*) - Wikimedia Commons</title>', html)
            if len(title) < 1:
                break
            nextpage = re.findall(
                r'a<\s*href=\"(/w/index.php?[\s\S]*)\" title=\"'+title[0]+'\">[\s\S]*>next page</a>', html)
            gallery = re.findall(
                r'<div class=\"gallerytext\">\s+<a\s+href=\"/wiki/File:(\S*)\"',
                html, re.DOTALL)

            for g in gallery:
                with urllib.request.urlopen(suburl+g) as response:
                    g = urllib.parse.quote_plus(urllib.parse.unquote_plus(g))
                    html = response.read().decode('utf-8')
                    original = re.findall(\
                        r'<a\s+(?:class=\"internal\")?\s*href=\"(https://upload.wikimedia.org/\S*/'+g+')\"[\s\S]*>[\s\S]*</a>',\
                        html)
                    print(original)
                    for ori in original:
                        print(ori)
                        face = ori.rsplit('/', 1)[1]
                        os.system('wget '+ori+' -O portrait/'+face)
                        if face.endswith('.tif') or face.endswith('.tiff'):
                            im=imread(os.path.join('portrait',face))
                            name,ext=os.path.splitext(face)
                            imsave(os.path.join('portrait',name+'.jpg'),im)
                            os.remove('portrait/'+face)

            if len(nextpage) > 0:
                next = nextpage[0].replace('&amp;', '&')
                next_page = base_url+next
            else:
                next_page = ''
    fs = os.listdir('portrait')
    for n, f in enumerate(fs):
        img = Image.open('portrait/'+f).convert('RGB')
        w = img.size[0]/2
        x = img.size[0]/4
        img = img.crop((x, 0, x+w, w)).resize((320, 320))
        img.save('train/'+str(n)+'.png')

def create_train():
    # 320x320のデータセットを作る
    fs = os.listdir('portrait')
    numimg = 0
    for fn in fs:
        # 画像を読み込み
        img = Image.open('portrait/' + fn).convert('RGB')
        # 上部中央の顔付近を切りだす
        w = img.size[0] / 2
        x = img.size[0] / 4
        img = img.crop((x, 0, x+w, w)).resize((320,320))
        # 名前を付けて保存する
        img.save('train/'+str(numimg)+'.png')
        numimg = numimg + 1
if __name__ == '__main__':
    #collect_data()
    create_train()
