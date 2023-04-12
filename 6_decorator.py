def summ_invoice():
    return 10000

def decorator_login(func):
    def wrapper_decorator(*args, **kwargs):
        if login != "admin":
            result=None
            print("Access is denied")
            return result
        
        result = func(*args, **kwargs)
        print("Invoice amount: ", result)
        return result
    return wrapper_decorator

login= input("Input login: ")
summ_admin = decorator_login(summ_invoice)
print(summ_admin())
