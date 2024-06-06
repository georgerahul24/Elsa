import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"


# List available 🐸TTS models

text = """he Rise of Artificial Creativity: Boon or Bane for the Human Artist?
The landscape of art is undergoing a seismic shift. Artificial intelligence (AI) is no longer relegated to science fiction; it's actively shaping the creative process. From composing music to generating paintings, AI tools are blurring the lines between human and machine creation. This essay explores the burgeoning realm of artificial creativity, delving into its potential benefits and drawbacks for the human artist.

Firstly, AI presents a powerful tool for artistic exploration and augmentation. Generative algorithms can produce vast quantities of unique content, serving as a springboard for human inspiration. Imagine a painter struggling with a color palette; an AI could generate thousands of potential combinations, sparking a new direction for the artwork. Similarly, a composer facing writer's block could utilize AI to create musical snippets, melodies, or chord progressions, igniting a fresh creative spark.

Furthermore, AI can democratize art creation. Tools that can translate text into images or generate music based on user preferences, empower anyone to become an "artist" in some capacity. This fosters artistic expression and engagement on a wider scale. Additionally, AI can assist with tedious aspects of the creative process, such as image editing or music composition tasks. This frees human artists to focus on higher-level aspects like concept development and emotional depth.

However, the rise of AI also raises concerns about the future of human creativity. With machines capable of generating high-quality art, there's a fear of human artists becoming obsolete. The very essence of art, its originality and emotional resonance, seems threatened by the calculated precision of algorithms.

Moreover, the reliance on AI could stifle creative growth. When faced with the ease of generating content with AI, artists may neglect the development of their own skills and unique styles. The struggle inherent in the creative process, often a catalyst for innovation, might be bypassed, leading to a homogenization of artistic expression.

Furthermore, the role of the artist as an interpreter of the human experience could be diminished. Art has always served as a mirror reflecting society's emotions, anxieties, and aspirations. Can AI, devoid of human experience, truly capture and convey these intricacies? The authenticity and emotional impact of art created solely by machines remains a question.

It's crucial to recognize that AI is not here to replace human artists. Instead, it should be viewed as a powerful collaborator, a tool to augment and enhance human creativity.  The future lies in a symbiotic relationship – artists harnessing the power of AI to push boundaries and explore new avenues, while retaining their unique human perspective to imbue art with soul and meaning.

To ensure a future where both human and AI-generated art flourish, several strategies can be employed. Firstly, fostering an understanding of AI's limitations is vital. AI can generate beautiful and innovative content, but it lacks the ability to understand and express human emotions.

Secondly, promoting artistic education remains crucial. Encouraging individuals to develop their own creative skills ensures a future with diverse artistic voices, both human and machine-generated.

Finally, fostering critical thinking around AI art is essential. We must learn to appreciate AI art for its unique qualities, while recognizing and valuing the distinct contribution of human artists.

In conclusion, the rise of artificial creativity signifies a transformative era for art. While AI poses challenges to traditional artistic practices, it also presents unparalleled opportunities. Through collaboration and a nuanced understanding of both human and machine capabilities, we can foster a future where art thrives in its most diverse and expressive forms. After all, the human spirit continues to crave creativity, and AI offers a powerful tool to expand its artistic horizons."""

text1 = "My name is Elsa!"

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)


# Run TTS
def talk(text):
    tts.tts_to_file(text=text,
                    file_path="output.wav",
                    speaker="Ana Florence",
                    language="en",
                    split_sentences=True
                    )



talk(text)
talk(text1)
