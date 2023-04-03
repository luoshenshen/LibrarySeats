from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('lena_std.tif')

img_r, img_g, img_b = img.split()
img_rgb = Image.merge("RGB", [img_r, img_g, img_b])
plt.figure(figsize=(10, 10))

img_RGB = [img_r, img_g, img_b, img_rgb]
img_name = ['R', 'G', 'B', 'RGB']
ii = 1
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.axis("off")
    plt.imshow(img_RGB[i])
    plt.title(img_name[i], fontsize=20)

plt.show()
