# Frame Capture from Video

This Python script captures frames from a video file and saves them as individual image files. It utilizes the OpenCV (`cv2`) library, which provides various functionalities for computer vision tasks, including video processing.

## Explanation

1. Import the necessary libraries:
   - `os` module: Provides functions for interacting with the operating system.
   - `shutil` module: Offers utility functions for handling files and directories.
   - `sys` module: Provides access to system-specific parameters and functions.
   - `cv2` module: Contains the functions and classes for computer vision tasks.
   - `datetime` module: Enables working with dates and times.

2. Define the `framecapture` class:
   - The class constructor (`__init__`) initializes the necessary variables and creates a directory to store the captured frames. The directory name is generated based on the current date and time.
   - The `capture_frames` method is responsible for capturing frames from the video. It retrieves the total number of frames in the video and then iterates through each frame using a loop. It saves each frame as an individual JPEG image file in the designated directory.

3. In the main block (`if __name__ == '__main__':`), the script retrieves the video file path from the command-line arguments. An instance of the `framecapture` class is created with the provided video path, and the `capture_frames` method is called to initiate the frame capture process.

4. During the frame capture process:
   - The total number of frames in the video is obtained using the `get` method from the `cv2.CAP_PROP_FRAME_COUNT` property.
   - The loop iterates through each frame of the video using the `read` method from the `video` object. If there are no more frames to read, the loop breaks.
   - For each frame, the script generates a capture filename based on the frame count.
   - The progress percentage is calculated using the formula `(count + 1) / total_frames * 100`. This value represents the progress of the frame capture process.
   - The progress is printed on the console using the `print` function, with the `\r` carriage return character to overwrite the previous progress output.
   - The current frame is saved as a JPEG image file using the `imwrite` function from `cv2`.

5. Once all the frames are captured, the script completes execution and displays a completion message.

6. The user can access the captured frames in the specified directory, organized by the capture timestamp.

## Prerequisites

Before running the script, make sure you have the following packages installed:

- **OpenCV**: The OpenCV library is used for video processing. You can install it using the following command:

  ```shell
  pip install opencv-python
 
