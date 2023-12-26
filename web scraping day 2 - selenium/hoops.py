from selenium import webdriver
from selenium.webdriver.common.by import By

def next_page(browser, n):
	dropdown_parent=browser.find_element(By.CLASS_NAME, "all")
	dropdown_parent.click()
	team_link = browser.find_element(By.CLASS_NAME, 'team-list-ul').find_elements(By.TAG_NAME, 'a')[n]
	team_link.click()

def get_players(browser, players_list):
	players  = browser.find_elements(By.CLASS_NAME, "name")
	for player in players:
		players_list.append(player.text)

def main():
	players_list=[]
	browser = webdriver.Firefox()
	browser.get('https://hoopshype.com/salaries/players/')
	
	get_players(browser,players_list)
	print(len(players_list))

	dropdown_parent = browser.find_element(By.CLASS_NAME, "all")
	dropdown_parent.click()
	dropdown_options = browser.find_elements(By.CLASS_NAME, "team-list-ul")
	team_link = browser.find_element(By.CLASS_NAME, 'team-list-ul').find_elements(By.TAG_NAME, 'a')[1]
	team_link.click()

	get_players(browser,players_list)
	print(len(players_list))

	next_page(browser, 2)

	get_players(browser,players_list)
	print(len(players_list))
	
if __name__ == "__main__":
    main()
