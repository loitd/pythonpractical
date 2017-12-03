from types import *
def test(a=0):
	assert(a>=0), "a must greater than 0"
	assert(type(a) is IntType), "please put integer"
	return True

test(1)
# test(-1)
test("a")