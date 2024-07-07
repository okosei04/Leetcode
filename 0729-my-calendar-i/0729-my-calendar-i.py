class MyCalendar:

    def __init__(self):
        self.bookings = []

        

    def book(self, start: int, end: int) -> bool:
        for book_start, book_end in self.bookings:
            if start < book_end and end > book_start:
                return False
        self.bookings.append((start,end)) 
        
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)