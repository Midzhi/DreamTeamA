import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.youtube.com'

my_html = requests.get(url)

soup = BeautifulSoup(my_html.text, 'html.parser')

my_tag = 'html5-video-player ytp-exp-bottom-control-flexbox ytp-exp-ppp-update ytp-fit-cover-video ytp-hide-info-bar ytp-small-mode ytp-menu-shown ytp-inline-preview-mode ytp-rounded-inline-preview ytp-autonav-endscreen-cancelled-state unstarted-mode ytp-hide-controls'

videos = soup.find('div', class_ = my_tag)

for child in videos.children:
    print(child.text + '\n')

video_content = {}
count = 0
for child in videos.children:
    count += 1
    video_content.update({f'video_{count}': child.text})

with open('video_content.json', 'w') as f:
    json.dump(video_content, f)
