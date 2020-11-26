from PIL import ImageDraw, Image


def image_filter(name):
    image = Image.open(name)
    new_image = Image.new('RGB', image.size)

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = image.getpixel((i, j))
            gray = int(r * 0.2 + g * 0.7 + b * 0.07)
            new_image.putpixel((i, j), (gray, gray, gray))

    new_image.save('img/goslya.jpg', 'JPEG')


image_filter('img/image.jpg')
