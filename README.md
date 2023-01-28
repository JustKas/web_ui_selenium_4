# This is the POC:
* web ui tests (selenium version - 4)
* fixtures for 3 browsers (Chrome, Safari, Firefox)
* method for search a shadow element
* base report

## Project requirements
* `python3 version` - 3.10.4
* `pip` - for python3
* `virtualenv` -  - for python3

### Install virtualenv
#### PAY ATTENTION: For correct creating venv with python 3.10 need to update virtualenv
```commandline
python3.10 -m pip install virtualenv
```


### Install requirements
```commandline
python3 -m pip install -r requirements. txt
```

### Run tests with report
```commandline
pytest --capture=no --verbose --html=pytest_selenium_test_report.html main.py
```
