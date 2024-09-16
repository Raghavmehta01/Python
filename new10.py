book = []
for i in range(2):
    book_name = input("enter name of book :")
    author_name = input("enter name of author :")
    book_price = int(input("enter price :"))
    book.append(

    {'Booktitle':book_name,'Authorname':author_name,'Price':book_price}

    )
    # print(i['book_name','author_name','book_price'])
    


#     print(data[f"Booktitle:{data['Booktitle']},Authorname:[data{'Authorname'}],Price:[data{'Price'}]]"])
header = f"{'Booktitle':<15} {'Authorname':<15} {'Price':<15}"
print(header)
for data in book:
    

    row = f"{data['Booktitle']:<15},{data['Authorname']:<15},{data['Price']:<15}"
    for i in range(book[book_price]):
        sum =0
        sum = sum +i

    print(f"{row},total sum : {i}")
    
    
    
# book = []
# for i in range(2):
#     book_name = input("enter name of book :")
#     author_name = input("enter name of author :")
#     book_price = int(input("enter price"))
#     book.append(

#     {'Booktitle':book_name,'Authorname':author_name,'Price':book_price}

#     )
#     # print(i['book_name','author_name','book_price'])
    

# for data in book:
#     print(data['Booktitle':{data['Booktitle']},'Authorname':[data{'Authorname'}],'Price':[data{'Price'}]])