import winsound, os

soundDir = "C:/Users/Morgan/Documents/Programming/Python Code/Sound"
os.chdir(soundDir)
winsound.PlaySound("gameover",winsound.SND_FILENAME)
