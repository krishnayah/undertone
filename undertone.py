import os

def whispercpp_installed():
    # determines if whispercpp is available.
    return os.path.exists("whisper.cpp")
    pass

def download_whispercpp():
    # https://github.com/ggerganov/whisper.cpp
    # downloads whispercpp
    os.system("git clone https://github.com/ggerganov/whisper.cpp.git")
def is_apple_silicon():
    pass

def run_model(audio):
    pass

def download_video(url):
    # downloads a video, converts to Wav 16k and returns the filepath
    pass

def download_model(size):
    os.system(f"cd whisper.cpp && make {size}")

def make_model(size):
    pass



if not whispercpp_installed():
    print("Whispercpp not downloaded. Downloading now.")
    download_whispercpp()

download_model("small")
os.system("cd whisper.cpp && make -j && ./main -m ./models/ggml-small.bin -f ./samples/jfk.wav -t 16")
