from PIL import Image, ImageFont, ImageDraw

msg = 'HBD Ankit'

font = ImageFont.truetype('arialbd.ttf', 15) #load the font
size = font.getsize(msg)  #calc the size of text in pixels
image = Image.new('1', size, 1)  #create a b/w image
draw = ImageDraw.Draw(image)
draw.text((0, 0), msg, font=font) #render the text to the bitmap
for i in range(size[1]): 
#scan the bitmap:
# print ' ' for black pixel and 
# print '@' for white one
    line = []
    for j in range(size[0]):
        if image.getpixel((j, i)): line.append(' '),
        else: line.append('@'),
    print(''.join(line))

img = Image.open("image.jpg")
width, height = img.size
new_width = 150 
new_height = int((height * new_width) / width)
new_image = img.resize((new_width, new_height))
new_image = new_image.convert("L") # convert to grayscale

ascii_chars = [ '#', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.']
def image_to_ascii(image):
    image_as_ascii = []
    all_pixels = list(image.getdata())
    for pixel_value in all_pixels:
        index = int(pixel_value / 25) # 0 - 10
        image_as_ascii.append(ascii_chars[index])
    return image_as_ascii   
        
#convert every pixel to the appropriate ascii character from "ascii_chars"
img_as_ascii = image_to_ascii(new_image)
img_as_ascii = ''.join(ch for ch in img_as_ascii)
for c in range(0, len(img_as_ascii), new_width):
        print(img_as_ascii[c:c+new_width])
