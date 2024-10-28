from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Initialize WebDriver
driver = webdriver.Chrome()  
driver.get("https://www.jiosaavn.com/artist/s.-p.-balasubrahmanyam-songs/Ix5AC5h7LSg_")

# page load
wait = WebDriverWait(driver, 10)

# Select "All Languages"
try:
    languages_button = wait.until(EC.clickable_element((By.XPATH, "//button[contains(text(), 'All Languages')]")))
    languages_button.click()
except Exception as e:
    print("Can't select 'All Langs.' filter:", e)

# Scroll and click "Load More" and  load all songs
while True:
    try:
        load_button = wait.until(EC.clickable_element((By.XPATH, "//button[contains(text(), 'Load more')]")))
        load_button.click()
        time.sleep(2)  # Wait  
    except Exception:
        break  # Break loop if "Load more" not available

# collecting song links for "Popular" section As the popular button is 
# selected by default so it will load all popular songs
song_links = []
try:
    songs = driver.find_elements(By.XPATH, "//a[contains(@href, '/song/')]")
    song_links = [song.get_attribute('href') for song in songs]
except Exception as e:
    print("Could not retrieve song links:", e)

# songs with "Aditya Music" copyright

aditya_music_count = 0

# Iterate over each song link to gather copyright info
for song_link in song_links:
    try:
        driver.get(song_link)
        time.sleep(2)  

        # BeautifulSoup to parse the page source
        soup = BeautifulSoup(driver.page_source, "html.parser")
        
        # to finding copyright information
        copyright_info = soup.find(text=lambda x: x and "Aditya Music" in x)
        
        if copyright_info:
            aditya_music_count += 1
    except Exception as e:
        print(f"Can't find copyright info for {song_link}: {e}")

# print the count for "Aditya Music"
print(aditya_music_count)

driver.quit()
