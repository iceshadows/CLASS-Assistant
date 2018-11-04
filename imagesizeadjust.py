from PIL import Image
import os
dir = 'D:/Projects/Code/Python3/Image-autoadjust/QDU-ClassAssistant/PHOTO/'
if os.path.exists(dir):
    dies = os.listdir(dir)
    for diec in dies:
        print(diec)
        im = Image.open(dir+diec)
        out = im.resize((538,441),Image.ANTIALIAS) #resize image with high-quality
        out.save(dir+diec)
