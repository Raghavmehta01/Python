def greet(fn):
    def mfx():
        print("Hello")
        fn()
        print("Thanks")
        
    return mfx


@greet 
def hello():
    print("World")
    def bye():
        print("bye bye")
    bye()
    
    


hello()
