"""Learn Python The Hard Way - Exercise 5"""

MY_NAME = 'Nicholas D. Land'
MY_AGE = 28 # not a lie
MY_HEIGHT = 71 # inches
MY_WEIGHT = 205 # lbs
MY_EYES = 'Blue'
MY_TEETH = 'White'
MY_HAIR = 'Brown'

print "Lets talk about %s." % MY_NAME
print "He's %d inches tall." % MY_HEIGHT
print "He's %d pounds heavy." % MY_WEIGHT
print "Actually thats not too heavy."
print "He's got %s hair." % MY_HAIR
print "His teeth are usually %s depending on the coffee." % MY_TEETH

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(
		MY_AGE, MY_HEIGHT, MY_WEIGHT, MY_AGE + MY_HEIGHT + MY_WEIGHT)
