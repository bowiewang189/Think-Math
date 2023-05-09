# Importing all necessary libraries
import cv2
import os



def makeVideo(path, variable, step, reverse, video_name):
    cam = cv2.VideoCapture(path)
    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print('Error: Creating directory of data')

    fps = cam.get(cv2.CAP_PROP_FPS)
    # 总帧数(frames)
    frames = cam.get(cv2.CAP_PROP_FRAME_COUNT)
    print("帧数：" + str(fps))
    print("总帧数：" + str(frames))
    print("视屏总时长：" + "{0:.2f}".format(frames / fps) + "秒")

    allChangeCount = variable / step
    print("预计获取" + str(allChangeCount) + "变化的帧的视频")

    VideoDurationMi = frames / fps * 1000
    print("原视频有" + str(VideoDurationMi) + "毫秒")
    print(str(int(frames / allChangeCount)) + "就会发生变化")
    height = 0;
    width = 0;
    layers = 0;
    # determine whether to open normally
    if cam.isOpened():
        ret, frame = cam.read()
        height, width, layers = frame.shape
    else:
        ret = False
    print(video_name, "..." ,width,"...", height)
    video = cv2.VideoWriter(video_name, 0, fps, (width, height))
    index = 0;
    num = 0.0;

    allFrames = []
    while ret:
        text = "a = " + str(round(num, 2))
        #text = "frame of No " + str(index)
        cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 50, 50), 4)
        allFrames.append(frame)
        #video.write(frame)
        print("Processing", str(index), "/" + str(frames))
        ret, frame = cam.read()
        index = index + 1
        if (index % (int(frames / allChangeCount)) == 0):
            num = num + step

        if(num>variable):
            break

    print(len(allFrames))
    for x in range(0,len(allFrames)):
        #print(x)
        if reverse:
            video.write(allFrames[x])
        else:
            video.write(allFrames[len(allFrames) - x - 1])

    """
    if reverse:
        video.write(allFrames[x])
    else:
        video.write(allFrames[len(allFrames) - x - 1])
    """



    cam.release()
    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':

    video_name = 'video3.avi'
    path = "F:\\Download\\把悲伤留给自己 - 陈升.mp4"
    makeVideo(path, 10, 0.01, False, video_name)



