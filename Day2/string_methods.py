name = ' Praveen The Founder '
name_=['Praveen','The','Founder']
name__='praveen the founder'
print('upper :' + name.upper())
print('lower :' + name.lower())
print('Replace : ' + name.replace('T','t'))
print('Strip : ' + name.strip())
print('Split : ' + f'{name.split()}')
print('Join :' + ' '.join(name_))
print('Startswith : ' + f'{name.startswith('praveen')}')
print('Startswith : ' + f'{name.endswith('founder')}')
print('find : ' + f'{name.find('The')}')
print('capitalize : ' + name__.capitalize())
print('title : ' + name__.title())