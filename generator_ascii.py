import os
import PIL


def simple_ascii_art(path_to_image):
    from PIL import Image
    ascii_chars = ['#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']

    def scale_image(image, new_width=100):
        (original_width, original_height) = image.size
        aspect_ratio = original_height / float(original_width)
        new_height = int(aspect_ratio * new_width)

        new_image = image.resize((new_width, new_height))
        return new_image

    def convert_to_grayscale(image):
        return image.convert('L')

    def map_pixels_to_ascii_chars(image, range_width=25):
        pixels_in_image = list(image.getdata())
        pixels_to_chars = [ascii_chars[int(pixel_value / range_width)] for
                           pixel_value in pixels_in_image]

        return "".join(pixels_to_chars)

    def convert_image_to_ascii(image, new_width=100):
        image = scale_image(image)
        image = convert_to_grayscale(image)

        pixels_to_chars = map_pixels_to_ascii_chars(image)
        len_pixels_to_chars = len(pixels_to_chars)

        image_ascii = [pixels_to_chars[index: index + new_width] for index in
                       range(0, len_pixels_to_chars, new_width)]

        return "\n".join(image_ascii)

    def handle_image_conversion(image_filepath):
        image = None
        try:
            image = Image.open(image_filepath)
        except Exception as e:
            print("Unable to open image file {image_filepath}.".format(
                image_filepath=image_filepath))
            print(e)
            return

        image_ascii = convert_image_to_ascii(image)
        #print(image_ascii)
        with open("Ascii_art.txt", "w") as f:
            f.write(image_ascii)
        print(os.path.dirname(os.path.abspath(__file__)))
        op = os.path.dirname(os.path.abspath(__file__))

    handle_image_conversion(path_to_image)
    return "test done"


def color_ascii_art(int_scale_factor, set_fill, path_to_image):
    from PIL import Image, ImageDraw, ImageFont
    import math

    c = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:," \
        "\"^`'. "[::-1]
    # chars = "#Wo- "[::-1]
    charArray = list(c)
    charLength = len(charArray)
    interval = charLength / 256

    scaleFactor = float(int_scale_factor)

    oneCharWidth = 10
    oneCharHeight = 18

    def getChar(inputInt):
        return charArray[math.floor(inputInt * interval)]

    text_file = open("Output.txt", "w")

    im = PIL.Image.open(path_to_image)

    fnt = PIL.ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

    width, height = im.size
    im = im.resize((int(scaleFactor * width), int(
        scaleFactor * height * (oneCharWidth / oneCharHeight))),
                   PIL.Image.NEAREST)
    width, height = im.size
    pix = im.load()

    outputImage = PIL.Image.new('RGB',
                                (oneCharWidth * width, oneCharHeight * height),
                                color=(0, 0, 0))
    d = PIL.ImageDraw.Draw(outputImage)

    for i in range(height):
        for j in range(width):
            r, g, b = pix[j, i]
            h = int(r / 3 + g / 3 + b / 3)
            pix[j, i] = (h, h, h)
            text_file.write(getChar(h))
            if set_fill == 1:
                d.text((j * oneCharWidth, i * oneCharHeight), getChar(h),
                       font=fnt, fill=(r, g, b))
            if set_fill == 0:
                d.text((j * oneCharWidth, i * oneCharHeight), getChar(h),
                       font=fnt, fill=(h, h, h))
            # fill=(r, g, b)
        text_file.write('\n')
    text_file.close()
    outputImage.save('Ascii_art.png')
    return "test done"
