## Setup Text to Speech-TTS-model with ElevenLabs
import os
import subprocess
import platform
from playsound import playsound
import elevenlabs
from elevenlabs.client import ElevenLabs

gtts_input_text="Hi this is Vaibhav"

## Setup Text to Speech-TTS-model with ElevenLabs
ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")

## Use model for Text output to Voice
def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "George",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    playsound(output_filepath)
    os.remove(output_filepath)

#text_to_speech_with_elevenlabs(gtts_input_text, output_filepath="elevenlabs_autoplay_testing.mp3")