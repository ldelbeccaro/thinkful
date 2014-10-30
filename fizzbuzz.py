import sys

args = [sys.argv for sys.argv in sys.argv[1:]]
list = []

for sys.argv in args:
  try:
    num = int(sys.argv)
  except ValueError:
    continue
  else:
    list.append(num)
if len(list) > 0:
  n = list[0]
else:
  while True:
    try:
      n = raw_input('Please enter an interger: ')
      n = int(n)
      break
    except ValueError:
      print 'Not an integer! Please try again.'

print 'Fizz buzz counting up to', n
for i in range(1, n+1):
  if i % 15 == 0:
    print 'fizzbuzz'
  elif i % 3 == 0:
    print 'fizz'
  elif i % 5 == 0:
    print 'buzz'
  else:
    print i