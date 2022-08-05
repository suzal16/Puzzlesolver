for i in range(2,70):
    a,b = i**(0.5),i**(1/3)
    ra,rb = round(a),round(b)
    if abs(ra-a)<=10**-3 and abs(rb-b)<=10**-3 :
        print(i)
