"""
@author Chris Kade

HGTV/Food Network 2021 Home Giveaway Entry Bot
Stores information in a database so all you have to do to fill out both forms
after originally entering all of your information is type your last name
"""

import enum
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sqlite3


class Month(enum.Enum):
    JAN = 2
    FEB = 3
    MAR = 4
    APR = 5
    MAY = 6
    JUN = 7
    JUL = 8
    AUG = 9
    SEP = 10
    OCT = 11
    NOV = 12
    DEC = 13


class Sex(enum.Enum):
    F = 1
    M = 2


class UserStatus(enum.Enum):
    NEW = 1
    RETURNING = 2


def construct_month_path(month_enum_object, month):
    assert month_enum_object[month]

    option_value = month_enum_object[month].value
    month_path = '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/'
    return month_path + 'option[{}]'.format(option_value)


def construct_gender_path(sex_enum_object, sex):
    assert sex_enum_object[sex]

    option_value = sex_enum_object[sex].value
    sex_path = '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[6]/div[2]/'
    return sex_path + 'div[{}]/input'.format(option_value)


def prompt_user_status():
    description = "This program helps you sign up for the HGTV giveaway \n without having to manually enter all account information. \n"
    new_user = "--- If you are a first time user, type NEW. \n"
    returning = "--- If you're already in the database type RETURNING. \n"

    valid_entry = False
    while (not valid_entry):
        user_status = input(description + new_user + returning)
        if user_status.upper() in UserStatus._member_names_:
            valid_entry = True
    return user_status.upper()


def init_account_info(driver_instance):
    """
    This function stores all of the information to input for new user
    entering the Food Network contest for the first time.
    """

    first = driver_instance.find_element_by_id('name_Firstname')
    first.send_keys(store[0][1])
    last = driver_instance.find_element_by_id('name_Lastname')
    last.send_keys(store[0][2])
    address = driver_instance.find_element_by_id('address_Address1')
    address.send_keys(store[0][3])
    city = driver_instance.find_element_by_id('address_City')
    city.send_keys(store[0][4])


    driver_instance.find_element_by_xpath(
        '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[4]/div[2]/div[4]/div[1]/select/option[24]').click()


    zip = driver_instance.find_element_by_id('address_Zip')
    zip.send_keys(store[0][5])

    phone_num = driver_instance.find_element_by_id('phone')
    phone_num.send_keys(store[0][6])


    gender = store[0][7]
    sex_path = construct_gender_path(Sex, gender.upper())
    driver_instance.find_element_by_xpath(sex_path).click()


    bday_month = store[0][8]
    month_path = construct_month_path(Month, bday_month.upper())
    driver_instance.find_element_by_xpath(month_path).click()


    bday = driver_instance.find_element_by_id('date_of_birth_day')
    bday.send_keys(store[0][9])

    bday_year = driver_instance.find_element_by_id('date_of_birth_year')
    bday_year.send_keys(store[0][10])

    cable = driver_instance.find_element_by_xpath(
        '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[8]/div[2]/div[1]/select/option[10]').click()


    return driver_instance


# This function opens the driver and completes the entry form
def fill_FN():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.foodnetwork.com/sponsored/sweepstakes/hgtv-dream-home-sweepstakes')
    driver.maximize_window()
    time.sleep(3)

    the_iframe = driver.find_element_by_id('ngxFrame186481')
    driver.switch_to.frame(the_iframe)

    email = driver.find_element_by_id('xReturningUserEmail')
    email.send_keys(store[0][0])


    button = driver.find_element_by_id('xCheckUser')
    button.click()
    time.sleep(3)
    try:
        driver = init_account_info(driver)
    except:
        pass
    try:
        submit = driver.find_element_by_xpath('/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[2]/div/button/span')
        driver.execute_script("arguments[0].click();", submit)
    except:
        pass

    time.sleep(3)



# This function opens the driver and completes the form for hgtv
def fill_HGTV():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.hgtv.com/sweepstakes/hgtv-dream-home/sweepstakes/?ocid=direct')
    driver.maximize_window()
    time.sleep(3)

    iframe = driver.find_element_by_id('ngxFrame186475')
    driver.switch_to.frame(iframe)


    email = driver.find_element_by_id('xReturningUserEmail')
    email.send_keys(store[0][0])

    next = driver.find_element_by_id('xCheckUser').click()
    time.sleep(3)
    try:
        driver = init_account_info(driver)
    except:
        pass
    submit = driver.find_element_by_xpath('/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[2]/div[2]/div/button')
    driver.execute_script("arguments[0].click();",submit)
    time.sleep(3)
    driver.close()


conn = sqlite3.connect('HGTV.db')
c = conn.cursor()
try:
    c.execute("""CREATE TABLE hgtv (
    email text,
    first text,
    last text,
    address text,
    city text,
    zip integer,
    phone_num integer,
    gender text,
    bday_month text,
    bday integer,
    bday_year integer)""")
except:
    pass

user_status = prompt_user_status()
if UserStatus[user_status] == UserStatus.NEW:
    email = input('Enter your email: ')
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    address = input('Enter your address: ')
    city = input('Enter your city: ')
    zip = int(input('Enter your zip: '))
    phone_num = int(input('Enter your phone number: '))
    gender = input('Enter the letter m for male or the letter f for female: ')
    bday_month = input('''
    Type:
    -- jan for January
    -- feb for February
    -- mar for March
    -- apr for April
    -- may for May
    -- jun for June
    -- jul for July
    -- aug for August
    -- sep for September
    -- oct for October
    -- nov for November
    -- dec for December 
    ''')
    bday = int(input('Enter the day of your birthday (only the day): '))
    bday_year = input('Enter your birthyear: ')
    params = (email, first, last, address, city, zip, phone_num, gender, bday_month, bday, bday_year)
    sql = """INSERT INTO hgtv
     (email, first, last, address, city, zip, phone_num, gender, bday_month, bday, bday_year)
     VALUES ('{}','{}','{}', '{}','{}', '{}', '{}', '{}', '{}', '{}','{}');
     """.format(email, first, last, address, city, zip, phone_num, gender, bday_month, bday, bday_year)

    c.execute(sql)
    time.sleep(3)

cont = input('Enter your last name to initiate form completion: ')
c.execute("SELECT * FROM hgtv WHERE last='%s'" % cont)
store = list(c.fetchall())
b_month = store[0][8]

fill_HGTV()
fill_FN()

conn.commit()
conn.close()
