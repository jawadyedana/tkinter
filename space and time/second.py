# constant time complexity
def printnumber(n):
    literation = 0 
    print("the ttal number entered by user is:",n)
    literation += 1
    print("total literation done by computer is",literation,"/n")

    printnumber(10)
    printnumber(2000)

    # linear time complexity
    def onTime(n):
        iteration=0
        for i in range(1,n+1):
            iteration+=1
        print("when n is ",n,"iterations = ",iteration)

onTime(10)
onTime(20)
onTime(42)