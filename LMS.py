class Bookstore:

    def __init__(self,):
        self.count = 0
        self.stock = []

    def new_book(self):
        
        Book = input("Enter  book name : ")
        self.stock.append(Book)
        self.count += 1
    
    
    def display_stock(self):
        print(f"Total books are : {self.count}")
        print(f"Books available are : {self.stock}")

    def Rent_book(self):
        if self.count == 0:
            print("Sorry no books available")
        
        else: 
            booktorent = input("Enter the book name you want to purchase : ")
            if booktorent not in self.stock:
                print("Not Available")
            else:
                self.count -= 1
                self.stock.remove(booktorent)
                print(f"You have rented the book")
    
    def return_book(self):
        book_toreturn = input("Enter book name : ")
        self.stock.append(book_toreturn)
        self.count += 1
                
Store = Bookstore()


userinput = int(input("Hello welcome to Book store !\nWhat you would like to do :\n1.Rent\n2.Display Stock\n3.Donate or Give new book "))
if userinput not in range(0,5):
    print("Enter correct Function")

else:
    if userinput==1:
        Store.Rent_book()
    elif userinput==2:
        Store.display_stock()
    elif userinput == 3:
        Store.new_book()
    else:
        Store.return_book()