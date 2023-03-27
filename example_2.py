import vlc
import time

# creating vlc media player object
video_path = "D:/Docs/Work/Python/Projects/Output/ScreenCapture Output/screenshots/video.mp4"
media_player = vlc.MediaPlayer(video_path)

# start playing video
media_player.play()
media_player.vlm_set_loop("1", True)

# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(5)