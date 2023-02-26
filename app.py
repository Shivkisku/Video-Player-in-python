import cv2
import tkinter as tk
from tkinter import filedialog

class VideoPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Video Player")
        self.video_path = None
        self.paused = False
        
        # Create buttons
        self.open_button = tk.Button(master, text="Open", command=self.open_file)
        self.play_button = tk.Button(master, text="Play", command=self.play_video)
        self.pause_button = tk.Button(master, text="Pause", command=self.pause_video)
        
        # Add buttons to layout
        self.open_button.pack(side=tk.LEFT)
        self.play_button.pack(side=tk.LEFT)
        self.pause_button.pack(side=tk.LEFT)
        
        # Create video frame
        self.video_frame = tk.Label(master)
        self.video_frame.pack()
        
    def open_file(self):
        # Ask user to select a video file
        self.video_path = filedialog.askopenfilename()
        
    def play_video(self):
        # If no video is selected, do nothing
        if self.video_path is None:
            return
        
        # Create video capture object and get first frame
        self.cap = cv2.VideoCapture(self.video_path)
        ret, frame = self.cap.read()
        
        # Loop through video frames
        while ret:
            # Convert BGR image to RGB and resize to fit window
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (640, 480))
            
            # Update video frame in GUI
            img = tk.PhotoImage(data=cv2.imencode('.png', frame)[1].tobytes())
            self.video_frame.config(image=img)
            self.video_frame.image = img
            
            # Wait for 30 milliseconds and check for pause button
            self.master.update()
            if self.paused:
                continue
            ret, frame = self.cap.read()
            
        # Release video capture object when done
        self.cap.release()
        
    def pause_video(self):
        self.paused = not self.paused
        
root = tk.Tk()
player = VideoPlayer(root)
root.mainloop()
