# Practice Problem
# Order Fulfillment Analysis
# Scenario: Here is a list of customer orders and asks you to identify which orders were delivered on time.
orders = [
    ["ORD001", 3, 3],
    ["ORD002", 5, 7],
    ["ORD003", 4, 2],
    ["ORD004", 6, 6],
    ["ORD005", 2, 5],
    ["ORD006", 7, 6]
]

# Each order contains three values:
# [order_id, promised_delivery_day, actual_delivery_day]
# For example, ["ORD002", 5, 7] means the order was promised on day 5 but arrived on day 7.

# Your tasks
# 1. Loop through every order.
# 2. Compare the actual delivery day with the promised delivery day.
# 3. Print one of these statuses for each order:
#    - "On Time" if the order arrives exactly on the promised day.
#    - "Early" if it arrives before the promised day.
#    - "Late" if it arrives after the promised day.
# 4. Count how many orders were delivered on time or early.
# 5. Count how many orders were delivered late.
# 6. Calculate the percentage of orders delivered on time or early.

# Use on-time calculation below:
# On-Time Delivery Rate = (orders delivered on time or early / Total orders) * 100

# Expected output format
# ORD001: On Time
# ORD002: Late
# ...
# Total Orders: X
# Orders Delivered On Time or Early: X
# Late Orders: X
# On-Time Delivery Rate: XX.XX%
total_orders = 0
delivery_time = 0
num_ontime_or_early = 0
num_late = 0
on_time_rate = 0

for order in orders:
    total_orders += 1
    delivery_time = (order[2] - order[1])
    if delivery_time == 0:
        num_ontime_or_early += 1
        print(f"{order[0]}: On Time")
    elif delivery_time < 0:
        num_ontime_or_early += 1
        print(f"{order[0]}: Early")
    else:
        num_late += 1
        print(f"{order[0]}: Late")

on_time_rate = (num_ontime_or_early / total_orders) * 100

print(f"Total Orders: {total_orders}")
print(f"Orders Delivered On Time or Early: {num_ontime_or_early}")
print(f"Late Orders: {num_late}")
print(f"On-Time Delivery Rate: {on_time_rate:.2f}%")

