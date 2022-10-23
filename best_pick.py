import constants as c

#use an int input to modify a string of functional programming code within Google Sheets
def best_pick(i):
    m = str(i + 2) # shift 2 as Python is 0 indexed, and first entry is on row 2
    code = c.p[0]
    #print(code)
    for x in range(len(c.p)-1):
        cells = "K" + m +":M" + m + ")," + c.col[x] + m
        code = code + cells + c.p[x+1]
        #6print(code)
    return code


# debugging purposes
#r = best_pick(22)
#print(type(r))
#if type(r) == str:
#    print("true")