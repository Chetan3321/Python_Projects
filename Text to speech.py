import pyttsx3

def text_to_speech(text, filename="output.mp3", speed=150, voice_index=1):
    engine = pyttsx3.init()
    
    # Set speech rate
    engine.setProperty('rate', speed)
    
    # Set voice (0 for male, 1 for female)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_index].id)
    
    # Speak the text
    engine.say(text)
    
    # Save to file
    engine.save_to_file(text, filename)
    
    # Run engine
    engine.runAndWait()
    print(f"Speech saved as {filename}")

# Example usage
text_to_speech("Hello! This is a complete text-to-speech script.", "speech.mp3", speed=130, voice_index=1)
