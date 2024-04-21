from yt_dlp import YoutubeDL

message = ""


def progress_tracker(output: dict) -> None:
    global message
    if output['status'] == "downloading":
        message = output["eta"] if output['eta'] else 'ETA Unknown'
    elif output['status'] == 'finished':
        message = "Finished!"


yt_dl_opts = {'extract_flat': 'discard_in_playlist',
              'format': 'bv+ba',
              'format_sort': ['res:1080'],
              'fragment_retries': 10,
              'ignoreerrors': 'only_download',
              'outtmpl': {'default': 'ytdloutput'},
              'postprocessors': [{'key': 'FFmpegConcat',
                                  'only_multi_video': True,
                                  'when': 'playlist'}],
              'progress_hooks': [progress_tracker],
              'quiet': True,
              'no_warnings': True,
              'overwrites': True,
              'retries': 10}


def start_download(url: str) -> None:
    with YoutubeDL(yt_dl_opts) as DL_instance:
        DL_instance.download([url])
