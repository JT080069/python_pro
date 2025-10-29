print('------------------')
s_m2 = r'hello \t\tworld \nit\'s Wednesday \n29th \t\tOctober'
s_m2 = 'hello \t\tworld \nit\'s Wednesday \\\n29th \October'
print(s_m2)

ll_i = s_m2.find('lll')
#ll_i = s_m2.index('lll')
print(f'll_i={ll_i}')
lines = s_m2.split('\n')
print(f'lines={lines}')