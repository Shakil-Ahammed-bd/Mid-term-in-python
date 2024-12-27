class Start_cinema:
    def __init__(self):
        self.hall_list = []
    
    def entry_hall(self,hall):
        self.hall_list.append(hall)
        # print(f"\n\tHall '{hall.hall_no}' has been added to Star Cinema.")
        
class Hall(Start_cinema):
    def __init__(self,rows,cols,hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no 

    def entry_show(self,id,movie_name,time):
        show = (id, movie_name,time)
        self.show_list.append(show)

        arr =  [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.seats[id] = arr
        print(f"\t\n Show Id '{id}, Shows '{movie_name}, at Time '{time}")

    
    def view_available_seats(self, id):
        if id not in self.__seats:
            print(f"Error: Show with ID '{id}' not found.")
            return
        print(f"Available seats for show id :{id}")
        matrix = self.__seats[id]
        for row in matrix:
            print(' '.join(row)) 

    
    def view_show_list(self):
        print("List of Shows : ")
        for show in self.show_list:
            id, movie_name,time = show
            print(f" Show id :{id}, Movie : {movie_name}, Time :{time}")

    

pl = Hall(1, 1, 3) 
pl.entry_show(101, "tufan", "10:00 AM")
pl.entry_show(102, "kajol rekha", "02:00 PM")

run = True

while run:
    print("\n\n\tOptions: \n")
    print("\t1 : VIEW ALL SHOW TODAY")
    print("\t2 : VIEW AVAILABLE SEATS")
    print("\t3 : BOOK TICKET")
    print("\t4 : Exit")
            

    ch =int(input("\n\tEnter Option : "))

    if ch == 1:
        pl.view_show_list()

    elif ch == 2:
        id = (input("\tShow id: "))
        pl.view_available_seats()

    elif ch == 3:
        id = (input("\tShow id: "))
        seats_to_book = int(input("\tNumber of Ticket? : "))
        rows = input("\tEnter Seat Row: ")
        clow = input("\tEnter Seat Cols: ")

    elif ch == 4:
        print("\tPrograme is exit: ----")
        exit()




