import requests
import json

url = 'https://www.wordreference.com/espt/bueno'

response = requests.get(url)
print(response.status_code)

with open('data.html','w', encoding="utf-8", errors="ignore") as f:
    f.write(str(response.text))
    f.close()

#with open('data.html', 'r', encoding="utf-8", errors="ignore") as f:

newText = response.text[response.text.find("<td class=\'ToWrd\' >")+19:response.text.find("<td class=\'ToWrd\' >")+40]
print(newText[0:newText.find("<em class=")])