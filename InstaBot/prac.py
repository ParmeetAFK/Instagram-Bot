from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time



driver = webdriver.Firefox(executable_path=r"Z:\InstaBot\drivers\geckodriver.exe")

def scc():
	time.sleep(5)
	sbox = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]")

	lht , ht = 0,1

	while lht != ht:
		lht = ht
		sleep(1)

		ht = driver.execute_script("""
			arguments[0].scrollTo(0 , arguments[0].scrollHeight);
			return arguments[0].scrollHeight;
			""",sbox)

	"""
	last_height = driver.execute_script("return arguments[0].scrollHeight",sbox)
	print(last_height)

	while True:

	    # Scroll down to the bottom.
	    driver.execute_script("window.scrollTo(0, arguments[0].scrollHeight);",sbox)

	    # Wait to load the page.
	    time.sleep(2)

	    # Calculate new scroll height and compare with last scroll height.
	    new_height = driver.execute_script("return arguments[0].scrollHeight",sbox)

	    if new_height == last_height:

	        break

	    last_height = new_height
	"""
driver.get("https://www.instagram.com/accounts/login/?hl=en&source=auth_switcher")
time.sleep(5)
driver.find_element_by_name("username").send_keys("parmeet_0077")
driver.find_element_by_name("password").send_keys("annehathway")
driver.find_element_by_name("password").send_keys(Keys.RETURN)

time.sleep(4)

driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
time.sleep(4)

driver.find_element_by_xpath("//a[contains(@class,'gmFkV')]").click()
time.sleep(4)

driver.find_element_by_xpath("//main[contains(@class,'o64aR')]//li[2]//a[1]").click()  

scc()


"""
JS for Scrolling
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
"""

time.sleep(4)

driver.quit()
