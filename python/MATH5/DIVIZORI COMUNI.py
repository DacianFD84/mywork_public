num1 = int(input("INTRODUCEȚI PRIMUL NUMĂR : "))
num2 = int(input("INTRODUCEȚI AL DOILEA NUMĂR : "))
divisor = 0
print("DIVIZORII COMUNI ALE NUMERELOR ",num1," SI ",num2," SUNT -")
for i in range(1,min(num1,num2)+1):
  if num1%i == num2%i == 0:
    divisor = i
    print(divisor)
