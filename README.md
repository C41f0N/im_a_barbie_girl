# im_a_barbie_girl

A python script that changes your wallpaper and plays the iconic song "I'm a barbie girl" forcefully at full volume every five minutes.

![image](https://github.com/user-attachments/assets/ca9e57d9-4cb1-410c-b8b9-c2f6bde00895)

## Requirements
`pip install -r requirements.txt`

## Compile
Install pyinstaller `pip install pyinstaller`

Then compile into an executable with `pyinstaller --onefile --add-data "image.jpg;." --add-data "audio.wav;." __main__.py`
