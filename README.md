This code tracks daily sales of a company and then calculates with those daily sales how many weekly sales are being made.

python app.py




# python_github_assignment
#sales tracker

#welcome message
print("Welcome to my Python program")

#ask for daily sales
sales = input("How many sales did you make today?")

#convert to float
sales = float(sales)

#calculate weekly estimate
weekly_sales = sales * 7

#display result
print(f"you are on track to make {weekly_sales} sales this wee.")
sales = flaot(sales)
except ValueError:
    print("Please enter a valid number.")
    exit()
