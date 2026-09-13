from bs4 import BeautifulSoup
html=""
with open("yess.html") as file:
    html=file.read()

kicker=BeautifulSoup(html,"html.parser")
#print(kicker)
def get_kickers():
    projects=kicker.select("li.project.grid_4")[0]
    title=projects.select("h2.bbcard_name strong a")[0].text
    image=projects.select("div.project-thumbnail a img")[0]["src"]
    description=projects.select("p.bbcard_blurb")[0].text
    location=projects.select(".location-name")[0].text
    funded=projects.select("ul.project-stats li.first.funded strong")[0].text.replace("%","")
    return funded
print(get_kickers())

def create_projects():
    projects={}
    for project in kicker.select("li.project.grid_4"):
        title=project.select("h2.bbcard_name strong a")[0].text
        projects[title]={
            "image_link":project.select("div.project-thumbnail a img")[0]["src"],
            "description":project.select("p.bbcard_blurb")[0].text,
            "location":project.select(".location-name")[0].text,
            "funded":project.select("ul.project-stats li.first.funded strong")[0].text.replace("%",""),
        }
    return projects

print(create_projects())