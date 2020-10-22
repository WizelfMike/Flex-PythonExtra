from PIL import Image

image = Image.open("Bird.JPG")

image.show()


width = image.width
height = image.height

print("De afbeelding is " + str(width) + " pixels breed en " + str(height) + " pixels hood")


print(image.format, image.size, image.mode)