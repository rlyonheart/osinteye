import requests
from bs4 import BeautifulSoup
from lib.colors import red,white,reset

def testpypi(self,args):
	response = requests.get(self.url)
	if response.status_code != 200:
		exit(f"{white}[{red}-{white}] testpypi: user not found{reset} ")
	soup = BeautifulSoup(response.text, 'html.parser')
	print('\n\t'+soup.title.string)
	print(soup.main.get_text())
