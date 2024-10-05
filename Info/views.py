from django.shortcuts import render,HttpResponse
import cv2
import pyudev
contex = pyudev.Context()
def Device(self):

    for device in contex.list_devices(subsystem='usb'):
        # print(device.sys_name,device.device_node,'\n')
        print(f"Device Name: {device.get('ID_MODEL')}, Device Path: {device.device_node}")
    # cap = cv2.VideoCapture('/dev/video0')
    # if not cap.isOpened():
    #     return HttpResponse('camera not found\n')
    
    # while True:
    #     ret,frem=cap.read()
    #     cv2.imshow('Hello',frem)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break   

    # # Release the camera and close all OpenCV windows
    # cap.release()
    # cv2.destroyAllWindows()
    return HttpResponse('Hello')
