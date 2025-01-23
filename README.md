

### `README.md`

```markdown
# WhatsApp Automation with Edge WebDriver

This Python project automates sending birthday messages on WhatsApp using Selenium and Edge WebDriver. It allows you to schedule and send personalized messages automatically at a specific time to your contacts based on their birthdays.

## Tech Stack:
- **Python**: Main programming language.
- **Selenium**: For automating browser interactions.
- **EdgeDriver**: WebDriver for automating Microsoft Edge browser.

## Prerequisites:
Before running the automation script, ensure you have:
1. **Python 3.x** installed.
2. **Edge WebDriver** corresponding to your Microsoft Edge version.

### Steps to Check Your Edge Version:

1. Open Microsoft Edge.
2. Click on the **three dots** (`...`) in the top-right corner.
3. Go to **Help and feedback** → **About Microsoft Edge**.
4. Note down the version number (e.g., 109.0.1518.78).

### Steps to Download Edge WebDriver:

1. Go to the official [Microsoft Edge WebDriver download page](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
2. Select the version that matches your **Edge version**.
3. Download and extract the `msedgedriver.exe` file.
4. Place the `msedgedriver.exe` file in a folder, e.g., `C:\Users\admin\Desktop\auto\`.

## How to Use:

1. Clone the repository:
   ```
   git clone https://github.com/your-username/WEB-SCRAPING.git
   ```

2. Install the required dependencies:
   ```
   pip install selenium
   ```

3. Update the **driver path** in `main.py`:
   ```python
   driver_path = r"C:\Users\admin\Desktop\auto\msedgedriver.exe"
   ```

4. Run the script:
   ```
   python main.py
   ```

5. **Scan the QR code** on WhatsApp Web when prompted. Then, the automation will start.

### Features:
- **Birthday Reminder**: The script will automatically check the current date and send a birthday message to contacts listed in the `birthday_contacts` dictionary.
- **Customizable**: You can modify the contacts and their birthday dates in the `birthday_contacts` dictionary.

### Project Script:
- **main.py**: Python script to automate sending birthday messages.

## License:
This project is licensed under the MIT License.
```

---

