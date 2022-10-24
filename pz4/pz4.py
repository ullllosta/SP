from PIL import Image, ImageDraw, ImageFont

img = Image.open('пз4.png')
watermark = Image.open('пз44.png')
img.paste(watermark, (-100, 260), watermark)

img.show()