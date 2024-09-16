import time

# def whileloop():
#     i =0
#     while i<500:
      
#         i=i+1
#         print(i)
        
        
# def forloop():
#     for i in range(500):
#         print(i)
        
        
# init = time.time()
# whileloop()
# t1= time.time()
# init = time.time()
# forloop()    
# print(t1)
# print(time.time())
import time

# Get the current local time
t = time.localtime()
print(t)

# Correctly format the time string
frmtdtime = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(frmtdtime)
