from transformers import pipeline
from gtts import gTTS
from deep_translator import GoogleTranslator  # Updated translation library
import os

# Initialize HuggingFace story generator and translator
story_generator = pipeline("text-generation", model="gpt2")

# Languages: name => gTTS language code
languages = {
    "english": "en",
    "hindi": "hi",
    "bengali": "bn",
   
    # Add more if needed
}

# Generate short story in English
def generate_english_story(topic="bedtime story for kids"):
    prompt = f"Write a short, creative, family-friendly {topic} in English. Keep it under 80 words."
    result = story_generator(prompt, max_length=100, num_return_sequences=1)
    story = result[0]['generated_text'].strip()
    return story

# Translate and save text + voice
def translate_and_save(story_en, lang_name, lang_code):
    # Translate story using deep_translator
    translated = GoogleTranslator(source='en', target=lang_code).translate(story_en)
    
    # Save text file
    with open(f"story_{lang_code}.txt", "w", encoding="utf-8") as f:
        f.write(translated)
    
    # Generate voice
    tts = gTTS(text=translated, lang=lang_code)
    tts.save(f"story_{lang_code}.mp3")
    print(f"[✅] Saved story in {lang_name.title()} as story_{lang_code}.mp3 & story_{lang_code}.txt")

def main():
    print("\n🎬 Generating multilingual stories and voices...")
    
    story_en = generate_english_story()
    print("\n[🔤] English Story:\n", story_en)

    for lang_name, lang_code in languages.items():
        translate_and_save(story_en, lang_name, lang_code)

    print("\n✅ All done! You now have story text + voice files in multiple languages.")

if __name__ == "__main__":
    main()
