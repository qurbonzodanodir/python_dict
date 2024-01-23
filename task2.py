a = int(input())
cnt = 0 
i = 0
while a >= 1:
   cnt+= a%10 * pow(2,i)
   i += 1
   a //= 10
print (cnt)