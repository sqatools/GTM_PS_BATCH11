# Note : code has to execute from root directory
  e.g. Deepesh/AutomationFramework

# command to execute the automation code
python -m pytest -v -s ./tests/

-v: verbose (detailed information on the console)
-k :  specific test case to execute
-s :  show print statement value on console
-m : marker to execution specific test cases
--html :  provide report file path


# command to execute the automation with headless from command line option.
python -m pytest -v .\tests\fb_page\test_fb_functionality_headless.py --browserName="edge"  --headlessValue=False

# command to install html report
# ->  pip install pytest-html
# python -m pytest -v .\tests\test_fun\ --browserName=firefox --html=logs/report.html



