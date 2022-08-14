# **Face Animation Generator**

### ****Video Demo****:  [Link to my project video on youtube](https://youtu.be/kW5syxT6F_M)


![](https://github.com/thebotgirl99/CS50-Python/blob/main/m.jpg)


## **Description**:
My CS50P final project is about generating facial animations (in an mp4 format) with lip-synced mouth movements according to any audio or text input.

Now a days, we see many social robots in the industry. The main feature of a social robot is it's face. The more realistic and humanoid the face, the better the user acceptance of the robot. Research has proven that cute Disney-like facial features, typically big eyes, no nose and cute mouth movements have had the highest ratings in terms of how users wanted a social robot's face to look like. Having a digital animated face is low-cost and has more flexibility when compared to having physical facial features on a robot. But the process of creating life-like real time animated faces can be tiresome and difficult for a designer. Hence, I have focused on automating the process of generating facial lip-synced animation videos based on the user's input text/audio.

This project is useful especially when a user wants to interact with a robot real-time. Here, when a user types in an input, for example, "Hello World", a video is generated as an output which consists of the face of a robot lip-syncing to the text along with the audio. This project can be further used to include real-time voice recognition (using the speech recognition modules in python) to not only accept text as input but to convert user's speech into text (speech to text) in real-time.

## **Pre-requisties**:
Prior to running "project.py", certain libraries have to be installed (python version 3.10.5). Given below are the list of libraries required:

```
pip install Pillow
pip install moviepy
pip install gTTS
pip install regex
```

The Pillow module is required to read the input images and generate an animated GIF. The moviepy module is responsible for converting the generated GIF to an mp4-format file (video file). The gTTS ( Google's Text to Speech) module is used to generate audio in the preferred language (I have used US English) based on the text input given by the user and finally, the regex module takes care of any unwanted user input formats (exceptions) - for example, when a user inputs "Hello world 123!" (which is an invalid input format).

I have included ten input images [(click here to download)](https://github.com/thebotgirl99/CS50-Python) in my project directory which represent different phonetics and alphabets. For example, there is an image that represents sounds or letters like "f" and "v". These input images have to be downloaded to your project directory prior to executing "project.py".

## **Main Code Explanation**:
To execute the code run:
```
python project.py
```

1. main() - We first start with a main() function to initialize the other six functions.
2. check_input() - This function validates the user input and raises a ValueError if the user's input is invalid. E.g Valid input = "Hello there"; Invalid input = "my name is @123!".
3. create_gif() - This function returns an "animation.gif" file after reading the user's input and matching the sounds/letters to the respective phonetic images.
4. check_imageExist() - This function validates whether we have all the required (nine) images in our directory. If not, it raises a FileNotFoundError.
5. convert_gif2vid() - This function converts "animaiton.gif" to an mp4 format, "animation.mp4".
6. generate_audio() - This function returns an audio (mp3) file after converting the user's text input to speech as "audio.mp3"
7. add_aud2vid() - This function adds the mp3 audio to the mp4 video file generated and returns the final output video in an mp4 format as "final_output.mp4"

I have named my functions in a reader-friendly way so that anyone who wants to replicate this code can understand and improvise easily. After running "project.py", you will have four output files in your directory, namely - "animation.gif", "animation.mp4", "audio.mp3" and "final_output.mp4".

Though this code might looks and sound a bit easy to understand, it can act as a powerful platform for robotic designers.

## **Testing Code**:
To test the code, run:
```
pytest test_project.py
```
The "test_project.py" file successfully tests the different kinds of user inputs the computer can expect. It also catches exceptions like ValueErrors and FileNotFoundErrors. Though I have added quite a few assertions, you can add as many examples as you want to the file. (The more, the better!😁)

## **Closing Note**:
I thoroughly enjoyed my CS50P learning experience thanks to Dr.David Malan @Harvard! Any of you who want to start somewhere in the world of coding, I highly recommend CS50X. Adios!😄

### **Libraries Used**:
- PIL (pillow)
- moviepy.editor (moviepy)
- gtts
- sys
- re (regex)



