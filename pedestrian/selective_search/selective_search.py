import skimage.data
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from selectivesearch import selective_search
from PIL import Image
import numpy as np

def main():

    # loading astronaut image
    #img = skimage.data.astronaut()
    #print(img.shape)

    img = np.asarray(Image.open('000133.jpg'))

    # perform selective search
    img_lbl, regions = selective_search(img, scale=500, sigma=0.9, min_size=10)

    candidates = set()
    for r in regions:
        # excluding same rectangle (with different segments)
        if r['rect'] in candidates:
            continue
        # excluding regions smaller than 2000 pixels
        if r['size'] < 2000:
            continue
        # distorted rects
        x, y, w, h = r['rect']
        if w / h > 1.2 or h / w > 1.2:
            continue
        candidates.add(r['rect'])

    # draw rectangles on the original image
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
    plt.axis('off')
    ax.imshow(img)
    for x, y, w, h in candidates:
        print(x, y, w, h)
        rect = mpatches.Rectangle(
            (x, y), w, h, fill=False, edgecolor='red', linewidth=1)
        ax.add_patch(rect)

    plt.show()
    plt.savefig("test.png")
if __name__ == "__main__":
    main()