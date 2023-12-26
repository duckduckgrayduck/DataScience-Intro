import pyautogui
import time

def open_notepad():
    # Open Notepad (or any other text editor)
    pyautogui.hotkey('win', 'r')  # Open the Run dialog
    time.sleep(1)
    pyautogui.write('notepad')  # Type 'notepad' and press Enter
    pyautogui.press('enter')
    time.sleep(2)  # Wait for Notepad to open

def type_message(message):
    # Type a predefined message
    pyautogui.write(message)
    
def save():
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.write('hello.txt')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

if __name__ == "__main__":
    # Open Notepad
    open_notepad()
    
    # Type a message
    message_to_type = "Hello, this is a PyAutoGUI automation example!"
    type_message(message_to_type)
    
    # Save the document
    save()
