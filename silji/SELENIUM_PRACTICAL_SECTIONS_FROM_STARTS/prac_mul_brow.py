from selenium import webdriver
import time

# Initialize the WebDriver (e.g., using Chrome)
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Open the first URL
driver.get("https://www.facebook.com")
print("Current tab URL:", driver.current_url)

# Save the original window handle
original_tab = driver.current_window_handle

# Open a new tab using JavaScript (useful for browsers like Chrome)
driver.execute_script("window.open('https://www.google.com', '_blank');")

# Get the list of all window handles (tabs)
window_handles = driver.window_handles
print("All window handles:", window_handles)

# Switch to the new tab
driver.switch_to.window(window_handles[1])
print("Switched to new tab URL:", driver.current_url)

# Pause for a few seconds (optional)
time.sleep(2)
# close google page
driver.close()

# Switch back to the original tab
driver.switch_to.window(original_tab)
print("Switched back to original tab URL:", driver.current_url)

time.sleep(2)

# Close the browser
driver.quit()