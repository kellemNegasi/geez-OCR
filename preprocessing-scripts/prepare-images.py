from PIL import Image, ImageDraw,ImageFont,ImageOps
import os
import csv
def generate_image(font=None,char=None,dest_folder=None):
    path=dest_folder+char+'/'
    os.makedirs(path, exist_ok=True)
    name_prefix=font.split('/')[-1].split('.')[0]
    print("preparing for font ",name_prefix)
    image_name_output =name_prefix+'_'+char+'.jpg'
    mode = 'RGB' # for color image “L” (luminance) for greyscale images, “RGB” for true color images, and “CMYK” for pre-press images.
    size = (500, 400)
    color = (255, 255, 255)
    font = ImageFont.truetype(font,400)
    img = Image.new(mode, size, color)
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), char, (0, 0, 0), font=font)
    img=ImageOps.grayscale(img)
    img.save(path + image_name_output )
def read_csv(file):
    with open(file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    chars=[]
    for char in data:
        chars.append(char[0])
    return chars
fonts_dir='../resources/fonts/'
fonts=[]
image_path_output = '../dataset/chars/'
csv_file='../resources/geez-characters.csv'
characters=read_csv(csv_file)

for file in os.listdir(fonts_dir):
    if file.split('.')[-1]=='ttf':
         fonts.append(fonts_dir+str(file))  
for char in characters:
    print('...preparing for character ',char)
    for font in fonts:
        generate_image(font=font,char=char,dest_folder=image_path_output)