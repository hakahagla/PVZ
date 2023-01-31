peashootervalue = 0
peashootervalue2 = 0
def peashooter(obj):
    global peashootervalue
    if peashootervalue >= len(obj):
        peashootervalue = 0
    peashooter = obj[peashootervalue]
    peashootervalue += 1
    return peashooter

def peashooter2(obj):
    global peashootervalue2
    if peashootervalue2 >= len(obj):
        peashootervalue2 = 0
    peashooter = obj[peashootervalue2]
    peashootervalue2 += 1
    return peashooter


    
    
    
    
