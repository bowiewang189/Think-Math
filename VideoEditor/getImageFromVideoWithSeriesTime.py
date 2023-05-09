# Importing all necessary libraries
import cv2
import os

# Read the video from specified path
cam = cv2.VideoCapture("E:\\电影\\搭错车 1983.avi")

try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0

# reading from frame

Correctdata = [];
with open("timeSeries", "r", encoding='UTF-8') as f:  # 打开文件
    data = f.readlines()  # 读取文件
    for x in data:
        temp = x.replace('\n','');
        tempList = temp.split(":")
        if len(tempList) == 2:
            Correctdata.append(int(tempList[0]) * 60 + int(tempList[1]))
        if len(tempList) == 3:
            Correctdata.append(int(tempList[0]) * 3600 + int(tempList[1]) * 60 + int(tempList[2]))
print(Correctdata)

for x in Correctdata:
    cam.set(cv2.CAP_PROP_POS_MSEC, x * 1000)
    ret, frame = cam.read()
    if ret:
        name = './data/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(name, frame)
        currentframe += 1

cam.release()
cv2.destroyAllWindows()
