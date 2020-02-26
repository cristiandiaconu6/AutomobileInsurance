from selenium.webdriver.common.by import By

class Locators():

#Categories
    automobile_category = (By.ID, "nav_automobile")

#Sub-categories
    select_price_option = (By.ID, "selectpriceoption")

#Enter Vehicle Data
    make_dropmenu = (By.ID, "make")
    engine_performance_textbox = (By.ID, "engineperformance")
    date_of_manufacture_textbox = (By.ID, "dateofmanufacture")
    number_of_seats_dropmenu = (By.ID, "numberofseats")
    fuel_type_dropmenu = (By.XPATH, "//select[@id='fuel']")
    list_price_textbox = (By.NAME, "List Price")
    license_plate_number_textbox = (By.ID, "licenseplatenumber")
    annual_mileage_textbox = (By.ID, "annualmileage")
    next_button_to_insurantData = (By.ID, "nextenterinsurantdata")

#Enter Insurant Data
    first_name_textbox = (By.ID, "firstname")
    last_name_textbox = (By.ID, "lastname")
    date_of_birth_textbox = (By.ID, "birthdate")
    gender_option = {"male": (By.XPATH, "//label[text()='Male']"),
                     "female": (By.XPATH, "//label[text()='Female']")}
    country_dropmenu = (By.ID, "country")
    zip_code_textbox = (By.ID, "zipcode")
    occupation_dropmenu = (By.ID, "occupation")
    hobby_options = {"speeding": (By.XPATH, "//div[@class='field idealforms-field idealforms-field-checkbox invalid']//p[@class='group']//label[1]"),
                     "bungee jumping": (By.XPATH, "//div[@class='field idealforms-field idealforms-field-checkbox invalid']//label[2]"),
                     "cliff diving": (By.XPATH, "//div[@class='field idealforms-field idealforms-field-checkbox invalid']//label[3]"),
                     "skydiving": (By.XPATH, "//div[@class='field idealforms-field idealforms-field-checkbox invalid']//label[4]"),
                     "other": (By.XPATH, "//body//label[5]")}

    prev_button_to_vehicleData = (By.ID, "preventervehicledata")
    next_button_to_productData = (By.ID, "nextenterproductdata")

#Enter Product Data
    start_date_textbox = (By.ID, "startdate")
    insurance_sum_dropmenu = (By.ID, "insurancesum")
    merit_rating_dropmenu = (By.ID, "meritrating")
    damage_insurance_dropmenu = (By.ID, "damageinsurance")
    optional_products = {"euro protection": (By.XPATH, "//label[text()='Euro Protection']"),
                        "legal defense insurance": (By.XPATH, "//label[text()='Legal Defense Insurance']")}
    courtesy_car_dropmenu = (By.ID, "courtesycar")
    prev_button_to_insurantData = (By.ID, "preventerinsurancedata")
    next_button_to_priceOption = (By.ID, "nextselectpriceoption")

#Select Price Option
    price_options = {"silver": (By.XPATH, "//section[@id='pricePlans']//label[1]"),
                     "gold": (By.XPATH, "//section[@id='pricePlans']//label[2]"),
                     "platinum": (By.XPATH, "//section[@id='pricePlans']//label[3]"),
                     "ultimate": (By.XPATH, "//section[@id='pricePlans']//label[4]")}
    download_quote_button = (By.XPATH, "//a[@id='downloadquote']//i[@class='fa fa-file-pdf-o']")
    next_button_to_sendQuote = (By.ID, "nextsendquote")

#Send Quote
    email_textbox = (By.ID, "email")
    phone_textbox = (By.ID, "phone")
    username_textbox = (By.ID, "username")
    password_textbox = (By.ID, "password")
    confirm_password_textbox = (By.ID, "confirmpassword")
    comments_textbox = (By.ID, "Comments")
    prev_button_to_priceOption = (By.ID, "prevselectpriceoption")
    send_button = (By.ID, "sendemail")


