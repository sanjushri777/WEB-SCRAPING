

### **WhatsApp Automation Script - Birthday Wishes**

This Python script automates sending WhatsApp birthday wishes at an exact time. It's designed to help you never miss a special occasion again!

## **Features**:
- Automates sending birthday messages on WhatsApp at a specific time.
- Customizable to add multiple contacts and tailor the message.
- Uses Selenium WebDriver with Microsoft Edge (but can be adapted for Chrome/Firefox).

## **Requirements**:
- Python 3.x
- Selenium WebDriver
- Microsoft Edge Driver (ensure the version matches your browser)

## **Installation**:

### 1. Clone this repository:
```bash
git clone https://github.com/sanjushri777/WEB-SCRAPING.git
```

### 2. Install Dependencies:
```bash
pip install selenium
```

### 3. Download Edge WebDriver:
- Go to the [Edge WebDriver Download page](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
- Make sure to download the WebDriver version matching your installed Edge version.

### 4. Update WebDriver Path:
- Ensure that the `driver_path` in the Python script points to the location of your downloaded **msedgedriver.exe** file.
  ```python
  driver_path = r"C:\path\to\msedgedriver.exe"
  ```

### 5. Run the Script:
```bash
python whatsapp_automation.py
```

### 6. Scan the QR Code:
- When prompted, scan the QR code shown in the terminal to log in to WhatsApp Web.

### 7. Customize Contacts:
- Modify the `birthday_contacts` dictionary to add the names and birthdates of the people you want to wish.
- Example: `{"ASWINI": "01-23"}` for a birthday on January 23rd.

---

## **Pros**:
- Automates birthday wishes and sends them at the **exact time**, ensuring you never miss important birthdays.
- Saves time as you don’t need to manually send birthday wishes.

## **Cons**:
- **Web WhatsApp** must be logged in at the time the script runs.
- The **system** must be kept on for the script to run continuously.

---

## **License**:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

