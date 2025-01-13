def compute_net_amount():
    net_amount = 0
    while True:
        transaction = input("Enter transaction (or press Enter to stop): ")
        if not transaction:
            break
        transaction_type, amount = transaction.split()
        amount = int(amount)

        if transaction_type == 'D':
            net_amount += amount
        elif transaction_type == 'W':
            net_amount -= amount

    print(net_amount)

compute_net_amount()
