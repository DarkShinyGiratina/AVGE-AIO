import shutil
import subprocess

ffmpeg_path = shutil.which("ffmpeg", path="./ffmpeg")
ffprobe_path = shutil.which("ffprobe", path="./ffmpeg")
ffprobe_args = "-v error -select_streams v:0 -count_packets -show_entries stream=nb_read_packets -of csv=p=0".split()
ffmpeg_args = "-y -v quiet -stats -i input_name -c:v libx264 -crf 18 -c:a aac".split()
progress = 0.0


def convert_to_mp4(file: str, output_name: str) -> None:
    # Get number of frames
    if ffprobe_args[0] != ffprobe_path:
        ffprobe_args.insert(0, ffprobe_path)
    ffprobe_args.append(file)
    num_frames = int(subprocess.run(ffprobe_args, capture_output=True, text=True).stdout)
    ffprobe_args.pop()

    if ffmpeg_args[0] != ffmpeg_path:
        ffmpeg_args.insert(0, ffmpeg_path)
    ffmpeg_args[6] = file
    ffmpeg_args.append(output_name)
    ffmpeg_proc = subprocess.Popen(ffmpeg_args, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT, text=True)
    ffmpeg_args.pop()
    for line in ffmpeg_proc.stdout:
        try:
            cur_frame = int(line.split(' fps')[0].split('frame= ')[1])
            global progress
            progress = 100*round(cur_frame / num_frames, 4)
        except:
            pass
