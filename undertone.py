import os

def install_dependencies():
    # installs all dependencies
    # run command pip install
    os.system("python3 -m pip install ane_transformers")
    os.system("python3 -m pip install openai-whisper")
    os.system("python3 -m pip install coremltools")

    pass
def whispercpp_installed():
    # determines if whispercpp is available.
    return os.path.exists("whisper.cpp")
    pass

def download_whispercpp():
    # https://github.com/ggerganov/whisper.cpp
    # downloads whispercpp
    os.system("git clone https://github.com/ggerganov/whisper.cpp.git")



def coreml_model_available(size):
    # determines if a given model is available
    return os.path.exists(f'./whisper.cpp/models/ggml-{size}.en-encoder.mlmodelc')

def is_apple_silicon():
    pass

def generate_coreml_model(size):
    os.system(f"./whisper.cpp/models/generate-coreml-model.sh {size}.en")
    pass

def build_whispercpp_coreml():
    os.system("cd whisper.cpp && make clean && WHISPER_COREML=1 make -j")
    pass

def run_model(audio):
    pass

def download_video(url):
    # downloads a video, converts to Wav 16k and returns the filepath
    pass

download_whispercpp()
