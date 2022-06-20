class Library:
    def __init__(self,list_of_books):
        self.list_of_books = list_of_books
        
    def display_books(self):
        print(self.list_of_books)
        
    def lend_book(self):
        l_book = input("Which book u want  ").strip()
        if l_book in list_of_books:
          print("Yes! You can take the book ")
          list_of_books.remove(l_book)
        else:
          print("Sorry we don't have that book with us ")
          
        
    def add_book(self):
        print("Your are doing a good job! ")
        a_book = input("Plz! Enter the name of the book ").strip()
        list_of_books.append(a_book)
        print("Thank you!")
        
    def return_book(self):
        r_book = input("Plz enter the book name: ").strip()
        list_of_books.append(r_book)
        
        
        
    
        
                
                
        
        
        
        
list_of_books = ["bcnb","hdhfsdhg","hjghd"]
Tarun = Library(list_of_books)
#choice = input("Enter ur choice:  ")
#if (choice == "1"):
#    Arun.display_books()
#else:
#    print("Not Found ")

#Arun.lend_book()
#print(list_of_books)
while True:
    print("Welcome to Tarun's Library ")
    choice  =int(input("Enter 1 to avilable books \nEnter 2 to lend books \nEnter 3 to add book \nEnter 4 to return the book\n"))
    if(choice == 1):
        Tarun.display_books()
    elif(choice == 2):
        Tarun.lend_book()
        list_of_books.sort()
        print(list_of_books)
    elif(choice == 3):
        Tarun.add_book()
        list_of_books.sort()
        print(list_of_books)
    elif(choice == 4):
        Tarun.return_book()
        list_of_books.sort()
        print(list_of_books)    
    else:
        exit()
        

list_of_books.sort()
print(list_of_books)
    

    
    