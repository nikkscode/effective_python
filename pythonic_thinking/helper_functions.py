from urllib.parse import parse_qs

# query-string
my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)

# printing representation of qs
print(repr(my_values))

# Listing of pairs with different types of value-representations
print('Red:     ', my_values.get('red'))
print('Green:   ', my_values.get('green'))
print('Opacity: ', my_values.get('opacity'))

print('\n')

# Listing of pairs with same types of value-representations but visual noise
red = int(my_values.get('red', [''])[0] or 0)
green = int(my_values.get('green', [''])[0] or 0)
opacity = int(my_values.get('opacity', [''])[0] or 0)
print('Red:     %r' % red)
print('Green:   %r' % green)
print('Opacity: %r' % opacity)

print('\n')

#helper-function to provide better readability:
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

print('Red:    ',get_first_int(my_values, 'red'))   
print('Green:  ',get_first_int(my_values, 'green')) 
print('Opacity:',get_first_int(my_values, 'opacity'))   

# Things to remember:
# - Python syntax makes it very easy to write single-line expressions that tend to create visual noise
# - Complex expressions should be refactored into helper Functions