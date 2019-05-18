
Python Selenium FDN Web Automation
===
## Description
It's a web automation project in Page Object design pattern, developed in Python & Selenium. Take *test_runner.py* as a entry of project to concatenate Page Objects, Automation Scripts.

## Python Env
* python 3.7

## Dependencies
* Selenium
    ```
    pip install selenium
    ```


## Project Structure
```
project
│   README.md
│   test_runner.py
│
└───configure
│   │   __init__.py
│   │   config.ini
│
└───driver
|   │   (Download the driver correspond to OS)
|   │   chromedriver
|   |   geckodriver
|
└───pages
|   |   __init__.py
|
└───testcases
|   |   __init__.py
|   |   driver.py
|   |   case01.py
│   |   case02.py
...
```

## Features
* **configure/ :** store the config
* **driver/ :** put driver binary of browser
* **pages/ :** implementation of Page Object
* **testcases/ :** put automation scripts
