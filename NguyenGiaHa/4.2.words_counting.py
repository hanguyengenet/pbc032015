#python
#Words, char counting program
running=True
while running:
	print "----------------"
	print "1.Words counting"
	print "2.Char counting"
	print "3.Quit"
	answer=raw_input('Hay chon (1-3): ')

	if answer=='1':
		#words counting
		s = raw_input('Hay nhap 1 doan van ban: ')
		l=s.split()
		d={}
		for i in range(len(l)):
			if l[i] in d:
				d[l[i]]=d[l[i]]+1
			else:
				d[l[i]]=1
		print d
		for k in d:
			print "Tu '"+str(k)+"' xuat hien "+str(d[k])+ ' lan.'
	elif answer=='2':
		#char counting
		s = raw_input('Hay nhap 1 doan van ban: ')
		j=0
		d={}
		for i in range(len(s)):
			if s[i]!=' ':
				if s[i] in d:
					d[s[i]]=d[s[i]]+1
				else:
					d[s[i]]=1
				j=j+1 #dem tong so ki tu
		print 'Doan van ban vua nhap co '+str(j)+' ki tu.'
		print d
		for c in d:
			print 'Ki tu '+str(c)+' da xuat hien '+str(d[c]) +' lan.'
	elif answer=='3':
		running=False
		print 'Quit!'
