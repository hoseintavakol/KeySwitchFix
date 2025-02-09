# import keyboard
import pyperclip
import time
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
import os
# import sys
import threading
import win32api
import win32con
import win32gui
import json
import subprocess



class HotkeyManager:
    def __init__(self, config_file="config.json"):
        self.HOTKEY_ID = 1
        self.config_file = config_file
        # self.user32 = ctypes.WinDLL('user32', use_last_error=True)
        self.modifiers = None
        self.key_code = None

        # بارگذاری هات‌کی از فایل و ثبت آن
        self.load_hotkey_from_file()
        if self.modifiers and self.key_code:
            self.register_hotkey(self.modifiers, self.key_code)
        else:
            print("هیچ هات‌کی ثبت نشده است.")
            change_hotkey(None, None)

        # ثبت تابع آزادسازی هات‌کی در هنگام خروج
        # atexit.register(self.unregister_hotkey)

    # # registering with ctypes
    # def register_hotkey(self, modifiers, key_code):
    #     """ثبت هات‌کی"""
    #     self.unregister_hotkey()  # حذف هات‌کی قبلی
    #     if not self.user32.RegisterHotKey(None, self.HOTKEY_ID, modifiers, key_code):
    #         print(f"خطا در ثبت هات‌کی: {ctypes.get_last_error()}")
    #     else:
    #         print(f"هات‌کی ثبت شد: modifiers={modifiers}, key_code={key_code}")

    def register_hotkey(self, modifiers, key_code):
        # unregister_hotkey()
        try:
            win32gui.RegisterHotKey(None, self.HOTKEY_ID, modifiers, key_code)
            print(f"هات‌کی ثبت شد: {modifiers} + {chr(key_code)}")
        except Exception as e:
            print(f"خطا در ثبت هات‌کی: {e}")

    # def unregister_hotkey(self):
    #     """حذف هات‌کی"""
    #     if not self.user32.UnregisterHotKey(None, self.HOTKEY_ID):
    #         error_code = ctypes.get_last_error()
    #         if error_code != 0:  # اگر خطایی وجود داشته باشد
    #             print(f"خطا در حذف هات‌کی: {error_code}")

    def load_hotkey_from_file(self):
        """بارگذاری هات‌کی از فایل تنظیمات"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r") as file:
                    config = json.load(file)
                    self.modifiers = config.get("modifiers")
                    self.key_code = config.get("key_code")
                    print("هات‌کی از فایل بارگذاری شد:", config)
            except Exception as e:
                print("خطا در خواندن فایل تنظیمات:", e)

    # def save_hotkey_to_file(self, modifiers, key_code):
    #     """ذخیره هات‌کی در فایل تنظیمات"""
    #     try:
    #         with open(self.config_file, "w") as file:
    #             json.dump({"modifiers": modifiers, "key_code": key_code}, file)
    #             print(f"هات‌کی در فایل ذخیره شد: modifiers={modifiers}, key_code={key_code}")
    #     except Exception as e:
    #         print("خطا در ذخیره فایل تنظیمات:", e)

    def listen_for_hotkey(self):
        """حلقه دریافت پیام‌ها"""
        print("در حال دریافت پیام‌ها...")
        try:
            while True:
                msg = win32gui.GetMessage(None, 0, 0)
                if msg[1][1] == win32con.WM_HOTKEY and msg[1][2] == self.HOTKEY_ID:
                    print("هات‌کی فشرده شد!")
                    check_clipboard_and_process()
                    time.sleep(0.5)
                win32gui.TranslateMessage(msg[1])
                win32gui.DispatchMessage(msg[1])
                time.sleep(0.02)
        except Exception as e:
            print(f"خطای دریافت پیام هات‌کی: {e}")
        # finally:
        #     self.unregister_hotkey()




# import winreg as reg

# Virtual-Key Codes: learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
def ctrl_c_with_win32api():
    # press ctrl
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
    # press c
    win32api.keybd_event(0x43, 0, 0, 0)
    # release c
    win32api.keybd_event(0x43, 0, win32con.KEYEVENTF_KEYUP, 0)
    # release ctrl
    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)


def ctrl_v_with_win32api():
    # press ctrl
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
    # press v
    win32api.keybd_event(0x56, 0, 0, 0)
    # release v
    win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)
    # release ctrl
    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)


def ctrl_a_with_win32api():
    # press ctrl
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
    # press a
    win32api.keybd_event(0x41, 0, 0, 0)
    # release a
    win32api.keybd_event(0x41, 0, win32con.KEYEVENTF_KEYUP, 0)
    # release ctrl
    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)


def alt_shift_with_win32api():
    # press alt
    win32api.keybd_event(win32con.VK_MENU, 0, 0, 0)
    # press shift
    win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
    # release shift
    win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
    # release alt
    win32api.keybd_event(win32con.VK_MENU, 0, win32con.KEYEVENTF_KEYUP, 0)


def create_image():
    img = Image.new('RGBA', (100, 100), (255, 255, 255, 0))  # Create a transparent background
    draw = ImageDraw.Draw(img)

    # Define the coordinates and size of the rectangles
    square_size = 58
    x1, y1 = 38, 12
    x2, y2 = x1 + square_size, y1 + square_size

    # Draw a rectangle with rounded corners and a white shadow
    draw.rounded_rectangle([(x1, y1), (x2, y2)], radius=14, outline='black', width=10)
    for i in range(1):  # Create one pixel shadow on each side
        draw.rounded_rectangle([(x1 - i, y1 - i), (x2 + i, y2 + i)], radius=15, outline='white', width=1)

    # Draw the second rectangle
    x1, y1 = 12, 38
    x2, y2 = x1 + square_size, y1 + square_size
    draw.rounded_rectangle([(x1, y1), (x2, y2)], radius=14, outline='black', width=10)
    for i in range(1):
        draw.rounded_rectangle([(x1 - i, y1 - i), (x2 + i, y2 + i)], radius=15, outline='white', width=1)

    return img


# def add_to_startup():
#     # اضافه کردن برنامه به Startup
#     if getattr(sys, 'frozen', False):
#         # وقتی که برنامه به باینری تبدیل شده
#         file_path = sys.executable
#     else:
#         file_path = os.path.abspath(__file__)
#
#     key = reg.HKEY_CURRENT_USER
#     key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
#
#     open_key = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
#     reg.SetValueEx(open_key, "TextConverterApp", 0, reg.REG_SZ, file_path)
#     reg.CloseKey(open_key)
#
# def remove_from_startup():
#     # حذف برنامه از Startup
#     key = reg.HKEY_CURRENT_USER
#     key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
#
#     open_key = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
#     reg.DeleteValue(open_key, "TextConverterApp")
#     reg.CloseKey(open_key)


def on_quit(icon, item):
    icon.stop()
    os._exit(0)  # Forcefully exit the application

def change_hotkey(icon, item):
    # اجرای باینری GUI به صورت مستقل
    subprocess.Popen(
        ["SettingsKeySwitchFix.exe"],
        creationflags=subprocess.DETACHED_PROCESS
    )

def setup_tray():

    # System tray icon and menu
    icon = pystray.Icon("name", create_image(), "KeySwitchFix", menu=pystray.Menu(
        # item('Enable on Startup', lambda: add_to_startup(), default=False),
        # item('Disable on Startup', lambda: remove_from_startup()),
        item('Change Hotkey', lambda: change_hotkey(None, None)),
        item('Quit', lambda: on_quit(icon, item))
    ))
    icon.run()


# Conversion dictionary
fa_to_en = {
    'ض': 'q', 'ص': 'w', 'ث': 'e', 'ق': 'r', 'ف': 't', 'غ': 'y', 'ع': 'u', 'ه': 'i', 'خ': 'o', 'ح': 'p',
    'ج': '[', 'چ': ']', 'ش': 'a', 'س': 's', 'ی': 'd', 'ب': 'f', 'ل': 'g', 'ا': 'h', 'ت': 'j', 'ن': 'k',
    'م': 'l', 'ک': ';', 'گ': "'", 'ظ': 'z', 'ط': 'x', 'ز': 'c', 'ر': 'v', 'ذ': 'b', 'د': 'n', 'پ': 'm',
    'و': ',', '؟': '/', ' ': ' ', '\n': '\n', '\t': '\t',
    'آ': 'H', 'ژ': 'C'  # Letters that are written with a shift and a key.
    # Here shift + key is considered to English uppercase letters
}

capitalletter_to_small = {  # The rest of the English uppercase letters are converted to
    # lowercase letters before conversion
    'Q': 'q', 'W': 'w', 'E': 'e', 'R': 'r', 'T': 't', 'Y': 'y', 'U': 'u', 'I': 'i', 'O': 'o', 'P': 'p',
    'A': 'a', 'S': 's', 'D': 'd', 'F': 'f', 'G': 'g', 'J': 'h', 'K': 'k',
    'L': 'l', 'Z': 'z', 'X': 'x', 'V': 'v', 'B': 'b', 'N': 'n', 'M': 'm', '’': "'"
}

en_to_fa = {v: k for k, v in fa_to_en.items()}
small_to_capitalletter = {v: k for k, v in capitalletter_to_small.items()}


# Identify the language of the selected text
def detect_language(text):
    english_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]',’;"
    for letter in text[:3]:  # Check the first three letters
        if letter in english_letters:
            return "en"
    return "fa"


# core Text conversion function
def transcript_text(text):
    lang = detect_language(text)
    if lang == "fa":
        return ''.join(fa_to_en.get(char, char) for char in text)
    else:
        text = ''.join(capitalletter_to_small.get(char, char) for char in text)
        return ''.join(en_to_fa.get(char, char) for char in text)


# A function that detects whether text is highlighted or not.
# If it is highlighted, the same text will be processed, otherwise, the entire text will be selected with ctrl A.
def check_clipboard_and_process():
    time.sleep(0.2)
    # Enter the text in the clipboard
    original_text = pyperclip.paste()
    # Copy new text
    # keyboard.send('ctrl+c')
    ctrl_c_with_win32api()
    time.sleep(0.1)  # delay to ensure the new text is copied to the clipboard
    # Enter the copied text (if available)
    new_text = pyperclip.paste()

    # Checking if two entered texts are equal. If they are equal, then there is no highlighted text.
    if new_text != original_text:
        process_text()
    else:
        # keyboard.send('ctrl+a')
        ctrl_a_with_win32api()
        process_text()


# Copy and paste the converted text and call the core function
def process_text():
    # keyboard.send('ctrl+c')
    ctrl_c_with_win32api()
    time.sleep(0.1)
    try:
        text = pyperclip.paste()
        # Check if text can be converted to string
        if not isinstance(text, str) or not text.strip():
            print("Clipboard does not contain a valid string.")
            return
    except Exception as e:
        print(f"Error accessing clipboard: {e}")
        return
    translated_text = transcript_text(text)
    pyperclip.copy(translated_text)  # Import the result to the clipboard
    # keyboard.send('ctrl+v')
    ctrl_v_with_win32api()
    # time.sleep(0.1)
    # keyboard.send('alt+shift')
    alt_shift_with_win32api()


# def is_key_pressed(key_code):
#     # Checks whether the specified key is currently pressed
#     return win32api.GetAsyncKeyState(key_code) & 0x8000


# Main function
def main():
    # Implementation of the setup_tray on a separate thread
    import threading
    tray_thread = threading.Thread(target=setup_tray)
    tray_thread.start()


    # # the old hotkey mechanism

    # # Specify hotkey
    # # Be careful that the hotkey does not overlap with other hotkeys.
    # # Also look at line 233
    # # Refer to this site: learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
    # # Default Hotkey: ctrl+alt+k
    # key1 = win32con.VK_CONTROL
    # key2 = win32con.VK_MENU
    # key3 = 0x4B
    #
    # print("Listening for hotkey...")
    #
    # while True:
    #     # Check if hotkey is pressed
    #     # If you want to use a combination of two keys or more than three keys,
    #     # you must change the bottom line as in the example.
    #     # if is_key_pressed(key1) and is_key_pressed(key2):
    #     if is_key_pressed(key1) and is_key_pressed(key2) and is_key_pressed(key3):
    #         check_clipboard_and_process()
    #         # Short timeout to prevent multiple execution of code when keys are pressed
    #         time.sleep(0.5)
    #
    #     # Short delay to reduce CPU consumption
    #     time.sleep(0.02)

    manager = HotkeyManager()
    manager.listen_for_hotkey()

if __name__ == "__main__":
    main()