#Study drill
#Task one: remove my_
name = 'Artur Nowak'
age = 23 
height = 175.0 #cm
weight = 60.0 #kg 
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

#Task two: make conversion from cm to inches and from kg to lbs
print "Lets talk about %s." % name
print "He's %d cm tall which is %r inches." % (height, height * 0.394)
print "He's %d kg heavy which is %f pounds." % (weight, weight * 2.2)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s beacuse he drinks tea." % teeth

#Task three: use %r
print "If I add %r, %r, and %r I get %r" % (age, height, weight, age + height + weight)
