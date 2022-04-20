from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import QtGui
from PyQt5.QtGui import *
import numpy as np


def convert(image_path):
    im = Image.open(image_path)
    im = im.convert('RGBA')

    data = np.array(im)
    red, green, blue, alpha = data.T

    white_areas = (red == 230) & (blue == 230) & (green == 230)
    data[..., :-1][white_areas.T] = (0, 0, 0)

    im2 = Image.fromarray(data)

    return QtGui.QPixmap.fromImage(ImageQt(im2))


#final_image = convert('v3/icons/cil-3d.png')
# final_image.show()
