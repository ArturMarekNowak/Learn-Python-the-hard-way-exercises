#Study Drill
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslach_cat = "I'm \\ a \\ cat."

#Task two: use ''' instead of """
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslach_cat
print fat_cat

print 10 * "--"

kg_of_cat_food = 1410.150716101518

print "\'%r\'" % kg_of_cat_food
print "\"%r\"" % kg_of_cat_food
print "\'%s\'" % kg_of_cat_food
print "\"%s\'" % kg_of_cat_food



#Just for fun
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
