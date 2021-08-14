# 解决Ubuntu16.04安装ROS Kinetic后Python3不能import cv2的问题
import sys
if '/opt/ros/kinetic/lib/python2.7/dist-packages' in sys.path:
    sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import multiprocessing as mp
import cv2
import time
import numpy as np
def image_put(q, user, pwd, ip, channel=1):
    # cap = cv2.VideoCapture("rtsp://%s:%s@%s//Streaming/Channels/%d" % (user, pwd, ip, channel))
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        print('HIKVISION')
    else:
        cap = cv2.VideoCapture(0)
        # cap = cv2.VideoCapture("rtsp://%s:%s@%s/cam/realmonitor?channel=%d&subtype=0" % (user, pwd, ip, channel))
        print('DaHua')

    while True:
        # shrnik=cv2.resize(cap.read()[1],(300,300),interpolation=cv2.INTER_AREA)
        # print("cap.read()[1] cap.read()[1] cap.read()[1] cap.read()[1]",cap.read()[0])
        if cap.read()[0]:
            q.put(cap.read()[1])
        else:
            print("ret none")
            time.sleep(3)
            cap.release()
            cap = cv2.VideoCapture(0)
            # cap = cv2.VideoCapture("rtsp://%s:%s@%s//Streaming/Channels/%d" % (user, pwd, ip, channel))
            q.put(cap.read()[1])

        q.get() if q.qsize() > 1 else time.sleep(0.01)

def image_get(q, window_name):
    # cv2.namedWindow(window_name, flags=cv2.WINDOW_FREERATIO)
    # cv2.namedWindow(window_name)
    while True:
        try:
            frame = q.get()
        except Exception as ex:
            print("the problem maybe is:", ex)
            continue

        # result = np.asarray(image)
        # info = "time: %.2f ms" %(1000*exec_time)
        cv2.namedWindow("result", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("result", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def run_single_camera():
    user_name, user_pwd, camera_ip = "admin", "zhuoyu1234", "192.168.3.209"

    mp.set_start_method(method='spawn')  # init
    queue = mp.Queue(maxsize=2)
    processes = [mp.Process(target=image_put, args=(queue, user_name, user_pwd, camera_ip)),
                 mp.Process(target=image_get, args=(queue, camera_ip))]

    [process.start() for process in processes]
    [process.join() for process in processes]
if __name__ == '__main__':
    run_single_camera()
    pass