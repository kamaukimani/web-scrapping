from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests 
import os
from course import Course

load_dotenv()
class Scrapper:
    def __init__(self):
        self.courses=[]
    def get_page(self):
        url=os.getenv("WEBSITE_URL")
        response=requests.get(url)
        doc=BeautifulSoup(response.text,"html.parser")
        #print(doc)
        return doc 
    def get_courses(self):  
        container=self.get_page().select_one(".\\@4xl\\:grid-cols-3.mt-12.grid.gap-4")           
        return container.find_all("div",recursive=False)
    def make_course(self):
        for page in self.get_courses():
            title=page.select("h3")[0].text
            description=page.select("p")[0].text

            new_course=Course(title,description)
            self.courses.append(new_course)
        return self.courses
    def print_courses(self):
        for course in self.make_course():
            print(course)

scrapper=Scrapper()
#scrapper.get_page()
#print(scrapper.get_courses())
scrapper.print_courses()