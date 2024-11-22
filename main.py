class Book:
    def __init__(self, title:str, author:str, price:float, quantity:int):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def apply_discount(self, discount_percentage:float):
        self.price *= 1 - discount_percentage
    
    def sell(self, amount:int):
        if amount <= self.quantity:
            self.quantity -= amount
        else:
            print(f"Not enough quantity is {self.quantity}")
        
    def __str__(self):
        return f"Назва: {self.title}, Автор: {self.author}, Ціна: ${self.price}, Кількість: {self.quantity}"
    
class BookStore:
    def __init__(self, books):
        self.books = books
    
    def add_book(self, book:Book):
        self.books.append(book)

    def search(self, query:str):
        answer = []
        for i in self.books:
            if i.title == query:
                if i not in answer:
                    answer.append(i)
            if i.author == query:
                if i not in answer:
                    answer.append(i)
        return answer
    
    def calculate_total_value(self):
        answer = 0
        for i in self.books:
            answer += i.price
        return answer
    

test_1 = Book("prog", "Popa", 10.2, 30)
test_2 = Book("dock", "Popa", 5.9, 3)

test_3 = BookStore([test_1])


print(test_3.books[0])
test_3.books[0].sell(10)
test_3.books[0].apply_discount(0.5)
print(test_3.books[0])

test_3.add_book(test_2)
ans = test_3.search("Popa")
print(*ans)
ans = test_3.calculate_total_value()
print("total value: ",ans)

