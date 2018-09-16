import random
import string


class Locators(object):

    _next_button = '#button-step'
    _path_error_required = "[class='help-block ng-active']"
    _path_error_not_valid = "//div[contains(text(), 'This field is not valid')]"
    _path_error_not_valid_2 = "[ng-switch-when] [ng-message]"
    _path_error_password = "//div[contains(text(), 'Password must be 6 to 15')]"
    _path_email = "[id=form-email]"
    _path_password = '[id=form-password]'
    _path_telephone = "[id=form-telephone]"
    _path_flag = ".selected-flag"
    _path_date_of_birth = "#form-date_of_birth"
    _path_country_dropdown = "[id=form___fieldId___chosen]"
    _path_first_name = "[id=form-first_name]"
    _path_last_name = "[id=form-last_name]"
    _path_address = "[id=form-addr_street]"
    _path_zip_code = "[id=form-addr_zip]"
    _path_city = "[id=form-addr_city]"

class Elements(object):

    _URL = "https://demo-biq.dev.tradecore.io/#/"
    _error_message_required = "THIS FIELD IS REQUIRED"
    _error_message_not_valid = "THIS FIELD IS NOT VALID"
    _first_name = "Nikola"
    _last_name = "Klipa"
    _cuban_code_flag = "Cuba: +53"
    random_string = ''.join([random.choice(string.ascii_letters.lower() + string.digits) for n in range(8)])
    _email = random_string + "@tradecore.com"
    _password = "Test11"
    _telephone = "+381658700045"
    _date_of_birth = "19/12/1987"
    _country = "Serbia"
    _zip_code = "11070"
    _address = "Bore Markovica 13-15"
    _city = "Belgrade"