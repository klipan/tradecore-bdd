from behave import step, then, given, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('Go to Tradecore site')
def step_impl(context):
    context.browser.get("https://demo-biq.dev.tradecore.io/#/")
    WebDriverWait(context.browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#button-step')))

@when('Click Next')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, '#button-step').click()
@then('Required fields become red')
def step_impl(context):
    assert context.browser.find_element(By.CSS_SELECTOR, "[class='help-block ng-active']").text == "THIS FIELD IS REQUIRED"
@when('Enter "{email}"')
def step_impl(context, email):
    element = context.browser.find_element(By.CSS_SELECTOR, "[id=form-email]")
    element.clear()
    element.send_keys(email)
@then('Email field throws an error')
def step_impl(context):
    assert context.browser.find_element(By.XPATH, "//div[contains(text(), 'This field is not valid')]").is_displayed()
    context.browser.find_element(By.CSS_SELECTOR, "[id=form-email]").clear()
@when('Type "{password}"')
def step_impl(context, password):
    element = context.browser.find_element(By.CSS_SELECTOR, '[id=form-password]')
    element.clear()
    element.send_keys(password)
@then('Password field throws an error')
def step_impl(context):
    assert context.browser.find_element(By.XPATH, "//div[contains(text(), 'Password must be 6 to 15')]").is_displayed()

@when('Enter "{phone}" number')
def step_impl(context, phone):
    element = context.browser.find_element_by_css_selector("[id=form-telephone]")
    element.clear()
    element.send_keys(phone)
@then('Phone number field throws an error')
def step_impl(context):
    assert context.browser.find_element(By.CSS_SELECTOR, "[class='help-block ng-active']").text == "THIS FIELD IS REQUIRED"
@when('Enter "{dial_code}" to phone number field')
def step_impl(context, dial_code):
    element = context.browser.find_element_by_css_selector("[id=form-telephone]")
    element.clear()
    element.send_keys(dial_code)
@then('Flag does not show up')
def step_impl(context):
    element = context.browser.find_element(By.CSS_SELECTOR, ".selected-flag")
    assert element.get_attribute("title") == "Unknown"
@when('Enter Cuban dial code in phone field')
def step_impl(context):
    element = context.browser.find_element_by_css_selector("[id=form-telephone]")
    element.clear()
    element.send_keys("53")
@then('Cuban flag shows up')
def step_impl(context):
    element = context.browser.find_element(By.CSS_SELECTOR, ".selected-flag")
    assert element.get_attribute("title") == "Cuba: +53"

@when('Leave date of birth field empty')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, "#form-date_of_birth").send_keys(" ")
@then('Error message is showing')
def step_impl(context):
    assert context.browser.find_element(By.CSS_SELECTOR,"[class='help-block ng-active']").text == "THIS FIELD IS REQUIRED"
@when('Enter "{date}" in date of birth field')
def step_impl(context, date):
    date = context.browser.find_element(By.CSS_SELECTOR, ".posr [name='date_of_birth']")
    date.clear()
    date.send_keys(date)
@then('Phone field return an error message')
def step_impl(context):
    pass#assert context.browser.find_element(By.CSS_SELECTOR,"[ng-switch-when] [ng-message]").text == "THIS FIELD IS NOT VALID"




@when('Enter all required fields')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, ".posr [name='first_name']").send_keys("Nikola")
    context.browser.find_element(By.CSS_SELECTOR, ".posr [name='last_name']").send_keys("Klipa")
    email = context.browser.find_element(By.CSS_SELECTOR, "[id=form-email]")
    email.clear()
    email.send_keys("test@tradecore.com")
    password = context.browser.find_element(By.CSS_SELECTOR, '[id=form-password]')
    password.clear()
    password.send_keys("test11")
@then('User is redirected to questionnaire')
def step_impl(context):
    pass
