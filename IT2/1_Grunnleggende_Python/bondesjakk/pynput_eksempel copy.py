# I terminalen:
# pip install pynput

from pynput import keyboard
from pynput.keyboard import Key

def flush_input():
    try: # Windows
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError: # MacOS / Linux
        import sys, termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def on_key_release(key):
  if key == Key.right:
    print("Right key clicked")
    flush_input()
    svar1 = input("Hva kommer nå? ")
    print(svar1)
  elif key == Key.left:
    print("Left key clicked")
    svar2 = input("Hva kommer nå? ")
    print(svar2)
  elif key == Key.up:
    print("Up key clicked")
  elif key == Key.down:
    print("Down key clicked")
  elif key == Key.space:
    print("Space key clicked")
  elif key == Key.esc:
    exit()
  elif key != Key.enter:
    try:
      print(key.char)
    except:
      print("ikke en bokstav")

with keyboard.Listener(on_release=on_key_release) as listener:
  listener.join()
