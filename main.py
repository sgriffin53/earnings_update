import pygetwindow as gw
import pyperclip
import pyautogui
import time
import playsound

def get_page_content():
    # Get the list of all open Firefox windows
    firefox_windows = [win for win in gw.getAllWindows() if "Mozilla Firefox" in win.title]

    # Iterate through the Firefox windows
    for win in firefox_windows:
        # Activate the window
        win.activate()
      #  time.sleep(2)  # Wait for the window to become active
        #new_content = ''
        # Check the title of the active window
        if "eBay Partner Network" in win.title:
            # Use the keyboard shortcut to select all content (Ctrl+A)
            pyautogui.hotkey('ctrl', 'a')  # Select all content
            time.sleep(0.5)  # Wait for the selection to take effect

            # Use the keyboard shortcut to copy the selected content (Ctrl+C)
            pyautogui.hotkey('ctrl', 'c')  # Copy content
            time.sleep(0.5)  # Wait for the copy to complete

            # Retrieve the copied content from the clipboard
            page_content = pyperclip.paste()
            new_content = ''
            lines = page_content.split("\n")
            for line in lines:
                line = line.replace("\r","")
                if "£" in line:
                    new_content += line
            return new_content

    return "No tab found with 'eBay Partner Network' in the title."


# Get and print the page content
last_content = ''
while True:
    content = get_page_content()
    print(content)
    if content != last_content:
        if last_content != '': playsound.playsound('cha-ching-7053.mp3')
    last_content = content
    time.sleep(200)