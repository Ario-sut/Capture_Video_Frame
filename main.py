import os
import shutil #utiliuty, function, directory trees
import sys
import cv2
from datetime import datetime

class framecapture:
    def __init__(self, video_path):
        self.directory = "captured_frames-%s"%datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.video = cv2.VideoCapture(video_path)
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        os.mkdir(self.directory)

    def capture_frames(self):
        total_frames = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
        count = 0
        while True:
            success, image = self.video.read()
            if not success:
                break
            capture = f"{self.directory}/frame%d.jpg"%count
            count+=1
            progress = (count + 1) / total_frames * 100
            print(f"Progress: {progress:.2f}% ({count + 1}/{total_frames})", end="\r")
            
            cv2.imwrite(capture, image)

if __name__ == '__main__':
    file_path = sys.argv[1]
    fc = framecapture(file_path)
    fc.capture_frames()

'''
    def capture_frames(self):
        cv2.object = cv2.VideoCapture(self.file_path)
        frame_number =0
        frame_found=1
        while frame_found:
            frame_found, image= cv2.object.read()
            capture = f'{self.directory}/frame{frame_number}.jpg'
            cv2.imwrite(capture,image)
            frame_number +=1
'''