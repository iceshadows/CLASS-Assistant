from PIL import Image

infile = "D:\\test\\1.jpg" #导入路径
outfile = "D:\\test\\2.jpg" #导出路径
im = Image.open(infile)
out = im.resize((538,441),Image.ANTIALIAS) #resize image with high-quality
out.save(outfile)
