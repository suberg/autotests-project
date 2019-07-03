# Config:
- `conftest.py` -- config file for the tests

# How to execute the tests:
- `pytest -s -v --tb=line test_items.py` - execute tests with default parameters.

- `pytest -s -v --tb=line --language="ru" test_items.py` - execute tests with a custom language parameter. The default parameter value is "en".

- `pytest -s -v --tb=line --browser=firefox --language="en" test_items.py` - execute tests in a specific browser with a default language parameter. The default browser is Chrome. You can select between `chrome` and `firefox`.

- `pytest -s -v --tb=line -m login_guest test_items.py` - execute tests that marks as `login_guest`.