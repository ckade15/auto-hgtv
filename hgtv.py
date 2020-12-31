# HGTV/Food Network 2021 Home Giveaway Entry Bot
# Stores information in a database so all you have to do to fill out both forms
# after originally entering all of your information is type your last name

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sqlite3

# This function stores all of the information to input if it
# is the users first time entering the contest for the Food Network
def init_FN():
    first = driver.find_element_by_id('name_Firstname')
    first.send_keys(store[0][1])
    time.sleep(3)
    last = driver.find_element_by_id('name_Lastname')
    last.send_keys(store[0][2])
    time.sleep(3)
    address = driver.find_element_by_id('address_Address1')
    address.send_keys(store[0][3])
    time.sleep(3)
    city = driver.find_element_by_id('address_City')
    city.send_keys(store[0][4])
    time.sleep(3)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[4]/div[2]/div[4]/div[1]/select/option[24]').click()
    time.sleep(3)
    zip = driver.find_element_by_id('address_Zip')
    zip.send_keys(store[0][5])
    time.sleep(3)
    phone_num = driver.find_element_by_id('phone')
    phone_num.send_keys(store[0][6])
    time.sleep(3)
    gender = store[0][7]
    if gender == 'm':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[6]/div[2]/div[2]/input').click()
    elif gender == 'f':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[6]/div[2]/div[1]/input').click()
    time.sleep(3)
    bday_month = store[0][8]
    if bday_month == 'jan':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[2]').click()
    elif bday_month == 'feb':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[4]').click()
    elif bday_month == 'mar':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[4]').click()
    elif bday_month == 'apr':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[5]').click()
    elif bday_month == 'may':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[6]').click()
    elif bday_month == 'jun':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[7]').click()
    elif bday_month == 'jul':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[8]').click()
    elif bday_month == 'aug':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[9]').click()
    elif bday_month == 'sep':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[10]').click()
    elif bday_month == 'oct':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[11]').click()
    elif bday_month == 'nov':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[12]').click()
    elif bday_month == 'dec':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[13]').click()
    time.sleep(3)
    bday = driver.find_element_by_id('date_of_birth_day')
    bday.send_keys(store[0][9])
    time.sleep(3)
    bday_year = driver.find_element_by_id('date_of_birth_year')
    bday_year.send_keys(store[0][10])
    time.sleep(3)
    cable = driver.find_element_by_xpath(
        '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[8]/div[2]/div[1]/select/option[10]').click()
    time.sleep(3)

# This function opens the driver and completes the entry form
def fill_FN():
    driver = webdriver.Chrome(r'') # I left the path for the webdriver empty for you to copy your path to the specific chrome driver
    driver.get('https://www.foodnetwork.com/sponsored/sweepstakes/hgtv-dream-home-sweepstakes')
    driver.maximize_window()
    time.sleep(3)
    the_iframe = driver.find_element_by_id('ngxFrame186481')
    driver.switch_to.frame(the_iframe)
    email = driver.find_element_by_id('xReturningUserEmail')
    email.send_keys(store[0][0])
    time.sleep(3)
    button = driver.find_element_by_id('xCheckUser')
    button.click()
    time.sleep(3)
    try:
        init_FN()
    except:
        pass
    submit = driver.find_element_by_xpath('/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[2]/div/button/span').click()
    time.sleep(3)
    driver.close()

# This function stores all of the information if it is the users
# first time entering the contest
def init_HGTV():
    first = driver.find_element_by_id('name_Firstname')
    first.send_keys(store[0][1])
    time.sleep(3)
    last = driver.find_element_by_id('name_Lastname')
    last.send_keys(store[0][2])
    time.sleep(3)
    address = driver.find_element_by_id('address_Address1')
    address.send_keys(store[0][3])
    time.sleep(3)
    city = driver.find_element_by_id('address_City')
    city.send_keys(store[0][4])
    time.sleep(3)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[4]/div[2]/div[4]/div[1]/select/option[24]').click()
    time.sleep(3)
    zip = driver.find_element_by_id('address_Zip')
    zip.send_keys(store[0][5])
    time.sleep(3)
    phone_num = driver.find_element_by_id('phone')
    phone_num.send_keys(store[0][6])
    time.sleep(3)
    gender = store[0][7]
    if gender == 'm':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[6]/div[2]/div[2]/input').click()
    elif gender == 'f':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[6]/div[2]/div[1]/input').click()
    time.sleep(3)
    bday_month = store[0][8]
    if bday_month == 'jan':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[2]').click()
    elif bday_month == 'feb':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[4]').click()
    elif bday_month == 'mar':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[4]').click()
    elif bday_month == 'apr':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[5]').click()
    elif bday_month == 'may':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[6]').click()
    elif bday_month == 'jun':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[7]').click()
    elif bday_month == 'jul':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[8]').click()
    elif bday_month == 'aug':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[9]').click()
    elif bday_month == 'sep':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[10]').click()
    elif bday_month == 'oct':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[11]').click()
    elif bday_month == 'nov':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[12]').click()
    elif bday_month == 'dec':
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[7]/div[2]/div[1]/select/option[13]').click()
    time.sleep(3)
    bday = driver.find_element_by_id('date_of_birth_day')
    bday.send_keys(store[0][9])
    time.sleep(3)
    bday_year = driver.find_element_by_id('date_of_birth_year')
    bday_year.send_keys(store[0][10])
    time.sleep(3)
    cable = driver.find_element_by_xpath('/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[1]/div[1]/div/fieldset/div[8]/div[2]/div[1]/select/option[10]').click()
    time.sleep(3)

# This function opens the driver and completes the form for hgtv
def fill_HGTV():
    driver = webdriver.Chrome(r'') # I left the path for the webdriver empty for you to copy your path to the specific chrome driver
    driver.get('https://www.hgtv.com/sweepstakes/hgtv-dream-home/sweepstakes/?ocid=direct')
    driver.maximize_window()
    time.sleep(3)
    iframe = driver.find_element_by_id('ngxFrame186475')
    driver.switch_to.frame(iframe)
    time.sleep(3)
    email = driver.find_element_by_id('xReturningUserEmail')
    email.send_keys(store[0][0])
    next = driver.find_element_by_id('xCheckUser').click()
    try:
        init_HGTV()
    except:
        pass
    submit = driver.find_element_by_xpath(
        '/html/body/div[1]/div/main/section/div/div/div/div/div/div[1]/div/div[2]/form[2]/div[2]/div/button').click()
    time.sleep(10)
    driver.close()



first_use = input('''
Made by Chris Kade
This program allows you to sign up for the HGTV giveaway without having
to go through the hassle of manually entering all of the information.
--- If this is your first time using this program, type the letter f. 
--- If you're already in the database type the letter c.
''')
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
if first_use == 'f':
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
