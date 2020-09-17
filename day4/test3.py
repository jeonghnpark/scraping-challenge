s = "not convertible"
try:
    i = int(s)
except ValueError as verr:
    print("value error !", verr)
except Exception as ex:
    print("exception error ", ex)

# print(i)
