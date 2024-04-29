from functools import reduce

CheckEven=lambda No : No%2==0
Increase=lambda No : No+1
Add=lambda A,B : A+B

def filterX(Task,Elements):
    Result=[]

    for no in Elements:
        if(Task(no)==True):
            Result.append(no)
    return Result

def mapX(Task,Elements):
    Result=[]

    for no in Elements:
        Ret=Task(no)
        Result.append(Ret)
    return Result
    
def main():
    Data=[11,14,20,23,18,16,15,20]
    print("Data from input list: ",Data)

    FData=list(filterX(CheckEven,Data))           # should always have boolean value
    print("Data after filter activity: ",FData)

    MData=list(mapX(Increase,FData))              # one input and one output
    print("Data after map activity: ",MData)

    RData=reduce(Add,MData)                       # .
    print("Data after reduce activity: ",RData)

if __name__ == "__main__":
    main()