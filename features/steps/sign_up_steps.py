from behave import then, given, when
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from features.pages.sign_up_page import Locators, Elements


@given('Go to Tradecore site')
def step_impl(context):
    context.browser.get(Elements._URL)
    WebDriverWait(context.browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators._next_button)))

@when('Click Next')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, Locators._next_button).click()
@then('Required fields become red')
def step_impl(context):
    assert context.browser.find_element(By.CSS_SELECTOR, Locators._path_error_required).text == Elements._error_message_required
@when('Enter "{email}"')
def step_impl(context, email):
    element = context.browser.find_element(By.CSS_SELECTOR, Locators._path_email)
    element.clear()
    element.send_keys(email)
@then('Email field throws an error')
def step_impl(context):
    assert context.browser.find_element(By.XPATH, Locators._path_error_not_valid).is_displayed()
    context.browser.find_element(By.CSS_SELECTOR, Locators._path_email).clear()
@when('Type "{password}"')
def step_impl(context, password):
    element = context.browser.find_element(By.CSS_SELECTOR, Locators._path_password)
    element.clear()
    element.send_keys(password)
@then('Password field throws an error')
def step_impl(context):
    assert context.browser.find_element(By.XPATH, Locators._path_error_password).is_displayed()

@when('Enter "{phone}" number')
def step_impl(context, phone):
    element = context.browser.find_element(By.CSS_SELECTOR, Locators._path_telephone)
    element.clear()
    element.send_keys(phone)
@then('Phone number field throws an error')
def step_impl(context):
    assert context.browser.find_element(By.CSS_SELECTOR, Locators._path_error_required).text == Elements._error_message_required
@when('Enter "{dial_code}" to phone number field')
def step_impl(context, dial_code):
    element = context.browser.find_element(By.CSS_SELECTOR, Locators._path_telephone)
    element.clear()
    element.send_keys(dial_code)
@then('Flag does not show up')
def step_impl(context):
    element = context.browser.find_element(By.CSS_SELECTOR, Locators._path_flag)
    assert element.get_attribute("title") == "Unknown"
@when('Enter Cuban dial code in phone field')
def step_impl(context):
    element = context.browser.find_element(By.CSS_SELECTOR, Locators._path_telephone)
    element.clear()
    element.send_keys("53")
@then('Cuban flag shows up')
def step_impl(context):
    element = context.browser.find_element(By.CSS_SELECTOR, Locators._path_flag)
    assert element.get_attribute("title") == Elements._cuban_code_flag
@when('Leave date of birth field empty')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, Locators._path_date_of_birth).send_keys(" ")
@then('Error message is showing')
def step_impl(context):
    assert context.browser.find_element(By.CSS_SELECTOR,Locators._path_error_required).text == Elements._error_message_required
@when('Enter "{date}" in date of birth field')
def step_impl(context, date):
    date_of_birth = context.browser.find_element(By.CSS_SELECTOR, Locators._path_date_of_birth)
    date_of_birth.clear()
    date_of_birth.send_keys(date)
@then('Phone field returns an error message')
def step_impl(context):
    assert context.browser.find_element(By.CSS_SELECTOR,"[ng-switch-when] [ng-message]").text == Elements._error_message_not_valid
@when('Enter "{address}" in Address line 1 field')
def step_impl(context, address):
    element = context.browser.find_element(By.CSS_SELECTOR, Locators._path_address)
    element.clear()
    element.send_keys(address)
@then("Address field returns an error message")
def step_impl(context):
    assert context.browser.find_element(By.CSS_SELECTOR,"[ng-switch-when] [ng-message]").text == Elements._error_message_not_valid

@when('Enter all required fields')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, Locators._path_first_name).send_keys(Elements._first_name)
    context.browser.find_element(By.CSS_SELECTOR, Locators._path_last_name).send_keys(Elements._last_name)
    
    email = context.browser.find_element(By.CSS_SELECTOR, Locators._path_email)
    email.clear()
    email.send_keys(Elements._email)
    
    password = context.browser.find_element(By.CSS_SELECTOR, Locators._path_password)
    password.clear()
    password.send_keys(Elements._password)
    
    phone = context.browser.find_element(By.CSS_SELECTOR, Locators._path_telephone)
    phone.clear()
    phone.send_keys(Elements._telephone)
    
    date = context.browser.find_element(By.CSS_SELECTOR, Locators._path_date_of_birth)
    date.clear()
    date.send_keys(Elements._date_of_birth)

    context.browser.find_element_by_css_selector("[id=form___fieldId___chosen]").click()
    country = context.browser.find_element_by_css_selector("#form___fieldId___chosen [type]")
    country.send_keys(Elements._country)
    country.send_keys(Keys.ENTER)
    
    context.browser.find_element(By.CSS_SELECTOR, Locators._path_zip_code).send_keys(Elements._zip_code)

    address = context.browser.find_element(By.CSS_SELECTOR, Locators._path_address)
    address.clear()
    address.send_keys(Elements._address)

    context.browser.find_element(By.CSS_SELECTOR, Locators._path_city).send_keys(Elements._city)

    context.browser.find_element(By.CSS_SELECTOR, Locators._next_button).click()
@then('User is redirected to a questionnaire')
def step_impl(context):
    #WebDriverWait(context.browser, 15).until(EC.element_to_be_clickable((By.XPATH, "[ng-class='\{\'text-red\'\:field\.\$invalid \&\& form\.\$submitted\}']")))
    title = context.browser.find_element(By.XPATH, "//*[contains(text(), 'Have you traded')]")
    assert title.is_displayed()

@when('Select one of Frequently from Shares')
def step_impl(context):
    WebDriverWait(context.browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id=button-step]')))
    context.browser.execute_script("document.getElementById('form-shares').setAttribute('style', 'inline-block')")

    context.browser.find_element(By.XPATH, "//*[@id='form___fieldId___chosen']/a").click()
    context.browser.find_element(By.XPATH, "//*[@id='form___fieldId___chosen']/a/span").click()
@then('One of the Shares dropdown Frequently will be visible')
def step_impl(context):
    pass# dropdown = context.browser.find_element(By.CSS_SELECTOR, "")
    #assert dropdown.select_by_visible_text(answers)