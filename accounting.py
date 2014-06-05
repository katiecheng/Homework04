def main():
    melon_cost = 1.00

    for line in open("customer_orders.csv"):
        
        line = line.rstrip()
        values = line.split(',')
        
        customer_name = values[1]
        customer_melons = float(values[2])
        customer_paid = float(values[3])
        customer_expected = customer_melons * melon_cost

        if customer_expected != customer_paid:
            print customer_name, "paid %.2f, expected %.2f"%(customer_paid, customer_expected)

if __name__ == "__main__":
    main()
