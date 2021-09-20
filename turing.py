def add(c, k):
    c.test += 1
    k += 1
    
    
class Plus :
    def __init__(self):
        self.test = 0
    
    
def main():
    P = Plus()
    index = 0
    for i in range(0, 25):
        add(P, index)
    print("P.test=", P.test)
    print("index=", index)
    
    
main()
