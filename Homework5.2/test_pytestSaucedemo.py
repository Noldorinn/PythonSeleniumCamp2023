from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date

class Test_PytestSaucedemo:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        
    def teardown_method(self):
        self.driver.quit()

    def test_pytest_EmptyAreas(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{Path(__file__).parent.resolve()}/test-pytest-EmptyAreas-{date.today()}.png")
        assert errorMessage.text == "Epic sadface: Username is required"

    @pytest.mark.parametrize("username,password",[("standard_user",""),("locked_out_user",""),("problem_user",""),("performance_glitch_user","")])
    def test_pytest_EmptyPassword(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{Path(__file__).parent.resolve()}/test-pytest-EmptyPassword-{username}-{date.today()}.png")
        assert  errorMessage.text == "Epic sadface: Password is required"

    @pytest.mark.parametrize("username,password",[("locked_out_user","secret_sauce")])
    def test_pytest_LockedUser(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{Path(__file__).parent.resolve()}/test-pytest-LockedUser-{username}-{password}-{date.today()}.png")
        assert  errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

    @pytest.mark.parametrize("username,password",[("",""),("standart_user",""),("standart_user","problem_user")])
    def test_pytest_XButtonsRemove(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessageXButton = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        errorMessageXButton.click()
        errorXSvgs = self.driver.find_elements(By.CLASS_NAME,"error_icon")
        self.driver.save_screenshot(f"{Path(__file__).parent.resolve()}/test-pytest-XButtonRemove-{username}-{password}-{date.today()}.png")
        assert len(errorXSvgs)==0

    def test_pytest_StandartUserLogin(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        self.driver.save_screenshot(f"{Path(__file__).parent.resolve()}/test-pytest-StandartUserLogin-{date.today()}.png")
        assert  self.driver.current_url == "https://www.saucedemo.com/inventory.html"

    def test_pytest_ItemNumbers(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        itemNumbers = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        self.driver.save_screenshot(f"{Path(__file__).parent.resolve()}/test-pytest-ItemNumbers-{date.today()}.png")
        assert len(itemNumbers)==6

    def test_pytest_AddToCart(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-onesie\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]").click()
        self.driver.save_screenshot(f"{Path(__file__).parent.resolve()}/test-pytest-AddToCart-{date.today()}.png")
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-backpack\"]").text == "Remove"
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-bolt-t-shirt\"]").text == "Remove"
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-fleece-jacket\"]").text == "Remove"
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-onesie\"]").text == "Remove"
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-test.allthethings()-t-shirt-(red)\"]").text == "Remove"
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-bike-light\"]").text == "Remove"
        

    def test_pytest_ShopIcon(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-onesie\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]").click()
        self.driver.save_screenshot(f"{Path(__file__).parent.resolve()}/test-pytest-ShopIcon-{date.today()}.png")
        assert self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text == "6"

    def test_pytest_LogOut(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        menuBttn=self.driver.find_element(By.ID, "react-burger-menu-btn")
        menuBttn.click()
        self.waitForElementVisible((By.ID,"logout_sidebar_link"))
        logoutBttn=self.driver.find_element(By.ID,"logout_sidebar_link")
        logoutBttn.click()
        self.driver.save_screenshot(f"{Path(__file__).parent.resolve()}/test-pytest-LogOut-{date.today()}.png")
        assert  self.driver.current_url == "https://www.saucedemo.com/"
        

    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))