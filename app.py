#Welcome messgae
print("Welcome to my Python program")

#Ask for daily sales
sales = input("How many sales did you make today")

#calculation
sales = float
weekly_sales = sales * 7

#convert to flaot

try:
  sales = float(sales)
except ValuieError:
  print(please enter a valid number.")
  exit()

#Display results
print(f" You are on track to make {weekly_sales} sales this week.")

