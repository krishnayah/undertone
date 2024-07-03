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

# Clones whispercpp and makes the main file with default options
def download_whispercpp():

    os.system("git clone https://github.com/ggerganov/whisper.cpp.git")
    os.system("cd whisper.cpp && make -j")


# This runs the whisper.cpp model bindings on the audio file, and saves the output to the output folder
def run_model(audio, size):
    os.system(f"cd whisper.cpp && ./main -m ./models/ggml-{size}.bin -f '../{audio}' -t 8 -olrc -of ../output/{audio.split('/')[-1]}")

    pass

def download_video(url):
    # downloads a video, converts to Wav 16k and returns the filepath
    with yt_dlp.YoutubeDL(ytdlp_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        audio_filename = ydl.prepare_filename(info).replace("webm", "wav")

        return audio_filename
    pass

def download_model(size):
    if os.path.exists(f"whisper.cpp/models/ggml-{size}.bin"):
        print(f"Model {size} already downloaded.")
    else:
        os.system(f"cd whisper.cpp && ./models/download-ggml-model.sh {size} && make {size}")

# This will run when the file is imported from main.py.
if not whispercpp_installed():
    print("Whispercpp not downloaded. Downloading now.")
    download_whispercpp()

