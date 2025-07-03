from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def auto_fill_form():
    try:
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.get("https://example.com/form")

        driver.find_element(By.ID, "name").send_keys("Adam Ahamed")
        driver.find_element(By.ID, "email").send_keys("adam@example.com")
        driver.find_element(By.ID, "submit").click()
        driver.quit()
        return "✅ Web form submitted via Selenium!"
    except Exception as e:
        return f"❌ Automation failed: {e}"
