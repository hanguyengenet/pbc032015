#python
#vd class ball
class ball:
	sobong = 0
	def __init__(self,x=0,y=0,z=0):
		#ball.sobong= + 1
		ball.sobong= ball.sobong+ 1
		self.x=x
		self.y=y
		self.z=z
		print 'So bong hien co: ', ball.sobong
	def bay(self):
		if self.x!=0:
			print 'True!'
		else:
			print 'False!'
	def lan(self):
		if self.z!=0:
			print 'Bong dang lan!'
		else:
			print 'Bong dang dung yen!'
	def dembong(self):
		print 'So bong hien co: ', ball.sobong
class Nikeball(ball):
        thuonghieu = 'Nike'
        xoay = 10
        super(Nikeball,self).__init__()
