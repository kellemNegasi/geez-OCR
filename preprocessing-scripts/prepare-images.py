from PIL import Image, ImageDraw,ImageFont,ImageOps
def generate_image():
    image_path_output = '../dataset/'
    image_name_output = 'tes.jpg'
    mode = 'RGB' # for color image “L” (luminance) for greyscale images, “RGB” for true color images, and “CMYK” for pre-press images.
    size = (280, 480)
    color = (255, 255, 255)
    font = ImageFont.truetype(r'../resources/fonts/GeezAble.ttf',550)
    img = Image.new(mode, size, color)
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), 'ሀ', (0, 0, 0), font=font)
    img=ImageOps.grayscale(img)
    img.save(image_path_output + image_name_output )
generate_image()
