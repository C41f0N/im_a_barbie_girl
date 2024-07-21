import ctypes
import struct
import os
from pynput.keyboard import Key, Controller
import winsound
import time
import threading
import sys
from shutil import copyfile
import os;
import pathlib


keyboard = Controller()

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def playAudio(audioFile):
	while True:
		time.sleep(0.05)
		winsound.PlaySound(resource_path(audioFile), winsound.SND_FILENAME)

def increaseVolume():
	while True:
		time.sleep(0.01)
		keyboard.press(Key.media_volume_up)

imagePath = "image.jpg"
audioPath = "audio.wav"

SPI_SETDESKWALLPAPER = 20

def is_64bit_windows():
    return struct.calcsize('P') * 8 == 64


if __name__ == "__main__":    
	volumeThread = threading.Thread(target=increaseVolume)
	audioThread = threading.Thread(target=playAudio, args=(audioPath,))

	if (is_64bit_windows()):
	    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, resource_path(imagePath), 3)
	else:
	    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, resource_path(imagePath), 3)

	volumeThread.start()
	audioThread.start()

	volumeThread.join()
	audioThread.join()
    

    

    
    

