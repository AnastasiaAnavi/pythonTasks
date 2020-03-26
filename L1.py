
#1. Задана вага в грамах. Визначити в тонах і кілограмах

#грами в тонни
print ('Enter value to covert it (grammes-tones)')
gramms_tones=input()
print (float(gramms_tones)/1000000)

#грами в кілограми
print ('Enter value to covert it (grammes-kilos)')
gramms_kilos=input()
print (float(gramms_kilos)/1000)

#2. Відомий обсяг інформації в байтах. Перевести в кілобайти, мегабайти

#байти в кілобайти
print ('Enter value to covert it (bytes-kilobytes)')
bytes_kilobytes=input()
print (float(bytes_kilobytes)/1024)

#байти в мегабайти
print ('Enter value to covert it (bytes-megabytes)')
bytes_megabytes=input()
print (float(bytes_megabytes)/1024/1024)

#3. Користувач вводить два числа. Одне присвоюється одній змінній,
#а друге - іншій. Необхідно поміняти значення змінних так, щоб значення першої
#виявилося в другій, а другої - у першій

print ('Enter first number')
a=input()
print ('Enter second number')
b=input()
a,b=b,a
print (a)
print (b)


#4. Обчислити площу і периметр прямокутника за заданими шириною і висотою

print ('Enter width of rectangle')
width=float(input())
print ('Enter altitude of rectangle')
altitude=float(input())
perimeter = (width+altitude)*2
area = (width*altitude)
print('The perimeter of rectangle is {} '.format(perimeter))
print('The area of rectangle is {} '.format(area))


#5. Обчислити площу і периметр кола по заданому радіусу

import math
print ('Enter radius of circle')
radius=float(input())
perimeter = math.pi * radius * 2
area = math.pi * radius * radius
print('The perimeter of circle is {} '.format(perimeter))
print('The area of circle is {} '.format(area))



#6.По двом введеним користувачем катетам прямокутного трикутника обчислити
#довжину гіпотенузи

import math
print ('Enter the length of first cathetus')
cathetus_1=float(input())
print ('Enter the length of second cathetus')
cathetus_2=float(input())
hypotenuse = math.sqrt(cathetus_1**2 + cathetus_2**2)
print('The length of hypotenuse is {} '.format(hypotenuse))

