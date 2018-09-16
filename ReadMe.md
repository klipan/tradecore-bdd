# tradecore-bdd

This project is written in Pycharm 2018.2 and to make easier to write .feature files install plugin: Gherkin

Suggested tools:
* Python version: 3.7
* Framework: Behave (BDD) used with combination with Page Object Model (POM)
* WebDriver: ChromeWebDriver

Requirements:

install package:
behave  in cmd/terminal type:
```
pip install behave
```
and selenium
```
pip install selenium
```
WebDriver:

The ChromeDriver controls the browser using Chrome's automation proxy framework.
The server expects you to have Chrome installed in the default location for each system:

Download ChromeDriver on this [link](https://chromedriver.storage.googleapis.com/index.html) (version I am currently using is 2.41)

Set path of ChromeWebDriver:

For Linux:

1) Move the file to /usr/bin directory - mv ChromeDriver /usr/bin

2) Go to /usr/bin directory and you would need to run something like "chmod a+x ChromeDriver" to mark it executable.

For Windows:

Paste the ChromeDriver.exe file in "C:\Python\Scripts" Folder.

more detail on [ChromeDriver wiki](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver)

Structure of the project is:

```

└── features
   ├── 1-negative_sign_up.feature
   ├── 2-succcess_sign_up.feature
   ├── 3-questionnaire.feature
   ├── environment.py
   ├── steps
   |   ├── sign_up_steps.py
   |   └── questionnaire_steps.py
   └── pages
       ├── sign_up_page.py
       └── questionnaire_page.py
```

Here's a brief explanation of the files:
* **environment.py**: Define code to run before and after certain events during testing. (starts WebDriver)
* **.feature**: Written test for create account and login, with scenarios an steps.
* **steps/**: This is where Behave will initially look for the code for tests via decorators.
* **pages/**: Use locators and elements in file for implementing steps

To run test case open terminal in project root directory and type:
```
behave
```
