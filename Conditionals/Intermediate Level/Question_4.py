'''
    Take income and calculate tax:
    - < 2.5L → No tax
    - 2.5L–5L → 5%
    - 5L–10L → 10%
    - 10L → 20%
'''
income=int(input("Enter Income(L):"))
if income<=2.5:
    print("Income:",income,"L")
    tax=income*0
    print("Tax=",tax,"L") 
    print("final income=",income-tax,"L")    
elif income>2.5 and income<=5:
    print("Income=",income,"L")
    tax=income*.05
    print("Tax=",tax,"L") 
    print("final income=",income-tax,"L")   
elif income>5 and income<=10:
    print("Income=",income,"L")
    tax=income*.1
    print("Tax=",tax,"L") 
    print("final income=",income-tax,"L")    
elif income>10:
    print("Income=",income,"L")
    tax=income*.2
    print("Tax=",tax,"L") 
    print("final income=",income-tax,"L")        