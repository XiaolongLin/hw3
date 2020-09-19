def digit_sum(n):
  sum = 0
  n = int(n)
  while n>0:
   sum += n % 10
   n //= 10
  return sum
   
def run():
  num = int(input("Enter an int: "))
  print(f"sum of digits of {num} is {digit_sum(num)}.")

if __name__ == "__main__":
  run() 
      
  

