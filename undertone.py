import os
import yt_dlp


ytdlp_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
    'postprocessor_args': [
        '-ar', '16000'
    ],
    'outtmpl': 'audiofiles/%(title)s.%(ext)s',
    'restrictfilenames': True,
}

def whispercpp_installed():
    # determines if whispercpp is available.
    return os.path.exists("whisper.cpp")
    pass

def download_whispercpp():
    # https://github.com/ggerganov/whisper.cpp
    # downloads whispercpp
    os.system("git clone https://github.com/ggerganov/whisper.cpp.git")
    os.system("cd whisper.cpp && make -j")


def run_model(audio, size):
    os.system(f"cd whisper.cpp && ./main -m ./models/ggml-{size}.bin -f '../{audio}' -t 16 -otxt")

    pass

def download_video(url):
    # downloads a video, converts to Wav 16k and returns the filepath
    with yt_dlp.YoutubeDL(ytdlp_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        audio_filename = ydl.prepare_filename(info).replace("webm", "wav")

        return audio_filename
    pass

def download_model(size):
    os.system(f"cd whisper.cpp && make {size}")


if not whispercpp_installed():
    print("Whispercpp not downloaded. Downloading now.")
    download_whispercpp()

download_model("small")
filename = download_video("https://www.youtube.com/watch?v=FgX5mGCnt64")
run_model(filename, "small")
