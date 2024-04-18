import ffmpeg_normalize as fn

test = fn.FFmpegNormalize(audio_codec="aac")

test.add_media_file("./Country Roads Video/CountryRoads.mp4", "test.mp4")

test.run_normalization()
