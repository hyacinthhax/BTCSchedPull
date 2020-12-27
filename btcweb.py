import selenium
from selenium.webdriver import Chrome
import time
import schedule
import datetime
from datetime import datetime

dt1 = datetime.now()

def check():
	driver = Chrome()
	with Chrome() as driver:
		driver.get("https://www.coindesk.com/price/bitcoin")
		results = driver.find_element_by_xpath("/html/body/div/div[2]/main/section/div[2]/div[1]/div/section/div/div[1]/div/section/div[1]/div[1]/div[2]/div").text
		results = results + ", " + str(dt1) + "\n"
		with open('btcprice.txt', 'a') as f:
			f.write(results)
			
		driver.close()

check()
schedule.every(60).seconds.do(check)
while True:
	schedule.run_pending()
	time.sleep(1)