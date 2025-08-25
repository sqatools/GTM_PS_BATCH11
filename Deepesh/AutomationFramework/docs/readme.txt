# Note : code has to execute from root directory
  e.g. Deepesh/AutomationFramework

# command to execute the automation code
python -m pytest -v -s ./tests/

-v: verbose (detailed information on the console)
-k :  specific test case to execute
-s :  show print statement value on console
-m : marker to execution specific test cases
--html :  provide report file path

