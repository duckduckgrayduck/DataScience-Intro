import subprocess # https://docs.python.org/3/library/subprocess.html
import time
import pyautogui # https://pyautogui.readthedocs.io/en/latest/

def open_text_editor():
    subprocess.Popen(['gedit'])
    time.sleep(2)

def type_message(message):
    subprocess.run(['xdotool', 'search', '--onlyvisible', '--class', 'gedit', 'windowactivate'])
    time.sleep(1)
    pyautogui.write(message)
    time.sleep(1)

def save_document():
    # Simulate keypresses to save the document
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.write('hello.txt')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

if __name__ == "__main__":
    # Open text editor
    open_text_editor()

    # Type a message
    message_to_type = "Hello, this is a PyAutoGUI automation example on Linux!"
    type_message(message_to_type)

    # Save the document
    save_document()
