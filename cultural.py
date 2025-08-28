api_key = "AIzaSyCa_ImbOTlZdnv7rRFJX7nxjjmlXK5rHhk"
import google.generativeai as genai
import os

# 🔑 Configure Gemini
genai.configure(api_key=api_key)

# 🧠 Story Generator Function
def generate_story(mythology , specific_story , lang = 'english'):
    # Use the latest available model that supports generateContent
    model = genai.GenerativeModel("gemini-1.5-flash-latest")
    prompt = f"""
    You are a master cultural storyteller, speaking directly to a human listener. 
    Your goal is to create a vivid, immersive story inspired by mythology.

    User Input:
    - Mythology: {mythology} (e.g., Hindu, Greek, Norse, Egyptian)
    - Specific Story/Character (optional): {specific_story}
    - Language: {lang}

    Instructions:
    1. Narrate as if you are telling the story to a live audience—engaging, warm, and emotionally connected.
    2. If a specific story/character is given, honor its cultural roots and essence while adding vivid details and stick to the story if given.
    3. If no specific story is provided, craft an original tale deeply inspired by the chosen mythology.
    4. Make the story:
       - Richly descriptive with sensory details (sights, sounds, emotions).
       - Filled with cultural authenticity, character depth, and natural dialogues.
       - Structured like a true oral narrative: a welcoming opening, rising events, a powerful climax, and a satisfying resolution.
    5. Reflect the tone and themes of the chosen mythology (e.g., moral wisdom for Hindu, grand heroism for Greek, fate and honor for Norse).
    6. Conclude by gently summarizing the core lesson or moral in a way that feels personal and reflective.
    7. Output the full story in {lang}.

    Begin the story as though you are sitting by a fire, speaking directly to the listener.

    at the end also give the moral teachings and learnings form the story


  """

    response = model.generate_content(prompt)
    return response.text

# 🔊 Convert Story to MP3


# 🖥️ Console Input
def main():
    print("\n📘 Welcome to the Gemini Smart Storyteller\n")

    # name = input("Enter hero's name: ")
    # traits = input("Enter hero's traits (comma separated): ")
    # genre = input("Enter genre (e.g., Fantasy, Sci-Fi, Horror): ")
    specific_story = input("Enter a brief plot idea: ")
    mythology = input("Enter a brief mythology idea: ")
    # lang = "Hindi"

    print("\n⏳ Generating your story...\n")
    story = generate_story(mythology=mythology , specific_story=specific_story)

    print("📖 Here's your story:\n")
    print(story)

    print("\n🔊 Converting story to audio...")
    # audio_file = text_to_speech(story)

    print(f"✅ Done! Story saved as text and audio.\n📄 Text saved to screen.\n")


    with open(f"{mythology}_story.txt", "w", encoding="utf-8") as f:
        f.write(story)

if __name__ == "__main__":
    main()