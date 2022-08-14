from PIL import Image
import moviepy.editor as mp
from gtts import gTTS
import sys
import re

def main():
    text = input("Enter text to generate animation: ").strip().lower()
    try:
        if check_input(text):
            gif = create_gif(text)
            mp4 = convert_gif2vid(gif)
            mp3 = generate_audio(text)
            add_aud2vid(mp4,mp3)
    except ValueError:
        sys.exit("Invalid user input, try again☹️")
    except FileNotFoundError:
        sys.exit("Image does not exist in your folder, try again☹️")

def check_input(text):
    matches = re.findall(r"[0-9_!@#$%^&*()-=+{}[]|\:\";\'<>?,./]+",text)
    if not matches and len(text) != 0:
        return True
    else:
        raise ValueError()

def create_gif(text):
    images = []
    for c in text:
        if c == "a":
            image = Image.open(check_imageExist("a.jpg"))
            images.append(image)
        elif c in ["b", "e", "g", "p", "x"]:
            image = Image.open(check_imageExist("begpx.jpg"))
            images.append(image)
        elif c in ["c", "d", "h", "j", "k", "s", "t", "z"]:
            image = Image.open(check_imageExist("cdhjkstz.jpg"))
            images.append(image)
        elif c in ["f", "v"]:
            image = Image.open(check_imageExist("fv.jpg"))
            images.append(image)
        elif c in ["i", "y"]:
            image = Image.open(check_imageExist("iy.jpg"))
            images.append(image)
        elif c in ["l", "n", "r"]:
            image = Image.open(check_imageExist("lnr.jpg"))
            images.append(image)
        elif c == "m":
            image = Image.open(check_imageExist("m.jpg"))
            images.append(image)
        elif c == "o":
            image = Image.open(check_imageExist("o.jpg"))
            images.append(image)
        elif c in ["q", "u", "w"]:
            image = Image.open(check_imageExist("quw.jpg"))
            images.append(image)
        else:
            image = Image.open(check_imageExist("m.jpg"))
            images.append(image)

    neut = [Image.open("closed.jpg"), Image.open("m.jpg")]
    images[0].save("animation.gif", format="GIF", append_images=images+neut, save_all=True, duration=105, loop=1)
    return "animation.gif"

def check_imageExist(name):
    if Image.open(name):
        return name
    else:
        raise FileNotFoundError()

def convert_gif2vid(gif):
    clip = mp.VideoFileClip(gif)
    clip.write_videofile("animation.mp4")
    return "animation.mp4"

def generate_audio(text):
    myobj = gTTS(text= text, lang= "en")
    myobj.save("audio.mp3")
    return "audio.mp3"

def add_aud2vid(mp4,mp3):
    video = mp.VideoFileClip(mp4)
    audio = mp.AudioFileClip(mp3)
    final_output = video.set_audio(audio)
    final_output.write_videofile("final_output.mp4")
    return "final_output.mp4"

if __name__ == "__main__":
    main()