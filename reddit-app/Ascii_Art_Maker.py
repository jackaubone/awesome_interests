import sys
from ctypes import addressof
import PIL.Image
import PIL.ImageEnhance
import requests
from io import BytesIO

image_scale = 96
# ASCII_CHARS1 = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
ASCII_CHARS = ['.', ',', ':', ';', '+', '*', '?', '%', '$', '#', '@']
# ASCII_CHARS = ["Ñ", "@", "#", "W", "$", "9", "8", "7", "6", "5", "4", "3", "2","1", "0", "?", "!", "a", "b", "c", ";", ":", "+", "=", "-", ",", ".", "_"]
image_list = []


def main(path):
    #path = input("Enter the Path/URL to the image field : \n")
    #path = sys.argv[1]
    # print(path)
    try:
        response = requests.get(path)
        image = PIL.Image.open(BytesIO(response.content))
    except:
        print(path, "Unable to find image ")
        quit()
    # resize image
    image = resizes(image)

    # raise contrast of image
    contrasted_image = raise_contrast(image)

    # convert image to greyscale image
    greyscale_image = to_greyscale(contrasted_image)

    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(greyscale_image)

    # Split the string based on width  of the image
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i: i+img_width] + "\n"

    # save the string to a file
    # with open("ascii_image.txt", "w") as f:
    #     f.write(ascii_img)
    image_list.append(ascii_img)


def resizes(image, new_width=image_scale):
    old_width, old_height = image.size
    new_height = 0.5 * (new_width * (old_height / old_width))
    new_height = int(new_height)

    return image.resize((new_width, new_height))


def raise_contrast(image):
    enhancer = PIL.ImageEnhance.Contrast(image)
    factor = 6
    image = enhancer.enhance(factor)
    return image


def to_greyscale(image):

    image = image.convert("L")
    return image


def pixel_to_ascii(image):
    pixels = list(image.getdata())
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25]
    return ascii_str


if __name__ == '__main__':
    main()
