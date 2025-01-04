#programme to show linaer time coMplexity (o(n)) by entrin any n
def lintime(n):
    iteration=0
    for i in range (1,n+1):
        iteration+=1
    print("for number",n,'iterations are',iteration)
lintime(98)
lintime(799)