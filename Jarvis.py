import os
import tempfile
from dotenv import load_dotenv
from openai import OpenAI
from gtts import gTTS

# Load API key
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    print("❌ API key missing! Create a .env file with your API key.")
    exit()

client = OpenAI(api_key=API_KEY)

# Voice output
def speak(text):
    tts = gTTS(text, lang='ur')
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as fp:
        tts.save(fp.name)
        os.system(f"mpv --no-video {fp.name}")

# AI reply
def ai_reply(message):
    resp = client.responses.create(
        model="gpt-4.1-mini",
        input=f"Reply in Urdu + English:\n{message}"
    )
    return resp.output_text

print("Jarvis ready! Type 'exit' to quit.")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        speak("Goodbye sir. Jarvis off ho raha hai.")
        break
    reply = ai_reply(user)
    print("Jarvis:", reply)
    speak(reply)
