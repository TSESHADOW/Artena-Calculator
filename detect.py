import numpy as np
import cv2
import imutils


# image = cv2.imread("test_2560x1440.png")
# image = cv2.imread("test_1920x1080.png")
# image = cv2.imread("test2_2560x1440.png")
# image = cv2.imread("test2_1920x1080.png") 
# image = cv2.imread("test3_1920x1080.png")
# image = cv2.imread("test4_1920x1080.png")


def detect(image):
    print(image)
    image = cv2.imread(image)
    (h, w) = image.shape[:2]
    image = image[int(1*h/6):int(6.5*h/8), 0:int(3*w/4)]
    template = cv2.imread("template_1920x1080.png")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    (height, width) = template.shape[:2] # MERGE h w and height width?

    found = None

    for scale in np.linspace(0.2, 1.0, 20)[::-1]:
        # resize the image and store the ratio
        resized_img = imutils.resize(image, width=int(image.shape[1] * scale))
        ratio = image.shape[1] / float(resized_img.shape[1])

        if resized_img.shape[0] < height or resized_img.shape[1] < width:
            break

        match = cv2.matchTemplate(resized_img, template, cv2.TM_SQDIFF_NORMED)

        _, val_max, min_loc, _ = cv2.minMaxLoc(match)

        if found is None or val_max > found[0]:
            
            found = (val_max, min_loc, ratio)

    temp = int(found[1][0] * found[2] - 200) if int(found[1][0] * found[2] - 200) > 80 else 80
    (startX, startY) = (temp, int(found[1][1] * found[2]))
    (endX, endY) = (int((found[1][0] + width+70) * found[2]), int((found[1][1] + height) * found[2])) # FIX CONSTANT 70

    # draw a bounding box around the detected result and display the image
    cv2.rectangle(image, (startX, startY), (endX, int(endY + (h/5.5))), (255, 255, 255), 1)

    # cv2.imshow("Image", image)
    # cv2.waitKey(0)

    return image, (startX, startY), (endX, int(endY + (h/5.5)))