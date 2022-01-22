import cv2 
import os

# IMAGES PRESENT = ['image.png' , 'image_1.png' , 'image_2.png' , 'image_2.png' ]
BACK_CAM_PATH = os.path.join('RESOURCES', 'image.png')

def parking_guide_lines(BACK_CAM_PATH):
    image = cv2.imread(BACK_CAM_PATH)
    BACK_CAM_IMAGE = cv2.resize(image, (700, 500))
    # print(BACK_CAM_IMAGE.shape)
    # WID_DIV = BACK_CAM_IMAGE.shape[1]//6
    # HIG_DIV = BACK_CAM_IMAGE.shape[0]//7
    RED = (0,0,255)
    GREEN = (0,255,0)
    YELLOW = (0,255,255)
    X_PAD = 20
    Y_PAD = 40
    X_START_POS = 60
    Y_START_POS = 40
    LINE_THICKNESS = 3

    #------------------------------ DRAW LINE STARTS ------------------------------
    BACK_CAM_IMAGE = cv2.line(BACK_CAM_IMAGE,(X_START_POS,BACK_CAM_IMAGE.shape[0]-Y_START_POS), (X_START_POS+3*X_PAD,BACK_CAM_IMAGE.shape[0]-40-Y_PAD), RED,LINE_THICKNESS)
    BACK_CAM_IMAGE = cv2.line(BACK_CAM_IMAGE,(X_START_POS,BACK_CAM_IMAGE.shape[0]-Y_START_POS), (X_START_POS+3*X_PAD,BACK_CAM_IMAGE.shape[0]-Y_START_POS), RED,LINE_THICKNESS)
    # side lines
    BACK_CAM_IMAGE = cv2.line(BACK_CAM_IMAGE,(BACK_CAM_IMAGE.shape[1]-X_START_POS,BACK_CAM_IMAGE.shape[0]-Y_START_POS), (BACK_CAM_IMAGE.shape[1]-X_START_POS-3*X_PAD,BACK_CAM_IMAGE.shape[0]-40-Y_PAD), RED,LINE_THICKNESS)
    BACK_CAM_IMAGE = cv2.line(BACK_CAM_IMAGE,(BACK_CAM_IMAGE.shape[1]-X_START_POS,BACK_CAM_IMAGE.shape[0]-Y_START_POS), (BACK_CAM_IMAGE.shape[1]-X_START_POS-3*X_PAD,BACK_CAM_IMAGE.shape[0]-Y_START_POS), RED,LINE_THICKNESS)


    BACK_CAM_IMAGE = cv2.line(BACK_CAM_IMAGE,(X_START_POS+3*X_PAD,BACK_CAM_IMAGE.shape[0]-40-Y_PAD), (X_START_POS+6*X_PAD , BACK_CAM_IMAGE.shape[0]-40-2*Y_PAD), YELLOW,LINE_THICKNESS)
    BACK_CAM_IMAGE = cv2.line(BACK_CAM_IMAGE,(X_START_POS+3*X_PAD,BACK_CAM_IMAGE.shape[0]-40-Y_PAD), (X_START_POS+6*X_PAD , BACK_CAM_IMAGE.shape[0]-40-Y_PAD), YELLOW,LINE_THICKNESS)
    # side lines
    BACK_CAM_IMAGE = cv2.line(BACK_CAM_IMAGE,(BACK_CAM_IMAGE.shape[1]-X_START_POS-3*X_PAD,BACK_CAM_IMAGE.shape[0]-40-Y_PAD), (BACK_CAM_IMAGE.shape[1]-X_START_POS-6*X_PAD,BACK_CAM_IMAGE.shape[0]-40-2*Y_PAD), YELLOW,LINE_THICKNESS)
    BACK_CAM_IMAGE = cv2.line(BACK_CAM_IMAGE,(BACK_CAM_IMAGE.shape[1]-X_START_POS-3*X_PAD,BACK_CAM_IMAGE.shape[0]-40-Y_PAD), (BACK_CAM_IMAGE.shape[1]-X_START_POS-6*X_PAD,BACK_CAM_IMAGE.shape[0]-40-Y_PAD), YELLOW,LINE_THICKNESS)


    BACK_CAM_IMAGE = cv2.line(BACK_CAM_IMAGE,(X_START_POS+6*X_PAD , BACK_CAM_IMAGE.shape[0]-40-2*Y_PAD), (X_START_POS+9*X_PAD , BACK_CAM_IMAGE.shape[0]-40-3*Y_PAD), GREEN,LINE_THICKNESS)
    BACK_CAM_IMAGE = cv2.line(BACK_CAM_IMAGE,(X_START_POS+6*X_PAD , BACK_CAM_IMAGE.shape[0]-40-2*Y_PAD), (X_START_POS+9*X_PAD , BACK_CAM_IMAGE.shape[0]-40-2*Y_PAD), GREEN,LINE_THICKNESS)
    # side lines
    BACK_CAM_IMAGE = cv2.line(BACK_CAM_IMAGE,(BACK_CAM_IMAGE.shape[1]-X_START_POS-6*X_PAD,BACK_CAM_IMAGE.shape[0]-40-2*Y_PAD), (BACK_CAM_IMAGE.shape[1]-X_START_POS-9*X_PAD,BACK_CAM_IMAGE.shape[0]-40-3*Y_PAD), GREEN,LINE_THICKNESS)
    BACK_CAM_IMAGE = cv2.line(BACK_CAM_IMAGE,(BACK_CAM_IMAGE.shape[1]-X_START_POS-6*X_PAD,BACK_CAM_IMAGE.shape[0]-40-2*Y_PAD), (BACK_CAM_IMAGE.shape[1]-X_START_POS-9*X_PAD,BACK_CAM_IMAGE.shape[0]-40-2*Y_PAD), GREEN,LINE_THICKNESS)
    BACK_CAM_IMAGE = cv2.line(BACK_CAM_IMAGE,(BACK_CAM_IMAGE.shape[1]-X_START_POS-9*X_PAD,BACK_CAM_IMAGE.shape[0]-40-3*Y_PAD), (BACK_CAM_IMAGE.shape[1]-X_START_POS-12*X_PAD,BACK_CAM_IMAGE.shape[0]-40-3*Y_PAD), GREEN,LINE_THICKNESS)
    BACK_CAM_IMAGE = cv2.line(BACK_CAM_IMAGE,(X_START_POS+9*X_PAD , BACK_CAM_IMAGE.shape[0]-40-3*Y_PAD), (X_START_POS+12*X_PAD , BACK_CAM_IMAGE.shape[0]-40-3*Y_PAD), GREEN,LINE_THICKNESS)
    #------------------------------ DRAW LINE STARTS ------------------------------

    cv2.imshow("GUIDED IMAGE", BACK_CAM_IMAGE)
    cv2.waitKey(0)

if __name__ == '__main__':
    parking_guide_lines(BACK_CAM_PATH)
