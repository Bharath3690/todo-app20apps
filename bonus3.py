# meals = ['pasta', 'pizza', 'parota']
# for meal in meals:
#     print(meal.capitalize())
# print("Bye")

# for item in ["hello", "hi"]:
#     print(item.upper())

# filenames = ["1.Raw data.txt", "2.reports.txt", "3.presentataion.txt"]
# for filename in filenames:
#     filename_new = filename.replace('.', '-', 1)
#     print(filename_new)

# waiting_list = ["sen", "john", "ben"]
# waiting_list = waiting_list.sort()
# # sort() used to sort the items in ascending order sort method doesnt return anything so we have to assing to a variable
#
# for index, item in enumerate(waiting_list):
#     row = f"{index+1}.{item.capitalize()}"
#     print(row)

# mylist = ["a", "d", "c"]
# # mylist.sort() for ascending order
# # mylist.sort(reverse=True) for descending oder
# print(mylist)

# for i, j in enumerate("abcd"):
#     print(i+1)

# for i, j in enumerate("abcd"):
#     phrase = f"Printing {i * 5}"
#     print(phrase)

# for i, j in enumerate("abcd"):
#     print(f"Printing {j * 5}")

filenames = ['document', 'report', 'presentation']
for index, filenames in enumerate(filenames):
    print(f"{index}-{filenames.capitalize()}.txt")