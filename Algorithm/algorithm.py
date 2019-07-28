from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import os
from random import choice
from string import ascii_uppercase
from multiprocessing.pool import ThreadPool
import time

start = time.time()
count = 1
def fetch_url(entry):
	print("Downloadig...")
	url= entry
	#path_suffix = ''.join(choice(ascii_uppercase) for i in range(8))
	global count
	path_suffix = str(count)
	count += 1
	path = "./katrinakaif/"+path_suffix+".jpg"
	if not os.path.exists(path):
		r =  requests.get(url, stream= True)
		if r.status_code ==200:
			with open(path, 'wb') as f:
				for chunk in r:
					f.write(chunk)
	return path

url = "https://www.instagram.com/katrinakaif/"
options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome("/usr/bin/chromedriver",chrome_options=options)

print("Getting webpage")
driver.get(url)
print("Webpage  downloaded")

end = time.time()
print("Time elapsed till now:", end-start)


print("Extracting image tags")
images = set([])

images_tag = driver.find_elements_by_class_name('FFVAD')
for img in images_tag:
	images.add(img.get_attribute("src"))

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

images_tag = driver.find_elements_by_class_name('FFVAD')
for img in images_tag:
        images.add(img.get_attribute("src"))


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

images_tag = driver.find_elements_by_class_name('FFVAD')
for img in images_tag:
        images.add(img.get_attribute("src"))

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

images_tag = driver.find_elements_by_class_name('FFVAD')
for img in images_tag:
        images.add(img.get_attribute("src"))

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

images_tag = driver.find_elements_by_class_name('FFVAD')
for img in images_tag:
	images.add(img.get_attribute("src"))


#print(images)
sample_size = list(images)

#for entry in sample_size:
#	fetch_url(entry)

print("Downloading photos")
results = ThreadPool(10).imap_unordered(fetch_url, sample_size)

print("Paths of downloaded photos")
for path in results:
	print(path)
end = time.time()
print("Time elapsed:",end-start)



