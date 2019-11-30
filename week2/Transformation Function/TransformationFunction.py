
import cv2
import numpy as np

try:
    import matplotlib.pyplot as plt
    print("matplotlib imported")
except ImportError:
    print("matplotlib is not install, let's install right now")
    import os
    os.system('python -m pip install -U matplotlib')
    try:
        import matplotlib.pyplot as plt
        print("done install and import matplotlib")
    except ImportError:
        print("matplotlib is can't install, please using terminal install package before run code")
        print("scrip close")
        exit()

def negative(image):
    image_0 = 255 - image
    image_1 = np.ones(np.shape(image))*255 - image
    image_1 = np.array(image_1, dtype=np.uint8)
    return image_1, image_0

def log(image, c):
    ones = np.ones(np.shape(image))
    image_1 = c * np.log(ones + image)
    image_1 = np.array(image_1, dtype=np.uint8)
    try:
        image_0 = c * np.log(1 + image)
        image_0 = np.array(image_0, dtype=np.uint8)
    except:
        print("Error")
    return image_1, image_0

if __name__ == '__main__':
    image = cv2.imread('lena.png')
    print('read image lena.png done')
    image_1, image_0 = negative(image)
    image_3, image_2 = log(image, 1)
    image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
    image_0 = cv2.cvtColor(image_0, cv2.COLOR_BGR2GRAY)
    image_3 = cv2.cvtColor(image_3, cv2.COLOR_BGR2GRAY)
    image_2 = cv2.cvtColor(image_2, cv2.COLOR_BGR2GRAY)
    print("transformer done")
    #show negative result image
    fig = plt.figure(num=1, figsize=[8, 6.4])
    var = fig.add_subplot(2, 2, 1)
    var.set_title('Original image')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    var = fig.add_subplot(2, 2, 2)
    var.set_title('Original image to Gray')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
    var = fig.add_subplot(2, 2, 3)
    var.set_title('Negative Transformation')
    plt.imshow(image_1)
    var = fig.add_subplot(2, 2, 4)
    var.set_title('Negative Transformation')
    plt.imshow(image_0)
    #show log result image
    fig_log = plt.figure(num=2, figsize=[8, 6.4])
    var = fig_log.add_subplot(2, 2, 1)
    var.set_title('Original image')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    var = fig_log.add_subplot(2, 2, 2)
    var.set_title('Original image to Gray')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
    var = fig_log.add_subplot(2, 2, 3)
    var.set_title('log Transformation')
    plt.imshow(image_3)
    var = fig_log.add_subplot(2, 2, 4)
    var.set_title('log Transformation')
    plt.imshow(image_2)
    plt.show()
    exit()








