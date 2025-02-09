import tkinter as tk
from tkinter import messagebox
import json
import os
import subprocess
import psutil
import time

class HotkeyGUI:
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.root = tk.Tk()
        self.root.title("تنظیم هات‌کی")

        # متغیرهای چک‌باکس‌ها برای کلیدهای ترکیبی
        self.ctrl_var = tk.BooleanVar()
        self.alt_var = tk.BooleanVar()
        self.shift_var = tk.BooleanVar()
        self.win_var = tk.BooleanVar()

        self._create_widgets()

    def _create_widgets(self):
        """ایجاد ویجت‌های رابط گرافیکی"""
        tk.Checkbutton(self.root, text="Ctrl", variable=self.ctrl_var).grid(row=0, column=0, sticky="w")
        tk.Checkbutton(self.root, text="Alt", variable=self.alt_var).grid(row=1, column=0, sticky="w")
        tk.Checkbutton(self.root, text="Shift", variable=self.shift_var).grid(row=2, column=0, sticky="w")
        tk.Checkbutton(self.root, text="Win", variable=self.win_var).grid(row=3, column=0, sticky="w")

        tk.Label(self.root, text="کلید نهایی (A-Z):").grid(row=4, column=0, sticky="w")
        self.key_entry = tk.Entry(self.root)
        self.key_entry.grid(row=4, column=1)

        save_button = tk.Button(self.root, text="ذخیره هات‌کی", command=self.save_hotkey)
        save_button.grid(row=5, column=0, columnspan=2)

    def save_hotkey(self):
        """ذخیره هات‌کی جدید در فایل"""
        modifiers = 0
        if self.ctrl_var.get():
            modifiers |= 2  # MOD_CONTROL
        if self.alt_var.get():
            modifiers |= 1  # MOD_ALT
        if self.shift_var.get():
            modifiers |= 4  # MOD_SHIFT
        if self.win_var.get():
            modifiers |= 8  # MOD_WIN

        key = self.key_entry.get().upper()
        if len(key) != 1 or not key.isalpha():
            messagebox.showerror("خطا", "لطفاً یک حرف معتبر وارد کنید.")
            return

        key_code = ord(key)
        self._save_hotkey_to_file(modifiers, key_code)
        messagebox.showinfo("موفقیت", f"هات‌کی جدید با موفقیت ثبت شد: {modifiers} + {key}")

        self.restart_main_binary()

    def _save_hotkey_to_file(self, modifiers, key_code):
        """ذخیره هات‌کی در فایل تنظیمات"""
        try:
            config = {"modifiers": modifiers, "key_code": key_code}
            with open(self.config_file, "w") as file:
                json.dump(config, file)
            print("هات‌کی ذخیره شد:", config)
        except Exception as e:
            print("خطا در ذخیره فایل تنظیمات:", e)

    def restart_main_binary(self):
        """خاموش کردن و اجرای دوباره باینری اصلی"""
        try:
            # نام باینری اصلی
            main_binary_name = "KeySwitchFix.exe"

            # شناسایی و بستن فرآیندهای مرتبط با باینری اصلی
            for process in psutil.process_iter(attrs=["pid", "name"]):
                if process.info["name"] == main_binary_name:
                    process.kill()
                    print(f"فرآیند {main_binary_name} با موفقیت بسته شد.")

            time.sleep(1)
            # اجرای دوباره باینری اصلی
            subprocess.Popen([main_binary_name],
            creationflags=subprocess.DETACHED_PROCESS)
            print(f"باینری {main_binary_name} دوباره اجرا شد.")

            # خروج از برنامه GUI
            # os._exit(0)
        except Exception as e:
            print(f"خطا در ریستارت کردن باینری اصلی: {e}")
            messagebox.showerror("خطا", "مشکلی در ریستارت کردن برنامه اصلی وجود دارد.")

    def run(self):
        """اجرای رابط گرافیکی"""
        self.root.mainloop()

# تست کلاس
if __name__ == "__main__":
    gui = HotkeyGUI()
    gui.run()
