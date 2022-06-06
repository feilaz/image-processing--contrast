from PIL import Image

def picture_histogram_eqalization(photo):
    cdf = []
    sum = 0
    histogram = photo.histogram()
    pixels = list(photo.getdata())
    width, height = photo.size

    for i in range(256):
        sum += histogram[i]
        cdf.append(sum)

    for n in range(height * width):
        pixels[n] = round((cdf[pixels[n]] - 1) / (height * width - 1) * 255)

    photo.putdata(pixels)
    return photo

if __name__ == '__main__':
    # image location
    photo = Image.open("yoda.jpeg")
    photo = photo.convert("L")
    photo = picture_histogram_eqalization(photo)
    photo.show()
    # compare to normal photo
    Image.open("yoda.jpeg").convert("L").show()