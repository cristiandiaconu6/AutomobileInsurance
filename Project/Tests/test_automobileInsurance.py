from selenium import webdriver
import pytest
from Project.Pages.automobile_insurance import VehicleData
from Project.Pages.automobile_insurance import InsurantData
from Project.Pages.automobile_insurance import ProductData
from Project.Pages.automobile_insurance import PriceOptions
from Project.Pages.automobile_insurance import SendQuote
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class Test_VehicleData():

    @pytest.fixture()
    def test_setup(self):
        self.chromeOptions = Options()
        self.chromeOptions.add_experimental_option("prefs", {"download.default_directory": "C:\Reports"})
        #self.chromeDriverPath = "C:/Users/cristian.diaconu/PycharmProjects/AutomobileInsurance/Drivers/chromedriver.exe"
        self.chromeDriverPath = "c:/hostedtoolcache/windows/python/3.7.6/x64/lib/site-packages/seleniumbase/drivers/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.chromeDriverPath, options=self.chromeOptions)
        global driver
        driver = self.driver
        driver.maximize_window()
        driver.get("http://sampleapp.tricentis.com/101")
        driver.implicitly_wait(10)
        yield
        driver.close()

    def test_example(self, test_setup):
    #Selecting Automobile from top section
        automobile = VehicleData(driver)
        automobile.select_automobile()

    #Entering Vehicle Data
        vehicleData = VehicleData(driver)
        vehicleData.enter_make("Volvo")
        vehicleData.enter_engine_performance("120")
        vehicleData.enter_date_of_manufacture("11/11/2013")
        vehicleData.enter_number_of_seats("5")
        vehicleData.enter_fuel_type("Gas")
        vehicleData.enter_list_price("30000")
        vehicleData.enter_license_plate_number("NT66ACD")
        vehicleData.enter_annual_mileage("25000")
        vehicleData.click_next()

    #Entering Insurant Data
        insurantData = InsurantData(driver)
        insurantData.enter_first_name("Cristian")
        insurantData.enter_last_name("Diaconu")
        insurantData.enter_date_of_birth("06/12/1992")
        insurantData.check_gender("male")
        insurantData.select_country("Romania")
        insurantData.enter_zip_code("700345")
        insurantData.select_occupation("Employee")
        insurantData.check_hobby("other")
        insurantData.click_next()

    #Enter Product Data
        productData = ProductData(driver)
        productData.enter_start_date("05/05/2021")
        productData.select_insurance_sum("5.000.000,00")
        productData.select_merit_rating("Bonus 7")
        productData.select_damage_insurance("Full Coverage")
        productData.check_optional_products("euro protection")
        productData.check_optional_products("legal defense insurance")
        productData.select_courtesy_car("Yes")
        productData.click_next()

    #Select Price Option
        priceOption = PriceOptions(driver)
        priceOption.select_price_option("gold")
        downloadQuote = PriceOptions(driver)
        downloadQuote.download_quote()

    #Send Quote
        sendQuote = SendQuote(driver)
        sendQuote.enter_email("cristian@g.com")
        sendQuote.enter_phone("123012031")
        sendQuote.enter_username("diac")
        sendQuote.enter_password("Hello1234")
        sendQuote.confirm_password("Hello1234")
        sendQuote.enter_comment("blabla")
        sendQuote.click_send()


#blabla




