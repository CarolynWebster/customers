melon_cost = 1.00
log_file = open("customer-orders.txt")


def check_payment(customer_name, melons, total_paid):
    total_expected = melons * melon_cost
    if total_expected != total_paid:
        amount_owed = total_expected - total_paid
        print customer_name, "paid {:.2f}, expected {:.2f}. Amount owed {:.2f}".format(total_paid, total_expected, amount_owed)
    else:
        amount_owed = 0
    return amount_owed

total_underpayment = 0.0
for line in log_file:
    line = line.rstrip()
    cust_info = line.split("|")
    customer_name = cust_info[1]
    melons = int(cust_info[2])
    total_paid = float(cust_info[3])
    total_underpayment += (check_payment(customer_name, melons, total_paid))
print "Overall we are missing ${}!!!".format(total_underpayment)
