from PIL import Image

def compute_average_image_color(img):
    width, height = img.size

    r_total = 0
    g_total = 0
    b_total = 0

    count = 0
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x,y))
            r_total += r
            g_total += g
            b_total += b
            count += 1

    return (r_total/count, g_total/count, b_total/count)

img = Image.open('dogs.jpeg')
img = img.resize((50,50))  # Small optimization
average_color = compute_average_image_color(img)
print("The three dominant color of the image RGB is: ")
print(average_color)