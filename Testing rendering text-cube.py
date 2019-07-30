a = [0,0,0,0]
b = [0,0,0,0]
c = [0,0,0,0]
d = [0,0,0,0]
e = [0,0,0,0]
f = [0,0,0,0]
g = [0,0,0,0]
h = [0,0,0,0]
i = [0,0,0,0]
j = [0,0,0,0]
k = [0,0,0,0]
l = [0,0,0,0]


def call(pos1, i, pos2, j, pos3, k):
	a[pos1-1] = i
	b[pos2-1] = j
	c[pos3-1] = k

def render():
	print(a,b,c)
	print(d,e,f)
	print(g,h,i)
	print(j,k,l)



render()