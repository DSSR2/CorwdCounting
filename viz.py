from matplotlib import pyplot as plt
from matplotlib import cm as CM
from PIL import Image
import numpy as np


def resize(density_map, image):
    density_map = 255*density_map/np.max(density_map)
    density_map= density_map[0][0]
    image = image[0]
    result_img = np.zeros((density_map.shape[0]*2, density_map.shape[1]*2))
    for i in range(result_img.shape[0]):
        for j in range(result_img.shape[1]):
            result_img[i][j] = density_map[int(i / 2)][int(j / 2)] / 4
    result_img  = result_img.astype(np.uint8, copy=False)
    return result_img

def vis_densitymap(o, den, cc, img_path):
    fig = plt.figure(figsize=(15,15))
    columns = 2
    rows = 1
    # X = np.transpose(o, (1, 2, 0))
    X = Image.open(img_path).convert('RGB')
    summ = int(np.sum(den))
    
    den = resize(den, o)
    
    for i in range(1, columns*rows +1):
        # image plot
        if i == 1:
            img = X
            fig.add_subplot(rows, columns, i)
            plt.gca().set_axis_off()
            plt.margins(0,0)
            plt.gca().xaxis.set_major_locator(plt.NullLocator())
            plt.gca().yaxis.set_major_locator(plt.NullLocator())
            plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
            plt.imshow(img)
            # img.save("./images/crowd_img3.jpg")

        # Density plot
        if i == 2:
            img = den
            fig.add_subplot(rows, columns, i)
            plt.gca().set_axis_off()
            plt.margins(0,0)
            plt.gca().xaxis.set_major_locator(plt.NullLocator())
            plt.gca().yaxis.set_major_locator(plt.NullLocator())
            plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
            plt.text(1, 80, 'M-SegNet* Est: '+str(summ)+', Gt:'+str(cc), fontsize=7, weight="bold", color = 'w')
            plt.imshow(img, cmap=CM.jet)
            # plt.imsave("./images/crowd_den3.jpg", img)
    
    filename = img_path.split('/')[-1]
    filename = filename.replace('.jpg', '_heatpmap.png')

