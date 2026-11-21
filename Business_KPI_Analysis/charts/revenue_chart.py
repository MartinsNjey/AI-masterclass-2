import matplotlib.pyplot as plt

labels = ["Prior", "Current"]
revenue = [750000, 840000]

plt.bar(labels, revenue)
plt.title("Revenue Comparison")
plt.show()