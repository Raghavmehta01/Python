f = open('/Users/raghavmehta/Desktop/Coding/python/new/myfile.txt', 'a')

f.write("hello again")



with open('/Users/raghavmehta/Desktop/Coding/python/new/myfile.txt', 'r'):
   text= f.read()
   print(text)