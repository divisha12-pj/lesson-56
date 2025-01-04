#programme to show time complexty(o(n^2)) ny entering any n
def timecoon(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print("#",end="")
            iteration+=1
        print("")
    print("when n is",n,"iteration is",iteration)
timecoon(7)
timecoon(12)