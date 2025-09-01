def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Leo", age=30)


def get_details(**kwargs):
    print(kwargs)

get_details(name = "Joy" ,age = 36, city="Mombasa")