from django.shortcuts import render,HttpResponse
import os
import win32print
import win32api

def Device(self,pdf_path,printer_name):

    # for device in contex.list_devices(subsystem='usb'):
    #     # print(device.sys_name,device.device_node,'\n')
    #     print(f"Device Name: {device.get('ID_MODEL')}, Device Path: {device.device_node}")
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
    # Ensure the PDF file exists
    print(pdf_path,printer_name)
    if not os.path.exists(pdf_path):
        print(f"PDF file not found: {pdf_path}")
        return

    try:

        win32api.ShellExecute(0, "print", pdf_path, None, ".", 0)
        print(f"Sent {pdf_path} to printer {printer_name}.")

    except Exception as e:
        print(f"Error occurred while printing PDF: {e}")
    return HttpResponse('Hello')
