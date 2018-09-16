from behave import then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from features.pages.sign_up_page import Locators
from features.pages.questionnaire_page import Locators_q

@then('User is redirected to a questionnaire')
def step_impl(context):
    #WebDriverWait(context.browser, 15).until(EC.element_to_be_clickable((By.XPATH, "[ng-class='\{\'text-red\'\:field\.\$invalid \&\& form\.\$submitted\}']")))
    title = context.browser.find_element(By.XPATH, Locators_q._path_question_second_page)
    assert title.is_displayed()

@when('Select one of "{options}" from Shares')
def step_impl(context, options):
    WebDriverWait(context.browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locators_q._path_finish_button)))
    context.browser.execute_script(Locators_q._java_script_shares)
    dd = Select (context.browser.find_element(By.XPATH, Locators_q._path_shares))
    dd.select_by_visible_text(options)

@then('One of the Shares "{options}" is visible')
def step_impl(context, options):
    dd = Select (context.browser.find_element(By.XPATH, Locators_q._path_shares))
    assert dd.first_selected_option.text == options

@when('Select one of "{options}" from Forex')
def step_impl(context, options):
    context.browser.execute_script(Locators_q._java_script_forex)
    dd = Select (context.browser.find_element(By.XPATH, Locators_q._path_forex))
    dd.select_by_visible_text(options)

@then('One of the Forex "{options}" is visible')
def step_impl(context, options):
    dd = Select (context.browser.find_element(By.XPATH, Locators_q._path_forex))
    assert dd.first_selected_option.text == options

@when('Select one of "{options}" from Cfds')
def step_impl(context, options):
    context.browser.execute_script(Locators_q._java_script_cfds)
    dd = Select (context.browser.find_element(By.XPATH, Locators_q._path_cfds))
    dd.select_by_visible_text(options)

@then('One of the Cfds "{options}" is visible')
def step_impl(context, options):
    dd = Select (context.browser.find_element(By.XPATH, Locators_q._path_cfds))
    assert dd.first_selected_option.text == options

@when('Select one of "{options}" from Spread betting')
def step_impl(context, options):
    context.browser.execute_script(Locators_q._java_script_spread_betting)
    dd = Select (context.browser.find_element(By.XPATH, Locators_q._path_spread_betting))
    dd.select_by_visible_text(options)

@then('One of the Spread betting "{options}" is visible')
def step_impl(context, options):
    dd = Select (context.browser.find_element(By.XPATH, Locators_q._path_spread_betting))
    assert dd.first_selected_option.text == options

@when('Select one of "{options}" from Relevante Experience')
def step_impl(context, options):
    context.browser.execute_script(Locators_q._java_script_relevante_experience)
    dd = Select (context.browser.find_element(By.XPATH, Locators_q._path_relevante_experience))
    dd.select_by_visible_text(options)

@then('One of the Relevante Experience "{options}" is visible')
def step_impl(context, options):
    dd = Select (context.browser.find_element(By.XPATH, Locators_q._path_relevante_experience))
    assert dd.first_selected_option.text == options

@when('Select one of "{answer}" from Trading platform')
def step_impl(context, answer):
    context.browser.execute_script(Locators_q._java_script_trading_platform)
    element = context.browser.find_element(By.XPATH, Locators_q._path_trading_platform)
    element.send_keys(answer)

@then('One of the Trading platform "{answer}" is visible')
def step_impl(context, answer):
    dd = Select(context.browser.find_element(By.XPATH, Locators_q._path_trading_platform))
    assert  dd.first_selected_option.text == answer

@then('Currency dropdown is displayed')
def step_impl(context):
    assert context.browser.find_element(By.CSS_SELECTOR, "[for='form-currency']").is_displayed()

@when('Select one of "{options}" from Currency')
def step_impl(context, options):
    context.browser.execute_script(Locators_q._java_script_currency)
    dd = Select (context.browser.find_element(By.XPATH, Locators_q._path_currency))
    dd.select_by_visible_text(options)

@then('One of the Currency "{options}" is visible')
def step_impl(context, options):
    dd = Select (context.browser.find_element(By.XPATH, Locators_q._path_currency))
    assert dd.first_selected_option.text == options

@when('Select one of "{options}" from Annual Income')
def step_impl(context, options):
    context.browser.execute_script(Locators_q._java_script_annual_income)
    dd = Select (context.browser.find_element(By.XPATH, Locators_q._path_annual_income))
    dd.select_by_visible_text(options)

@then('One of the Annual Income "{options}" is visible')
def step_impl(context, options):
    dd = Select (context.browser.find_element(By.XPATH, Locators_q._path_annual_income))
    assert dd.first_selected_option.text == options

@when('Select one of "{options}" from Employment status')
def step_impl(context, options):
    context.browser.execute_script(Locators_q._java_script_employment_status)
    dd = Select (context.browser.find_element(By.XPATH, Locators_q._path_employment_status))
    dd.select_by_visible_text(options)

@then('One of the Employment status "{options}" is visible')
def step_impl(context, options):
    dd = Select (context.browser.find_element(By.XPATH, Locators_q._path_employment_status))
    assert dd.first_selected_option.text == options

@when('Select one of "{options}" from Assets')
def step_impl(context, options):
    context.browser.execute_script(Locators_q._java_script_assets)
    dd = Select (context.browser.find_element(By.XPATH, Locators_q._path_assets))
    dd.select_by_visible_text(options)

@then('One of the Assets "{options}" is visible')
def step_impl(context, options):
    dd = Select (context.browser.find_element(By.XPATH, Locators_q._path_assets))
    assert dd.first_selected_option.text == options

@when('Select read terms')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, ".checkbox").click()
@when('Click Finish')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, "#button-step").click()
@then('Test is done')
def step_impl(context):
    WebDriverWait(context.browser, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#base\.portal\.account-add')))
    assert context.browser.title == "TradeCore - Account"