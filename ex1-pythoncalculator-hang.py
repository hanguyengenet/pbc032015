#Python Calculator
print "Xin chao, day la chuong trinh Python Calculator"
print "1.Cong(+)"
print "2.Tru(-)"
print "3.Nhan(*)"
print "4.Chia(/)"
print "5.Fibonacci(f)"
print "6.Quit(q)"
answer = raw_input('Chon 1 trong cac phep tinh: ')
while answer not in ['1','2','3','4','5','6','Cong','Tru','Nhan','Chia','Fibonacci','Quit','+','-','*','/','f','q']:
    print "1.Cong(+)"
    print "2.Tru(-)"
    print "3.Nhan(*)"
    print "4.Chia(/)"
    print "5.Fibonacci(f)"
    print "6.Quit(q)"
    answer = raw_input('Chon 1 trong cac phep tinh: ')
else:
    if answer == "Cong" or answer == "+" or answer == "1":
	     a = float(raw_input('Nhap so thu 1: '))
	     b = float(raw_input('Nhap so thu 2: '))
	     print 'Ket qua: ', a+b
    elif answer == "Tru" or answer == "-" or answer == "2":
	     a = float(raw_input('Nhap so thu 1: '))
	     b = float(raw_input('Nhap so thu 2: '))
	     print 'Ket qua: ', a-b
    elif answer == "Nhan" or answer == "*" or answer == "3":
	     a = float(raw_input('Nhap so thu 1: '))
	     b = float(raw_input('Nhap so thu 2: '))
	     print 'Ket qua: ', a*b
    elif answer == "Chia" or answer == "/" or answer == "4":
	     a = float(raw_input('Nhap so thu 1: '))
	     b = float(raw_input('Nhap so thu 2: '))
	     print 'Ket qua: ', a/b
    elif answer == "Fibonacci" or answer == "f" or answer == "5":
	     n = int(raw_input('Tinh F(n), hay nhap n: '))
	     a=0
	     b=1
	     i=1
	     r=0
	     if n==2:
		     r=1
	     else:
	       while i<=n-2:
		       r=a+b
		       a=b
		       b=r
		       i=i+1
		       
       print 'F('+str(n)+')= ', r
    elif answer == "Quit" or answer == "q" or answer == "6":
       print 'Tam biet!'
	

