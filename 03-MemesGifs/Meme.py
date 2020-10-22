from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

image = Image.open("Bird.JPG")


image.show

lettertype = ImageFont.truetype("impact.ttf", 20)

tekengebied = ImageDraw.Draw(image)

tekst = "Bird\Bottom Text!"
tekengebied.multiline_text((10,10), tekst, font=lettertype, fill=(0,0,0))

image.show()

image.save("meme_met_tekst.jpg")
