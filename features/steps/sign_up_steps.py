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

@when('Select one of "{options}" from Shares')
def step_impl(context, options):
    WebDriverWait(context.browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id=button-step]')))
    context.browser.execute_script("document.getElementById('form-shares').setAttribute('style', 'inline-block')")
    dd = Select (context.browser.find_element(By.XPATH, "//select[@id='form-shares']"))
    dd.select_by_visible_text(options)

@then('One of the Shares "{options}" is visible')
def step_impl(context, options):
    dd = Select (context.browser.find_element(By.XPATH, "//select[@id='form-shares']"))
    assert dd.first_selected_option.text == options

@when('Select one of "{options}" from Forex')
def step_impl(context, options):
    context.browser.execute_script("document.getElementById('form-forex').setAttribute('style', 'inline-block')")
    dd = Select (context.browser.find_element(By.XPATH, "//select[@id='form-forex']"))
    dd.select_by_visible_text(options)

@then('One of the Forex "{options}" is visible')
def step_impl(context, options):
    dd = Select (context.browser.find_element(By.XPATH, "//select[@id='form-forex']"))
    assert dd.first_selected_option.text == options

@when('Select one of "{options}" from Cfds')
def step_impl(context, options):
    context.browser.execute_script("document.getElementById('form-cfds').setAttribute('style', 'inline-block')")
    dd = Select (context.browser.find_element(By.XPATH, "//select[@id='form-cfds']"))
    dd.select_by_visible_text(options)

@then('One of the Cfds "{options}" is visible')
def step_impl(context, options):
    dd = Select (context.browser.find_element(By.XPATH, "//select[@id='form-cfds']"))
    assert dd.first_selected_option.text == options

@when('Select one of "{options}" from Spread betting')
def step_impl(context, options):
    context.browser.execute_script("document.getElementById('form-spread_betting').setAttribute('style', 'inline-block')")
    dd = Select (context.browser.find_element(By.XPATH, "//select[@id='form-spread_betting']"))
    dd.select_by_visible_text(options)

@then('One of the Spread betting "{options}" is visible')
def step_impl(context, options):
    dd = Select (context.browser.find_element(By.XPATH, "//select[@id='form-spread_betting']"))
    assert dd.first_selected_option.text == options

@when('Select one of "{options}" from Relevante Experience')
def step_impl(context, options):
    context.browser.execute_script("document.getElementById('form-relevant_experience').setAttribute('style', 'inline-block')")
    dd = Select (context.browser.find_element(By.XPATH, "//select[@id='form-relevant_experience']"))
    dd.select_by_visible_text(options)

@then('One of the Relevante Experience "{options}" is visible')
def step_impl(context, options):
    dd = Select (context.browser.find_element(By.XPATH, "//select[@id='form-relevant_experience']"))
    assert dd.first_selected_option.text == options

@when('Select one of "{answer}" from Trading platform')
def step_impl(context, answer):
    context.browser.execute_script("document.getElementById('form-trading_accounts').setAttribute('style', 'inline-block')")
    element = context.browser.find_element(By.XPATH, "//select[@id='form-trading_accounts']")
    element.send_keys(answer)
@then('One of the Trading platform "{answer}" is visible')
def step_impl(context, answer):
    dd = Select(context.browser.find_element(By.XPATH, "//select[@id='form-trading_accounts']"))
    assert  dd.first_selected_option.text == answer

@when('Select one of "{options}" from Currency')
def step_impl(context, options):
    context.browser.execute_script("document.getElementById('form-currency').setAttribute('style', 'inline-block')")
    dd = Select (context.browser.find_element(By.XPATH, "//select[@id='form-currency']"))
    dd.select_by_visible_text(options)

@then('One of the Currency "{options}" is visible')
def step_impl(context, options):
    dd = Select (context.browser.find_element(By.XPATH, "//select[@id='form-currency']"))
    assert dd.first_selected_option.text == options

@when('Select one of "{options}" from Annual Income')
def step_impl(context, options):
    context.browser.execute_script("document.getElementById('form-approx_annual_income').setAttribute('style', 'inline-block')")
    dd = Select (context.browser.find_element(By.XPATH, "//select[@id='form-approx_annual_income']"))
    dd.select_by_visible_text(options)

@then('One of the Annual Income "{options}" is visible')
def step_impl(context, options):
    dd = Select (context.browser.find_element(By.XPATH, "//select[@id='form-approx_annual_income']"))
    assert dd.first_selected_option.text == options

@when('Select one of "{options}" from Employment status')
def step_impl(context, options):
    context.browser.execute_script("document.getElementById('form-employment_status').setAttribute('style', 'inline-block')")
    dd = Select (context.browser.find_element(By.XPATH, "//select[@id='form-employment_status']"))
    dd.select_by_visible_text(options)

@then('One of the Employment status "{options}" is visible')
def step_impl(context, options):
    dd = Select (context.browser.find_element(By.XPATH, "//select[@id='form-employment_status']"))
    assert dd.first_selected_option.text == options

@when('Select one of "{options}" from Assets')
def step_impl(context, options):
    context.browser.execute_script("document.getElementById('form-liquid_savings').setAttribute('style', 'inline-block')")
    dd = Select (context.browser.find_element(By.XPATH, "//select[@id='form-liquid_savings']"))
    dd.select_by_visible_text(options)

@then('One of the Assets "{options}" is visible')
def step_impl(context, options):
    dd = Select (context.browser.find_element(By.XPATH, "//select[@id='form-liquid_savings']"))
    assert dd.first_selected_option.text == options

@when('User clicks on Finish button')
def step_impl(context):
    pass
@then('Error is displayed')
def step_impl(context):
    pass

@when('Select read terms')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, ".checkbox").click()
@then('Read terms checkbox is selected')
def step_impl(context):
    assert not context.browser.find_element(By.CSS_SELECTOR, ".text-red").is_desplayed()