import sys

alphas = 'abcdefghijklmnopqrstuvwxyz'

keys = input('Enter the keyword: ')
keys = keys.lower()
keys = ''.join(sorted(set(keys),key = keys.index))
subst = alphas

for char in keys:
   subst = subst.replace(char,'')

mixed = keys+subst
print('Plaintext :'+alphas)
print('Ciphertext :'+mixed)
infil = open(sys.argv[1])
plain = infil.read()
text = ''

for char in plain:
   position = alphas.find(char)
   if(position==-1):
       text = text+char
   else:
       text = text+mixed[position]

print(text)