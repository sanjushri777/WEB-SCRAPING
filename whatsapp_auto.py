from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime


driver_path = r"C:\Users\admin\Desktop\auto\msedgedriver.exe"


birthday_contacts = {
       #for test case
       "ASWINI": "01-23"
}

message_template = "Happy Birthday, {name}! Wishing you a fantastic year ahead!"


service = Service(driver_path)
driver = webdriver.Edge(service=service)


driver.get("https://web.whatsapp.com/")


input("Scan the QR code and press Enter to continue...")

while True:
    
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"Current time: {current_time}")

    
    target_time = "09:56:00"
    
    if current_time == target_time:
        today = datetime.now().strftime("%m-%d")
        
        
        for contact, birthday in birthday_contacts.items():
            if birthday == today:
                
                search_box = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true']"))
                )
                search_box.clear()
                search_box.send_keys(contact)
                time.sleep(2)  

                try:
                    
                    contact_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, f"//span[@title='{contact}']"))
                    )
                    contact_element.click()
                    print(f"Contact {contact} found and clicked!")
                except Exception as e:
                    print(f"Error finding contact {contact}: {e}")
                    continue  
                
                try:
                    message_box = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @data-tab='10']"))
                    )
                    print("Message box found!")

                    
                    message = message_template.format(name=contact)
                    message_box.send_keys(message)

                   
                    message_box.send_keys(Keys.RETURN)
                    print(f"Message sent to {contact}.")

                    
                    time.sleep(1)

                except Exception as e:
                    print(f"Error finding message box or sending message: {e}")
                    continue  
        break  
    else:
        print("Waiting for the right time...")

    time.sleep(1)
