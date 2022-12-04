def permutacje(string,start,end):
    current =0;
    if (start==end-1):
        print(string);
    else:
        for current in range (start,end):
            x=list(string);
            temp=x[start];
            x[start]=x[current];
            x[current]=temp;
            permutacje("".join(x),start+1,end);
            temp=x[start];
            x[start]=x[current];
            x[current]=temp;            
str=input('podaj ciag znakow a ja wypisze wszystkie jego permutacje: ')
n=len(str);
print("Wszystkie permutacje twojego napisu")
permutacje(str,0,n)