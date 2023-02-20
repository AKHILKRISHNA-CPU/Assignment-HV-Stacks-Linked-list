class Node:
    def __init__(self, customer_id, customer_name, purchase_date, bill_amount):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.purchase_date = purchase_date
        self.bill_amount = bill_amount
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_customer(self, customer_id, customer_name, purchase_date, bill_amount):
        new_node = Node(customer_id, customer_name, purchase_date, bill_amount)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            previous_node = None
            while current_node and current_node.bill_amount < bill_amount:
                previous_node = current_node
                current_node = current_node.next
            if previous_node:
                previous_node.next = new_node
                new_node.next = current_node
            else:
                new_node.next = self.head
                self.head = new_node

    def view_all_customers(self):
        current_node = self.head
        while current_node:
            print(f"Customer ID: {current_node.customer_id}, Name: {current_node.customer_name}, Purchase Date: {current_node.purchase_date}, Bill Amount: {current_node.bill_amount}")
            current_node = current_node.next
    
    def view_total_purchase_amount(self, year):
        amount = 0
        current_node = self.head
        while current_node:
            if current_node.purchase_date.split("/")[-1] == year:
                amount += current_node.bill_amount
            current_node = current_node.next
        print(f"The total amount of specific year {year} and it's total amount {amount}")
    
    def view_customer_details(self, name):
        current_node = self.head
        while current_node:
            if current_node.customer_name == name:
                print(f"Customer ID: {current_node.customer_id}, Name: {current_node.customer_name}, Purchase Date: {current_node.purchase_date}, Bill Amount: {current_node.bill_amount}")
                return
            current_node = current_node.next
        print(f"No customer the name  {name} found")

list_data = LinkedList()
list_data.add_customer(1, "Akhil", "20/05/2023", 50)
list_data.add_customer(2, "Krishna", "21/02/2024", 10)
list_data.add_customer(3, "Madicherla", "1/12/2025", 100)
list_data.view_all_customers()
list_data.view_total_purchase_amount("2023")
list_data.view_customer_details("Akhil")
