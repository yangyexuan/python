def maxval(w,v,i,aw):
	global numcalls
	numcalls += 1

	if i == 0:
		if w[i] <= aw:
			return v[i]
		else:
			return 0

	without_i = maxval(w,v,i-1,aw)

	if w[i] > aw:
		return without_i
	else:
		with_i = v[i] + maxval(w,v,i-1,aw-w[i])
		return max(with_i,without_i)

weights = [1, 5, 3, 4,7,5,6,9,4,10,15,23,17,19,18,23,24,25,20,10,13]
vals = [15, 10, 9, 5,10,16,13,14,18,10,17,13,15,19,18,10,12,11,10,14,16]
numcalls = 0
res = maxval(weights, vals, len(vals)-1, 16)
print ('maxval = %s, numcalls = %s' %(res, numcalls))

def maxval(w,v,i,aw):
	m = {}
	return fastmaxval(w,v,i,aw,m)

def fastmaxval(w,v,i,aw,m):
	global numcalls
	numcalls += 1

	try:
		return m[(i,aw)]
	except KeyError:
		if i == 0:
			if w[i] <= aw:
				m[(i,aw)] = v[i]
				return v[i]
			else:
				m[(i,aw)] = 0
				return 0

		without_i = fastmaxval(w,v,i-1,aw,m)

		if w[i] > aw:
			m[(i,aw)] = without_i
			return without_i
		else:
			with_i = v[i] + fastmaxval(w,v,i-1,aw-w[i],m)
			res = max(with_i,without_i)
			m[(i,aw)] = res
			return res

weights = [1, 5, 3, 4,7,5,6,9,4,10,15,23,17,19,18,23,24,25,20,10,13]
vals = [15, 10, 9, 5,10,16,13,14,18,10,17,13,15,19,18,10,12,11,10,14,16]
numcalls = 0
res = maxval(weights, vals, len(vals)-1, 16)
print ('maxval = %s, numcalls = %s' %(res, numcalls))