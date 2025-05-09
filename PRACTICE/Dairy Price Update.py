# class DairyProduct:
#     def __init__(self, id, brand, type, price, grade):
#         self.id = id
#         self.brand = brand
#         self.type = type
#         self.price = price
#         self.grade = grade

#     def update_price_and_grade(self, price, grade):
#         self.price = price
#         self.grade = grade


# class ProductGrade:
#     def __init__(self, dairyList, weightageDict):
#         self.dairyList = dairyList
#         self.weightageDict = weightageDict

#     def priceBasedOnBrandAndType(self, brand, type):
#         matched = []
#         for product in self.dairyList:
#             if product.brand.lower() == brand.lower() and product.type.lower() == type.lower():
#                 weight = self.weightageDict.get(product.grade, 0)
#                 updated_price = product.price + (product.price * weight / 100)
#                 product.price = updated_price
#                 matched.append(product)
#         return matched if matched else None


# # Main Program
# dairyList = []
# n = int(input())
# for _ in range(n):
#     id = int(input())
#     brand = input()
#     type = input()
#     price = float(input())
#     grade = input()
#     dairyList.append(DairyProduct(id, brand, type, price, grade))

# d = int(input())
# weightageDict = {}
# for _ in range(d):
#     key = input()
#     value = int(input())
#     weightageDict[key] = value

# brand = input()
# type = input()

# pg = ProductGrade(dairyList, weightageDict)
# result = pg.priceBasedOnBrandAndType(brand, type)

# if result:
#     for prod in result:
#         print(f"{prod.brand} {prod.price}")
# else:
#     print("No dairy product found")
