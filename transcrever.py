import whisper
import os

model = whisper.load_model("base")

audio_folder = "audios"

for filename in os.listdir(audio_folder):
    if filename.endswith((".mp3", ".wav", ".m4a")):
        path = os.path.join(audio_folder, filename)
        print(f"Transcrevendo {filename}...")
        result = model.transcribe(path)
        print(result["text"])
