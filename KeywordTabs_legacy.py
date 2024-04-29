from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

keyword = input("Keyword: ")
# keyword = "디아블로"
driver = webdriver.Chrome(options=chrome_options)

# one depth sites

websites = [
    ("https://www.inven.co.kr/search/webzine/news", 'name', 'searchword'),
    ("https://game.donga.com/news/", 'name', 'query'),
    ("https://www.gamechosun.co.kr/webzine/article/news.php", 'name', 'kw'),
    ("https://www.fomos.kr/game", 'name', 'fword'),
    ("https://www.thisisgame.com/", 'name', 'as_q'),
    ("https://www.gamemeca.com/", 'name', 'q'),
    ("http://www.gameshot.net/common/search.php", 'name', 'st'),
    ("https://www.dailygame.co.kr/index.php", 'id', 'sch'),
    ("https://www.ggemguide.com/", 'name', 'searchword'),
    ("https://gamefocus.co.kr/", 'name', 'search_word'),
    ("https://bbs.ruliweb.com/", 'name', 'q'),
    ("https://www.gamey.kr/", 'name', 'sc_word'),
    ("https://konsoler.com/g2/bbs/search.php", 'name', 'q'),
]

for url, attribute, value in websites:
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url)
    search_input = driver.find_element(by=attribute, value=value)
    search_input.send_keys(keyword)
    search_input.send_keys(Keys.RETURN)
    # print("Result URL:", driver.current_url)

# Two depth sites

websites = [
    ('https://www.playforum.net/', 'icon-search-thin', 'name', 'sc_word'),
    ('https://www.gameabout.com/', 'user-allbtn', 'name', 'sc_word'),
    ('https://www.gamevu.co.kr/', 'inptxt', 'name', 'sc_word'),
    ('https://www.gametoc.co.kr/', 'icon-search-thin', 'name', 'sc_word'),
    ('https://game.mk.co.kr/', 'bt_gnb_srch', 'name', 's_keyword'),
    ('https://www.gameple.co.kr/', 'icon-search', 'name', 'sc_word'),
    ('https://www.gameinsight.co.kr/', 'user-allbtn', 'name', 'sc_word'),
    ('http://www.gameand.co.kr/?', 'inptxt', 'name', 'sc_word'),
]

for url, attributeOne, attribute, value in websites:
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url)
    # Find the button element and click on it
    driver.find_element(By.CLASS_NAME, attributeOne).click()
    # Now find the search input element
    search_input = driver.find_element(by=attribute, value=value)
    search_input.send_keys(keyword)
    search_input.send_keys(Keys.RETURN)

# driver.quit()
