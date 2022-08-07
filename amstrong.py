n=153
l=len(str(n))
s=0
temp=n
while temp>0:
    d=temp%10
    s += d**l
    temp//=10

if s==n:
    print('its amstrong')
else:
    print('its not')
