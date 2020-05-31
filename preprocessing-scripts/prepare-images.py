from PIL import Image, ImageDraw,ImageFont,ImageOps
import os
def generate_image(font):
    image_path_output = '../dataset/'
    name_prefix=font.split('/')[-1].split('.')[0]
    print("preparing for font ",name_prefix)
    image_name_output =name_prefix+'___test.jpg'
    mode = 'RGB' # for color image “L” (luminance) for greyscale images, “RGB” for true color images, and “CMYK” for pre-press images.
    size = (280, 480)
    color = (255, 255, 255)
    font = ImageFont.truetype(font,550)
    img = Image.new(mode, size, color)
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), 'ሀ', (0, 0, 0), font=font)
    img=ImageOps.grayscale(img)
    img.save(image_path_output + image_name_output )

fonts_dir="../resources/fonts/"
fonts=[]
for file in os.listdir(fonts_dir):
    if file.split('.')[-1]=='ttf':
         fonts.append(fonts_dir+str(file))  
#generate_image()
print(len(fonts))
for font in fonts:
    generate_image(font)