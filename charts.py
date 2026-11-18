import matplotlib.pyplot as plt

months = ["Jan", "Feb" , "Mar", "Apr"]
sales = [1000, 2000, 1500, 3000]

plt.bar(months, sales)

plt.title("Monthly sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()