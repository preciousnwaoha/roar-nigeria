# import random
# # fun = lambda x, y : print(random.randint(x, y))
# # fun(1000, 100000)

# pythagoras
# import math
# (lambda x, y : print(math.sqrt((x**2) + (y**2))))(float(input("Enter side 1: ")), float(input("Enter side 2: ")))


appliances = {
    "Bulbs": 18,
    "Air_Conditioners": 200,
    "Electric_Cookers": 1,
    "Fridges": 30,
    "Irons": 1
}
def power():
    pow = 0
    for app in appliances:
        x = float(input(app))
        pow = pow + (appliances[app] * x)
    print(pow)
power()


# fibonacci

# def fibo(end):
#     a, num, = 1, 0
#     while num <= end:
#         print(num)
#         b = num
#         num = num + a
#         a = b
# fibo(1000000)

# def recurFibo(end):
#     print(end)
#     if end == 0:
#         return 0
#     else:
#         return recurFibo(end - 2)
# recurFibo(30)


# bulbs, airConditioners, electricCookers, fridges, irons  = 18, 200, 1, 3, 1
# def power():
#     pow = 0
#     for x in range(5):
#         appliance, value  = input("appliance: "), float(input("value: "))
#         if appliance == "bulbs":
#             pow = pow + (bulbs * value)
#         elif appliance == "air conditioner":
#             pow = pow + (airConditioners * value)
#         elif appliance == "electric cooker":
#             pow = pow + (electricCookers * value)
#         elif appliance == "fridge":
#             pow = pow + (fridges * value)
#         elif appliance == "iron":
#             pow = pow + (irons * value)
#         else:
#             pow = pow * 1
#     print(pow)
# power()

