import sys
from ctypes import addressof
import PIL.Image
import requests
from io import BytesIO


ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
# ASCII_CHARS = ["Ñ", "@", "#", "W", "$", "9", "8", "7", "6", "5", "4", "3", "2","1", "0", "?", "!", "a", "b", "c", ";", ":", "+", "=", "-", ",", ".", "_"]


def main():
    #path = input("Enter the Path/URL to the image field : \n")
    path = sys.argv[1]
    print(path)
    try:
        response = requests.get(path)
        image = PIL.Image.open(BytesIO(response.content))
    except:
        print(path, "Unable to find image ")
        quit()
    # resize image
    image = resizes(image)
    # convert image to greyscale image
    greyscale_image = to_greyscale(image)
    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(greyscale_image)
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    # Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i: i+img_width] + "\n"
    # save the string to a file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)
    print(ascii_img)


def resizes(image, new_width=100):
    old_width, old_height = image.size
    new_height = new_width * (old_height / old_width)
    new_height = int(new_height)

    return image.resize((new_width, new_height))


def to_greyscale(image):

    image = image.convert("L")
    print(image)
    return image


def pixel_to_ascii(image):
    pixels = list(image.getdata())
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25]
    return ascii_str


if __name__ == '__main__':
    main()
