class Rev:
    def reverse(self, text):
        return " ".join(text.split()[::-1])

o=Rev()
print(o.reverse("hello .py"))
