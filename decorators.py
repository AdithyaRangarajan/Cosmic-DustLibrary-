def announce(f):
    def wrapper ():
        print("Abount to run a function...")
        f()
        print("Done with the functions.")
        
    return wrapper
@announce
def hello():
    print("Hello my world..!!!!!")

hello()
