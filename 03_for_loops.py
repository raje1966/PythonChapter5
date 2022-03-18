# # for letter in "Rajendra Kulkarni":
# #     print(letter)
# vegetables = ["onions", "cabbage", "parsley", "cucumber"]
# for vegetable in vegetables:
#     print(vegetable)

# from unittest import result


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(4, 3))