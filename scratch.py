# # Dictionamry
# # #
# # # dict = {
# # #     "name": "precious",
# # #     "age": 20,
# # #     "stack": "Full"
# # # }
# # # for key, value in dict.items():
# # #     print(key, value)
# # #
# # # dict.pop("age")
# # # dict["networth"] = 1000000
# # # if "networth" in dict:
# # #     print(dict.get("networth"))
# # #     print(len(dict))
# # # print(dict.items())
#
# if statements
#
# Project 1 - Prime numbers
#
# def primeNums(a, b):
#     arr = list(range(a, b))
#
#     for x in arr:
#         prime = True
#         for y in list(range(1, x)):
#             if ((x % y) == 0) and (y != 1):
#                 prime = False
#         if prime == True:
#             print(x)
# primeNums(1, 100)
#
# # Countries
#
# class Countries:
#     def __init__(self, name, code, flag, slogan):
#         self.name = name
#         self.code = code
#         self.flag = flag
#         self.slogan = slogan=
#
# country1 = Countries("Nigeria", 234, ["green", "white"], "Peace and Unity")
# country2 = Countries("US", 555, ["red", "white", "blue"], "Freedom City")
# country3 = Countries("Brazil", 99, ["yellow", "green", "blue"], "Footbal frenzy")
#
# def getCountryInfo(country, info):
#     print(country.name) if info == "name" else print(country.code) if info == "code" else print(country.flag) if info == "flag" else print(country.slogan) if info == "slogan" else print("Invalid input")
#
#
#
# getCountryInfo(country2, "slogan")
#
# getCountryInfo(country2, "flag")
# getCountryInfo(country3, "name")
# getCountryInfo(country1, "code")
#
# RegExp in Python
# import re
#
# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)
#

#
#
# IT Lecture
# if 4 == 4.4:
#     print("hey")
# else:
#     print("go")
# print("hello")
#
# import math
# def volumeofsphere(r):
#     return ((4/3) * math.pi * (r*r*r))
#
# print("Volume is", volumeofsphere(9))
#
# # def cakeSize(r, h):
#
#
#
# import math
#
# def cakeFlavour(flavour, size):
#     if flavour == "vanilla" and size < 10000:
#         print("Available")
#     elif flavour == "choco" and size < 10000:
#         print("Available")
#     elif flavour == "fruit" and size < 10000:
#         print("Available")
#     else:
#         print("We no get am")
#
# def cakeSize():
#     flavour = input("Cake Falvour: ")
#     r = int(input("Enter the radius: "))
#     h = int(input("Enter the Volume: "))
#     if r > 30 and h > 80:
#         return "Can't bake such large cake"
#     else:
#         size = (4/3) * math.pi * (r**r) * h
#         return cakeFlavour(flavour, size)
# cakeSize()
#


# import pywhatkit
# pywhatkit.sendwhatmsg("+2348121170077", "hello", 15, 15)
