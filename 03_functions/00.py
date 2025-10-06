def greet(user_id = 147, name="Guest"):

    print(f" {user_id} Hello, {name}!")
    

greet()
greet(123)
greet("Member 1")
greet(name = "Member 2")
greet(987654, "Member 3")
greet(name = "Member 3", user_id = 987654)
    
    
    
    
    