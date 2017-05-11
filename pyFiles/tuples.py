tuple = ('abc', 786, 2.23, "jonh", 70.2)
tiny_tuple = (123, 'jonh')


print "tuple: %s" % (tuple,)
print "tuple[0]: %s" % (tuple[0],)
print "tuple[1:3]: %s" % (tuple[1:3],)
print "tuple[2:]: %s" % (tuple[2:],)
print "tiny_tuple * 2: %s" % (tiny_tuple * 2,)
# final_tuple = tuple + tiny_tuple
print "tuple + tiny_tuple #1: %s" % ((tuple+tiny_tuple),)
print "tuple + tiny_tuple #2: %s" % (tuple+tiny_tuple,)
raw_input("Waiting for you :)")
