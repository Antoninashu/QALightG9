spisok1 = [1,2,3]

print(spisok1)
print (sum (spisok1))

spisok2 = [1,2,3,1,2,4,1,2,5,2,3,6,3,4,7]

print(spisok2)
print(set(spisok2))

tz = {'name' : 'Tonia',
      'age' : 23,
      'selary' : 3000}
print(tz)
tz['salary'] = 3045
print(tz)


isHappy = int(input('Enter num: '))

if isHappy > 5:
    print('Yes yahoo')
elif isHappy == 9:
    print("njnj")
else:
    print('hohoho')