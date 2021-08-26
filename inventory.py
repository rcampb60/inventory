'''
a script to keep track of inventory
'''

class product:

    def __init__(self, name, price, id, quantity):
        self.name = name # name to refer to the product
        self.price = price # price of the product
        self.id = id # id of the product
        self.quantity = quantity # quantity in stock
        

    def info(self):
        print(f"{self.name}:\nprice: £{self.price} id: {self.id} in stock: {self.quantity}") # prints out the relevant info
        

mouse = product('mouse',20,1,48) # instantiate the various product objects
keyboard = product('keyboard',60,2,109)
mat = product('mat',5,3,16)
monitor = product('monitor',150,4,37)
computer = product('computer',500,5,23)

class inventory(product): # inventory class is passed the product class as objects already instantiated 

    def sum_value(self):
        mouse_subtotal = mouse.price * mouse.quantity # sum up all subtotals
        keyboard_subtotal = keyboard.price * keyboard.quantity
        mat_subtotal = mat.price * mat.quantity
        monitor_subtotal = monitor.price * monitor.quantity
        computer_subtotal = computer.price * computer.quantity
        grand_total = mouse_subtotal + keyboard_subtotal + mat_subtotal + monitor_subtotal + computer_subtotal # sum up grand total

        __str__(f"""
Mice value: £{mouse_subtotal}
Keyboard value: £{keyboard_subtotal}
Mouse Mat value: £{mat_subtotal}
Monitor value: £{monitor_subtotal}
Computer value: £{computer_subtotal}
Grand total: £{grand_total}
        """)

    

inventory.sum_value(product) # call the sum_value function insie the inventory class whilst passing product class
