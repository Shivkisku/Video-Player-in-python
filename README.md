# Video-Player-in-python

This is a Python program that creates a simple video player GUI using the tkinter library and the OpenCV (cv2) library for video processing. The program allows the user to select a video file using the "Open" button, and then play the video using the "Play" button. The video is displayed in a tkinter Label widget called "video_frame". The program also has a "Pause" button that allows the user to pause and resume the video playback.

When the user clicks the "Open" button, the program uses the tkinter filedialog to open a file selection dialog, where the user can select a video file. The file path is stored in the "video_path" attribute of the VideoPlayer object.

When the user clicks the "Play" button, the program creates a cv2 VideoCapture object with the video file path, and reads the first frame of the video. Then the program enters a loop that reads each frame of the video, converts it from BGR to RGB color space, resizes it to fit the dimensions of the "video_frame" widget, and updates the widget with the new frame using a PhotoImage object. The loop also checks for the "Pause" button state, and if it is pressed, continues to the next iteration of the loop without reading the next frame from the video.

When the video playback is complete or the user closes the window, the program releases the cv2 VideoCapture object.



