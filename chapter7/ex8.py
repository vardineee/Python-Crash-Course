sandwich_orders = ['chicken', 'nutella', 'grilled cheese', 'beef']
finished_sandwiches = []
while sandwich_orders:
        current_order = sandwich_orders.pop()
        print(f"I am working on your {current_order}")
        finished_sandwiches.append(current_order)

print("\nFinished orders are: ")
for finished_sabdwich in finished_sandwiches:
    print(f"\t-{finished_sabdwich}")
    
