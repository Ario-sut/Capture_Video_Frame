import os  
import shutil  
import sys  
import cv2  
from datetime import datetime


class FrameCapture:
    def __init__(self, video_path):
        self.directory = f"captured_frames-{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
        self.video = cv2.VideoCapture(video_path)
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)  # Remove the existing directory if it already exists
        os.mkdir(self.directory)  # Create a new directory to store the captured frames

    def capture_frames(self):
        total_frames = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
        count = 0
        while True:
            success, image = self.video.read()
            if not success:
                break
            capture = f"{self.directory}/frame{count}.jpg"  # Define the file path for the captured frame
            count += 1
            progress = (count + 1) / total_frames * 100
            print(f"Progress: {progress:.2f}% ({count + 1}/{total_frames})", end="\r")  # Print the capture progress
            cv2.imwrite(capture, image)  # Save the captured frame as an image file

if __name__ == '__main__':
    file_path = sys.argv[1]  # Get the video file path from the command line argument
    fc = FrameCapture(file_path)  # Create an instance of the FrameCapture class
    fc.capture_frames()  # Start capturing the frames from the video
