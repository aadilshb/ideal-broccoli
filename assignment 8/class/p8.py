class String1:
    def __init__(self):
        self.text=""

    def get_string(self, text):
        self.text=text

    def print_string(self):
        print(self.text[::-1])

o=String1()
o.get_string("Hello racecar")
o.print_string()
