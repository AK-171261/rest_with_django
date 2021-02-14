word = "Wikipedia (/ˌwɪkɪˈpiːdiə/ (About this soundlisten) wik-ih-PEE-dee-ə or /ˌwɪki-/ (About this soundlisten) wik-ee-) is a free, multilingual open-collaborative online encyclopedia created and maintained by a community of volunteer editors using a wiki-based editing system. It is one of the 15 most popular websites as ranked by Alexa, as of January 2021[3] and The Economist newspaper placed it as the 13th-most-visited place on the web.[4] Featuring no advertisements, it is hosted by the Wikimedia Foundation, an American non-profit organization funded primarily through donations"
import re

word_lst = [re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", file) for file in word]
res = "".join(word_lst)

word_lst = res.split(" ")
x_dict = {}
for i in word_lst:
    if i in x_dict.keys():
        x_dict[i] += 1
    else:
        x_dict[i] = 1
x = sorted(x_dict.items(), key=lambda x: x[1], reverse=True)[0][1]
print(x)

# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     def fullname(self):
#         print(self.name + " " + str(self.age))

#     @classmethod
#     def parsing(cls, st):
#         name, age, salary = st.split('-')
#         return cls(name, age, salary)
#
#
# obj = Employee("Anand", 20, 20000)
# obj.fullname()
