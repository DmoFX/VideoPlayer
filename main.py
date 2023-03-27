import subprocess
import os
video_path = "D:/Docs/Work/Python/Projects/Output/ScreenCapture Output/screenshots/video.mp4"
video_path = video_path.replace("/","\\")
# video_path = "D:\\Docs\\Work\\Python\\Projects\\Output\\ScreenCapture Output\\screenshots\\video.mp4"
# print(os.path.exists(video_path))
print(video_path)
# p = subprocess.Popen(["C:/Program Files/VideoLAN/VLC/vlc.exe","D:\\" + "video" + '.mp4'])
p = subprocess.Popen(["C:/Program Files/VideoLAN/VLC/vlc.exe",video_path,"--loop"])
