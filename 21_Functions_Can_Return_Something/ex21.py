def add(a, b):
    print "Adding: %d + %d" % (a, b)
    return a + b

def substract(a, b):
    print "Substracting: %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiplying: %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing: %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(14, 4)
height = substract(220, 40)
weight = multiply(30, 2)
iq = divide(1000, 8)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


#A puzlle for the extra credit, type it anyway.
print "Here is a puzzle."

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
