#Yanira Manzano
#22/11/2019

from textbooks import Textbooks

book1 = Textbooks(title="Being A Scholar", first="Michael", last="Smith", age=22, edition="First", ISBN=123456, publisher="Scholar Press", year=2019, inventory=1000, price="$10")
book2 = Textbooks(title="Being A Scholar", first="Michael", last="Smith", age=25, edition="Second", ISBN=246810, publisher="Scholar Press", year=2022, inventory=2000, price="$20")
book3 = Textbooks(title="Being A Scholar", first="Michael", last="Smith", age=28, edition="Third", ISBN=369121, publisher="Scholar Press", year=2025, inventory=3000, price="$30")

print("""Hello user! Which book would you select today?
(Enter 1 for Book One/ 2 for Book Two/ 3 for Book Three""")
chose = input("> ")
if chose == "1":
    print("Your have selected Book 1. Here is the content within it")
    print(book1)
elif chose == "2":
    print("Your have selected Book 2. Here is the content within it")
    print(book2)
elif chose == "3":
    print("Your have selected Book 3. Here is the content within it")
    print(book3)
