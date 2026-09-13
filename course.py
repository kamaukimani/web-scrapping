class Course:
    def __init__(self,title,description):
        self.title=title
        self.description=description

    def __str__(self):
        output=""
        output +=f"{self.title}\n{self.description}\n"
        output +="......................"
        return output