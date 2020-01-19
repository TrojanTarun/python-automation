# Get the wallpaper from the internet
# Save it to a temp directory
# Set the wallpaper
# Automation of wallpapers

import os
import ctypes
import requests
import wget
import subprocess
import time

def get_wallpaper():
	access_key = os.environ.get('UNSPLASH_ACCESS_KEY')
	url = 'https://api.unsplash.com/photos/random?client_id=' + access_key
	params = {
		'query': 'HD wallpapers',
		'orientation': 'landscape'
	}

	response = requests.get(url, params=params).json()
	image_source = response['urls']['full']

	image = wget.download(image_source, 'tmp/wallpaper.jpg')
	return image

def change_wallpaper():
    wallpaper = get_wallpaper()
    cmd = """/usr/bin/osascript<<END
    tell application "Finder"
    set desktop picture to POSIX file "%s"
    end tell
    END"""
    #cmd=ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER , SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
    subprocess.Popen(cmd%wallpaper, shell=True)
    subprocess.call(["killall Dock"], shell=True)

def main():
	try:
		while True:
			change_wallpaper()
			time.sleep(10)

	except KeyboardInterrupt:
		print("\nHope you like this one! Quitting.")
	except Exception :
		pass
	

if __name__ == "__main__":
	main()
