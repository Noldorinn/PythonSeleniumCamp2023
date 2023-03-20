from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Saucedemo:
    def test_empty_areas(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        usernameInput = driver.find_element(By.NAME,"user-name")
        usernameInput.send_keys("")
        passwordInput = driver.find_element(By.NAME,"password")
        passwordInput.send_keys("")

        loginButton = driver.find_element(By.NAME,"login-button")
        loginButton.click()
        sleep(5)

        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Test sonucu: {testResult}")

    def test_empty_password(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        usernameInput = driver.find_element(By.NAME,"user-name")
        usernameInput.send_keys("standard_user")
        passwordInput = driver.find_element(By.NAME,"password")
        passwordInput.send_keys("")

        loginButton = driver.find_element(By.NAME,"login-button")
        loginButton.click()
        sleep(5)

        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Test sonucu: {testResult}")

    def test_locked_user(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        usernameInput = driver.find_element(By.NAME,"user-name")
        usernameInput.send_keys("locked_out_user")
        passwordInput = driver.find_element(By.NAME,"password")
        passwordInput.send_keys("secret_sauce")

        loginButton = driver.find_element(By.NAME,"login-button")
        loginButton.click()
        sleep(5)

        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test sonucu: {testResult}")

    def test_error_xbuttons(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        usernameInput = driver.find_element(By.NAME,"user-name")
        usernameInput.send_keys("")
        passwordInput = driver.find_element(By.NAME,"password")
        passwordInput.send_keys("")

        loginButton = driver.find_element(By.NAME,"login-button")
        loginButton.click()
        sleep(5)

        errorMessageXButton = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        errorMessageXButton.click()
        sleep(5)
        # errorXSvgs = driver.find_elements(By.XPATH,"//div/*[@data-icon='times-circle']")
        errorXSvgs = driver.find_elements(By.CLASS_NAME,"error_icon")

        if len(errorXSvgs)==0:
            print(f"Login error x buton testi: True")
        else:
            print(f"Login error x buton testi: False")

    def test_standartuser_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        usernameInput = driver.find_element(By.NAME,"user-name")
        usernameInput.send_keys("standard_user")
        passwordInput = driver.find_element(By.NAME,"password")
        passwordInput.send_keys("secret_sauce")

        loginButton = driver.find_element(By.NAME,"login-button")
        loginButton.click()
        sleep(5)

        testURL = driver.current_url == "https://www.saucedemo.com/inventory.html"
        print(f"Standart kullanıcı sayfa yönlendirme testi {testURL}")

    def test_item_numbers(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)

        usernameInput = driver.find_element(By.NAME,"user-name")
        usernameInput.send_keys("standard_user")
        passwordInput = driver.find_element(By.NAME,"password")
        passwordInput.send_keys("secret_sauce")

        loginButton = driver.find_element(By.NAME,"login-button")
        loginButton.click()
        sleep(5)

        itemNumbers = driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Listelenen ürün sayı testi: {len(itemNumbers)}")



        
        


testClass = Test_Saucedemo()
# testClass.test_empty_areas()
# testClass.test_empty_password()
# testClass.test_locked_user()
# testClass.test_error_xbuttons()
# testClass.test_standartuser_login()
testClass.test_item_numbers()

