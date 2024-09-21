# KeySwitchFix
KeySwitchFix - Quickly Fix Mistyped Text When Using the Wrong Keyboard Layout

"Ever started typing in one language only to realize your keyboard was set to another? KeySwitchFix is here to help! With a simple hotkey, you can instantly convert your mistyped gibberish into the correct language (e.g., Persian or English). Whether you're working in multiple languages or just accidentally typed in the wrong layout, KeySwitchFix ensures seamless transitions between languages. Say goodbye to retyping frustration!"

### فارسی:
اصلاح سریع متن اشتباه تایپ شده هنگام استفاده از زبان نادرست صفحه‌کلید
"آیا تا به حال تایپ کرده‌اید و بعد متوجه شده‌اید که کیبورد شما روی زبان دیگری تنظیم بوده؟ KeySwitchFix برای کمک اینجاست! با فشردن یک کلید میانبر، می‌توانید متن نامفهوم تایپ‌شده را به زبان درست (مثلاً فارسی یا انگلیسی) تبدیل کنید. چه در حال کار با چند زبان باشید یا به اشتباه در چیدمان اشتباه تایپ کرده باشید، KeySwitchFix تغییر زبان‌ها را برای شما آسان و بدون دردسر می‌کند. با این برنامه از دوباره‌نویسی خسته‌کننده خداحافظی کنید!"

---

#### How It Works:
By default, the hotkey for the program is `Ctrl + Alt + K`. When pressed, the program detects the currently highlighted text and converts it to the opposite language (e.g., Persian to English or vice versa). 

If no text is highlighted, the program will automatically select the entire text using `Ctrl + A` and then proceed with the conversion. After each operation, the keyboard layout will be switched using the `Alt + Shift` combination.

If you want to change the default hotkey, please refer to the following section



### فارسی:

#### نحوه عملکرد:
به صورت پیش‌فرض، هات‌کی برنامه `Ctrl + Alt + K` است. با فشردن این ترکیب، برنامه متن انتخاب‌شده (هایلایت‌شده) را شناسایی کرده و آن را به زبان مقابل (مثلاً از فارسی به انگلیسی یا برعکس) تبدیل می‌کند.

اگر هیچ متنی هایلایت نشده باشد، برنامه به‌طور خودکار با استفاده از `Ctrl + A` کل متن را انتخاب کرده و سپس تبدیل را انجام می‌دهد. همچنین بعد از هر عملیات، با استفاده از ترکیب کلید `Alt + Shift` چیدمان کیبورد تغییر خواهد کرد.

اگر قصد دارید هات‌کی پیش‌فرض را تغییر دهید، لطفاً برای راهنمایی به بخش بعدی مراجعه کنید.

---


#### Customizing the Hotkey:
To change the default hotkey of the program, you first need to save the three files `KeySwitchFix.py`, `requirements.txt`, and `logo.ico` in the same folder. Next, open the `KeySwitchFix.py` file in a text editor. You will need to modify the variables `key1`, `key2`, and `key3` around line 222.

For special keys like `Ctrl`, `Alt`, etc., follow the format used in the original code. For regular keys, do the same as demonstrated. Ensure that your new hotkey does not conflict with existing hotkeys on your system. 

For example, to set the hotkey to `Ctrl + Shift + G`, modify the variables as follows:
```python
key1 = win32con.VK_CONTROL
key2 = win32con.VK_SHIFT
key3 = 0x47
```

For more information on key codes, refer to this site:  
[Virtual-Key Codes Documentation](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes)

If you want to use a combination of two keys or more than three keys, you must also modify the line around 233. For example, for a two-key combination:
```python
if is_key_pressed(key1) and is_key_pressed(key2):
```


#### Compiling to an EXE:
After editing the code, you will need to compile it into an executable file (.exe). To do this, first, download and install Python from the official website. Ensure that Python is correctly working from the command line.

Next, open a terminal in the folder containing the downloaded files and run the following commands:

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Compile the script into a .exe file:
```bash
pyinstaller --onefile --windowed --icon=logo.ico KeySwitchFix.py
```

The compiled .exe file will be available in the `dist` folder.



### فارسی:

#### سفارشی‌سازی هات‌کی:
برای تغییر هات‌کی پیش‌فرض برنامه، ابتدا باید سه فایل `KeySwitchFix.py`، `requirements.txt` و `logo.ico` را در یک پوشه ذخیره کنید. سپس فایل `KeySwitchFix.py` را با یک ویرایشگر متن باز کنید. در حدود خط ۲۲۲، متغیرهای `key1`، `key2` و `key3` را ویرایش کنید.

برای کلیدهای خاص مثل `Ctrl`، `Alt` و غیره، از فرمت کد اصلی پیروی کنید. برای کلیدهای عادی نیز مشابه عمل کنید. دقت داشته باشید که هات‌کی جدید شما با هات‌کی‌های موجود تداخلی نداشته باشد.

به‌عنوان نمونه، اگر می‌خواهید هات‌کی را به `Ctrl + Shift + G` تغییر دهید، متغیرها را به این صورت تنظیم کنید:
```python
key1 = win32con.VK_CONTROL
key2 = win32con.VK_SHIFT
key3 = 0x47
```

برای اطلاعات بیشتر درباره کدهای کلیدها به این سایت مراجعه کنید:  
[مستندات Virtual-Key Codes](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes)

اگر بخواهید از ترکیب دو کلید یا بیشتر از سه کلید استفاده کنید، باید خط ۲۳۳ را نیز ویرایش کنید. به‌عنوان مثال برای ترکیب دو کلید:
```python
if is_key_pressed(key1) and is_key_pressed(key2):
```



#### کامپایل به فایل EXE:
پس از ویرایش کد، باید آن را به یک فایل اجرایی (.exe) تبدیل کنید. برای این کار ابتدا پایتون را از سایت رسمی آن دانلود و نصب کنید و مطمئن شوید که در خط فرمان به درستی کار می‌کند.

سپس یک ترمینال را در پوشه‌ای که فایل‌ها را ذخیره کرده‌اید باز کرده و دستورات زیر را به ترتیب اجرا کنید:

1. نصب وابستگی‌ها:
```bash
pip install -r requirements.txt
```

2. کامپایل اسکریپت به فایل اجرایی:
```bash
pyinstaller --onefile --windowed --icon=logo.ico KeySwitchFix.py
```

فایل اجرایی در پوشه `dist` در دسترس خواهد بود.

---

#### Adding the Program to Windows Startup:
To add the program to Windows Startup, follow these steps:

1. First, save the program in a suitable location on your computer.
2. Create a shortcut of the program.
3. Press `Windows + R` to open the "Run" dialog box.
4. In the dialog box, type `shell:startup` and press `Enter`. This will open the Startup folder.
5. Move the created shortcut into the opened Startup folder.

Once done, the program will automatically run when you start your computer. You can also manage the program’s startup status by checking the **Task Manager** under the **Startup** tab to enable or disable it.



### فارسی:

#### اضافه کردن برنامه به استارت‌آپ ویندوز:
برای اضافه کردن برنامه به استارت‌آپ ویندوز مراحل زیر را دنبال کنید:

1. ابتدا برنامه را در یک مکان مناسب روی کامپیوتر ذخیره کنید.
2. سپس یک شورتکات (میانبر) از برنامه ایجاد کنید.
3. کلیدهای `Windows + R` را فشار دهید تا پنجره "Run" باز شود.
4. در پنجره باز شده تایپ کنید `shell:startup` و کلید `Enter` را بزنید. با این کار پوشه استارت‌آپ باز می‌شود.
5. شورتکاتی که ایجاد کرده‌اید را به پوشه استارت‌آپ منتقل کنید.

بعد از انجام این مراحل، برنامه به‌طور خودکار با شروع ویندوز اجرا خواهد شد. همچنین می‌توانید وضعیت استارت‌آپ برنامه را از طریق **Task Manager** در تب **Startup** مدیریت کنید و آن را فعال یا غیرفعال نمایید.

<br><br><br><br><br>
###### Made with ChatGPT and Gemini 😊
