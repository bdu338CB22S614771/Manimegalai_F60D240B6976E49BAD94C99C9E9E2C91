def fact_rect(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rect(n-1)
    number=4
    res=fact_rect(number)
    print("The factorial of{}is{}". formal(number, res))