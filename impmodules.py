# import glob
# myfiles = glob.glob("*.txt")
# for filepath in myfiles:
#     with open(filepath,'r') as file:
#         print(file.read().upper())

# import csv
# with open("wth.csv",'r') as file:
#     data = list(csv.reader(file))
#
# city = input("Enter the city")
# for row in data:
#     if row[0] == city:
#         print(row[1])
#
# import shutil
# # shutil means shell utility files used for making files archive,zip
# shutil.make_archive("output","zip","files")

import webbrowser
user_term = input("enter a search item: ")
webbrowser.open("https://www.google.com/search?q="+user_term)
