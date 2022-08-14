from project import check_input, create_gif, check_imageExist, convert_gif2vid, generate_audio, add_aud2vid
import pytest

def main():
    test_check_input()
    test_create_gif()
    test_check_imageExist()
    test_convert_gif2vid()
    test_generate_audio()
    test_add_aud2vid()

def test_check_input():
    assert check_input("hello") == True
    assert check_input("hello there") == True
    assert check_input(" hello    there how are you   ") == True
    assert check_input("Hello THERE") == True
    with pytest.raises(ValueError):
        check_input("1234")
    with pytest.raises(ValueError):
        check_input("hey there!")
    with pytest.raises(ValueError):
        check_input("welcome to CS50")
    with pytest.raises(ValueError):
        check_input("my email is xyz@abc.com")

def test_create_gif():
    assert create_gif("hello") == "animation.gif"
    assert create_gif("hey   there") == "animation.gif"
    assert create_gif("  hello THEre  ") == "animation.gif"

def test_check_imageExist():
    assert check_imageExist("a.jpg") == "a.jpg"
    assert check_imageExist("fv.jpg") == "fv.jpg"
    with pytest.raises(FileNotFoundError):
        check_imageExist("hello.jpg")
    with pytest.raises(FileNotFoundError):
        check_imageExist("a.png")

def test_convert_gif2vid():
    assert convert_gif2vid("animation.gif") == "animation.mp4"

def test_generate_audio():
    assert generate_audio("hello") == "audio.mp3"
    assert generate_audio("my name is") == "audio.mp3"
    assert generate_audio("hey THERE") == "audio.mp3"

def test_add_aud2vid():
    assert add_aud2vid("animation.mp4","audio.mp3") == "final_output.mp4"

if __name__ == "__main__":
    main()