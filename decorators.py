def announce (f):
    def wrapper():
        print ("About to run a Functions...")
        
        f()

        print ("Done with the functions.")
        return wrapper

@announce
def hello ():
    print ("Hello, World!")
