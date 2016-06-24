class queue(object):
	
	def __init__(self, lst = []):
		self._lst = lst
	def push(self,element):
		self._lst.append(element)
	def pop(self):
		outelement = self._lst[0]
		self._lst = self._lst[1:]
		return outelement
	def view(self):
		return self._lst

if __name__ == '__main__':
	q =queue()
	q.push(1)
	q.push('a')
	q.push('25')
	print (q.pop())
	q.push(2)
	print (q.view())		