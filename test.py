import subtitles as subs
import ytdl as dl
import glob
import shutil
import threading

t = threading.Thread(target=dl.start_download, args=['https://www.youtube.com/watch?v=4TzVOLOROkM'])
t.start()
t.join()


output_file = glob.glob("ytdloutput.*")[0]
ffmpeg_path = shutil.which("ffmpeg", path="./ffmpeg")
