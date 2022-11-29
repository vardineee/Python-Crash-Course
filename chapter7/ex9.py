sandwich_orders = ['pastrami','chicken', 'pastrami', 'nutella', 'grilled cheese', 'beef', 'pastrami']
finished_sandwiches = []
print("Sorry, the deli has run out of pastrami! \n")
while 'pastrami' in sandwich_orders:
    sandwich_orders .remove('pastrami')
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I am working on {current_order}")
    finished_sandwiches.append(current_order)

print("\n")
for order in finished_sandwiches:
    print(f"Your {order} sandwich is ready!")
    