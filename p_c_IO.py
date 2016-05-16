def consumer():
	r = 'hello'
	print (r)
	while True:
		n = yield r
		if not n:
			return 
		print ('[CONSUMER] Consuming %s...' %n)
		r = '200 ok'

def produce(c):
	c.send(None)
	n = 0
	while n<5:
		n = n +1
		print ('[PRODUCE] Produce %s...' %n)
		r = c.send(n)
		print ('[PRODUCE] Consumer return :%s' %r)
	c.close()

c = consumer()
produce(c)