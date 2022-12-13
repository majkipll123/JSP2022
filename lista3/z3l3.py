a=int(input())
b=int(input())
c=int(input())
if a==0 :
    print("podane rownanie nie jest kwadratowe")
elif ((b**2)-2*a*c)< 0:
    print("Delta jest ujemna, brak rozwiazan rzeczhywistych")
elif ((b**2)-2*a*c)==0:
    print("Delta jest rowna zero, rownanie posiada jeden  podwojny pierwiastek rzeczywisty")
elif ((b**2)-2*a*c)> 0:
    print("Delta jest wieksza od zera, rownanie posiada dwa pierwiastki rzeczywiste")