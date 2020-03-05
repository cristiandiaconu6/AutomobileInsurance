from selenium.webdriver.support.select import Select
from Project.Locators.Locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

class VehicleData():
    def __init__(self, driver):
        self.driver = driver

    def select_automobile(self):
        self.driver.find_element(*Locators.automobile_category).click()

    def enter_make(self, make):
        Select(self.driver.find_element(*Locators.make_dropmenu)).select_by_visible_text(make)


    def enter_engine_performance(self, enginePerformance):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((Locators.engine_performance_textbox))).send_keys(enginePerformance)

    def enter_date_of_manufacture(self, dateOfManufacture):
        self.driver.find_element(*Locators.date_of_manufacture_textbox).send_keys(dateOfManufacture)

    def enter_number_of_seats(self, numberOfSeats):
        Select(self.driver.find_element(*Locators.number_of_seats_dropmenu)).select_by_visible_text(numberOfSeats)

    def enter_fuel_type(self, fuelType):
        Select(self.driver.find_element(*Locators.fuel_type_dropmenu)).select_by_visible_text(fuelType)

    def enter_list_price(self, listPrice):
        self.driver.find_element(*Locators.list_price_textbox).send_keys(listPrice)

    def enter_license_plate_number(self, licensePlateNumber):
        self.driver.find_element(*Locators.license_plate_number_textbox).send_keys(licensePlateNumber)

    def enter_annual_mileage(self, annualMileage):
        self.driver.find_element(*Locators.annual_mileage_textbox).send_keys(annualMileage)

    def click_next(self):
        self.driver.find_element(*Locators.next_button_to_insurantData).click()

class InsurantData():
    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, firstName):
        self.driver.find_element(*Locators.first_name_textbox).send_keys(firstName)

    def enter_last_name(self, lastName):
        self.driver.find_element(*Locators.last_name_textbox).send_keys(lastName)

    def enter_date_of_birth(self, dateOfBirth):
        self.driver.find_element(*Locators.date_of_birth_textbox).send_keys(dateOfBirth)

    def check_gender(self, gender):
        self.driver.find_element(*Locators.gender_option[gender]).click()

    def select_country(self, country):
        Select(self.driver.find_element(*Locators.country_dropmenu)).select_by_visible_text(country)

    def enter_zip_code(self, zipCode):
        self.driver.find_element(*Locators.zip_code_textbox).send_keys(zipCode)

    def select_occupation(self, occupation):
        Select(self.driver.find_element(*Locators.occupation_dropmenu)).select_by_visible_text(occupation)

    def check_hobby(self, hobby):
        self.driver.find_element(*Locators.hobby_options[hobby]).click()

    def click_prev(self):
        self.driver.find_element(*Locators.prev_button_to_vehicleData).click()

    def click_next(self):
        self.driver.find_element(*Locators.next_button_to_productData).click()

class ProductData():
    def __init__(self, driver):
        self.driver = driver

    def enter_start_date(self, startDate):
        self.driver.find_element(*Locators.start_date_textbox).send_keys(startDate)

    def select_insurance_sum(self, insuranceSum):
        Select(self.driver.find_element(*Locators.insurance_sum_dropmenu)).select_by_visible_text(insuranceSum)

    def select_merit_rating(self, meritRating):
        Select(self.driver.find_element(*Locators.merit_rating_dropmenu)).select_by_visible_text(meritRating)

    def select_damage_insurance(self, damageInsurance):
        Select(self.driver.find_element(*Locators.damage_insurance_dropmenu)).select_by_visible_text(damageInsurance)

    def check_optional_products(self, optionalProduct):
        self.driver.find_element(*Locators.optional_products[optionalProduct]).click()

    def select_courtesy_car(self, courtesyCarOption):
        Select(self.driver.find_element(*Locators.courtesy_car_dropmenu)).select_by_visible_text(courtesyCarOption)

    def click_prev(self):
        self.driver.find_element(*Locators.prev_button_to_insurantData).click()

    def click_next(self):
        self.driver.find_element(*Locators.next_button_to_priceOption).click()


class PriceOptions():
    def __init__(self, driver):
        self.driver = driver

    def select_price_option(self, priceOption):
        self.driver.find_element(*Locators.price_options[priceOption]).click()

    def download_quote(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*Locators.download_quote_button).click()
        time.sleep(10)
        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((Locators.select_price_option))).click()
        self.driver.find_element(*Locators.select_price_option).click()
        self.driver.find_element(*Locators.next_button_to_sendQuote).click()

class SendQuote():
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(*Locators.email_textbox).send_keys(email)

    def enter_phone(self, phone):
        self.driver.find_element(*Locators.phone_textbox).send_keys(phone)

    def enter_username(self, username):
        self.driver.find_element(*Locators.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*Locators.password_textbox).send_keys(password)

    def confirm_password(self, password):
        self.driver.find_element(*Locators.confirm_password_textbox).send_keys(password)

    def enter_comment(self, comment):
        self.driver.find_element(*Locators.comments_textbox).send_keys(comment)

    def click_send(self):
        self.driver.find_element(*Locators.send_button).click()













