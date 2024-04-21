import subtitles as subs
import ytdl as dl
import ffmpeg_encode as ff_e
import threading
import time
import glob

output_file = glob.glob("ytdloutput.*")[0]

t = threading.Thread(target=ff_e.convert_to_mp4, args=[output_file, "out.mp4"])
t.start()
while (t.is_alive()):
    print(ff_e.progress)
    time.sleep(0.1)
