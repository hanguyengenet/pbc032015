#python
#Chuong trinh quan ly hoc sinh
running = True
l=[]
i=0
#Functions
def Add():
    '''Ham them hoc sinh moi'''
    d={}
    d['id'] = len(l)
    d['hoten'] = raw_input('Ho ten hoc sinh: ')
    d['bod'] = raw_input('Ngay sinh (dd/mm/yyyy): ')
    d['lop'] = raw_input ('Lop: ')
    d['qq'] = raw_input('Que quan: ')
    try:
        l.append(d)
        return True
    except:
        return False
    finally:
        d={}
def Search():
    '''Ham tim kiem hoc sinh'''
    s = raw_input('Ho ten hoc sinh can tim: ')
    c=0
    for i in range(len(l)):
        if l[i]['hoten']==s:
            print str(l[i]['id'])+' '+l[i]['hoten']+' '+l[i]['bod']+' '+l[i]['qq']
            c=c+1
    if c==0:
        print 'Khong tim thay, hay thu lai.' 
def Modify():
    '''Ham chinh sua thong tin hoc sinh'''
    s = input('Nhap id hoc sinh can sua: ')
    c=0
    for i in range(len(l)):
        if l[i]['id']==s:
            d['id'] = s
            d['hoten'] = raw_input('Ho ten hoc sinh: ')
            d['bod'] = raw_input('Ngay sinh (dd/mm/yyyy): ')
            d['lop'] = raw_input ('Lop: ')
            d['qq'] = raw_input('Que quan: ')
            l.remove(l[i])
            l.insert(i,d)
            c=c+1
                
    if c==0:
        print 'Khong tim thay, hay thu lai.'

def Del():
    '''Ham xoa thong tin hoc sinh'''
    s = input('Nhap id hoc sinh can xoa: ')
    c=0
    for i in range(len(l)):
        if l[i]['id']==s:
            l.remove(l[i])
            c=c+1
    if c==0:
        print 'Khong tim thay, hay thu lai.' 
def Print():
    print ''
    print 'ID|Ho ten|Ngay sinh|Que quan'
    print '----------------------------'
    for i in range(len(l)):
        print str(l[i]['id'])+' '+l[i]['hoten']+' '+l[i]['bod']+' '+l[i]['qq']
#Main            

try:
    while running:
        print '-----------------'
        print '1. Them hoc sinh'
        print '2. Tim kiem'
        print '3. Sua'
        print '4. Xoa'
        print '5. In'
        print '6. Thoat'
        
        answer = raw_input('Hay chon (1-5): ')
        if answer =='1':
            #Add
            if Add()==True:
                print 'Da them thanh cong!'
            else:
                print 'False'
            
        elif answer == '2':
            #Search
            Search()
                
        elif answer == '3':
            #Modify
            Modify()
        elif answer == '4':
            #Del
            Del()
        elif answer == '5':
            #Print
            Print()
        elif answer == '6':
            a=raw_input('Ban muon thoat(y/n): ')
            if a=='y':
                running = False
            else:
                running = True
        
except:
        print 'Error occurred!'
finally:
        print 'Done!'
