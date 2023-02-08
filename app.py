
def decorator(function_name):
    def wrapper(*args):
        print('Good morning ')
        function_name(*args)
    return wrapper

@decorator
def person_info(name,age):
    print("dear " + name + " you are " + age + " years old.")


person_info('satinder','27')