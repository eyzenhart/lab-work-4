from PIL import ImageDraw, Image


def board(num, size):
    new_image = Image.new('RGB', (num * size, num * size), (256, 256, 256))
    draw = ImageDraw.Draw(new_image)
    for i in range(num):
        for j in range(num):
            if i % 2 == 0 and j % 2 == 0 or i % 2 == 1 and j % 2 == 1:
                draw.rectangle([j * size, i * size, j * size + size - 1, i * size + size - 1], (0, 0, 0))

    new_image.save('res.png', 'PNG')


board(8, 50)
