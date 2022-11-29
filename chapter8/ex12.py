def sandwhich_maker(*items):
    print("Making sandwich with the following")
    for item in items:
        
       print(f"\t-{item}")
    
sandwhich_maker('tomato')
sandwhich_maker('cucumber', 'mashroom')
    