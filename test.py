n = "KALLEe"

n = n.lower()
print(n)

def check(answer, wanted):
    "Checks if the desired string is in the answer follor answer , wanted"
    answer = answer.lower()
    for word in wanted:
        if answer is not None and word in answer:
            return True
    
        else:
            return False

if check("Bob",["bob"]):
    print("bob")