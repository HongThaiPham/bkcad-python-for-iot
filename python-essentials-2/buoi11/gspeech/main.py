from gtts import gTTS
from IPython.display import Audio
from playsound import playsound

# tts = gTTS('Xin chào các bạn, mình là trợ lý ảo google đây.',
#            lang='vi', slow=True)

# tts.save('hello.mp3')
# wn = Audio("hello.mp3", autoplay=True)


def text_to_speech(text, lang='en'):
    tts = gTTS(text, lang=lang)
    name = 'word_' + lang + '.mp3'
    tts.save(name)
    playsound(name)


def speech_input():
    word = input("Nhap vao 1 tu: ")
    lang = input("Nhap vao ngon ngu: (en, vi): ")
    text_to_speech(word, lang)


def speech_from_file(filename):
    try:
        f = open(filename, "r")
        text = f.read()
        text_to_speech(text)
    except Exception as e:
        print(e)


# speech_input()
speech_from_file("demofile.txt")
