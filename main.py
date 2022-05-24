import requests
import bs4
url=input("Enter your url")
response=requests.get(url)
#print(type(response))
#print(response.text)
filename="temp.html"
bs=bs4.BeautifulSoup(response.text,"html.parser")
formatted_text=bs.prettify()
print(formatted_text)

with open(filename,"w+",encoding='utf-8') as f:
    f.write(formatted_text)
list_img=bs.find_all('img')
print(len(list_img))
