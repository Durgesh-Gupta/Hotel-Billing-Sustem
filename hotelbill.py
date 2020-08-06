class hotel:
    def __init__(self):
        self.price={
            1:300,
            2:150,
            3:30,
            4:150,
            # Nonveh
            5:250,
            6:280,
            7:300
        }
        self.lst=[]
        self.total=0

    def menu(self):
        self.c=1
        while(self.c==1):
            choice=int(input("\nEnter 1.Veg   2.Nonveg    3.Bill\n"))
            
            if choice==1:
                self.veg()
            elif choice==2:
                self.nonveg()
            elif choice==3:
                self.c=0
                self.bill()
                # print(self.c)
            else:
                print("Choose Valid Option\n")
            

        

    def veg(self):
        print("\nVeg Menu:\n1.Shahi Paneer\n2.Dal\n3.Butter Roti\n4.Jeera Pulao")
        self.veg1=int(input("\nEnter :"))
        self.qty=int(input("Enter Qtys:"))
        self.total+=self.price[self.veg1]*self.qty
        

    def nonveg(self):
        print("\nNonveg Menu:\n1.Biryani\n2.Chicken Masala\n3.Butter Chicken")
        self.nveg1=int(input("\nEnter :"))
        self.qty=int(input("Enter Qtys:"))
        self.total+=self.price[self.nveg1+4]*self.qty
        

    def bill(self):
        print("****************************")
        print("Total Bill is..",self.total)

a=hotel()
a.menu()
