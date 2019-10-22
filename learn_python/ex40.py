cities={'CA':'San Francisco', 'MI':'Detroit', 'FL':'Jacksolnville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return 'Not found.'

#ok pay attention!
cities['_find'] = find_city

for city in cities.keys():
    print '%s => %s\n' % (city, cities[city])
print('**************************\n')
for (k,v) in cities.items():
    print '%s => %s\n' % (k, v)

while True:
    print 'State?(ENTER to quit)',
    state = raw_input('> ')

    if not state: break

    #this line is the most important ever! study!

    city_found = cities['_find'](cities, state)

    print city_found
