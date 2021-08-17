principle = int(input('Enter principle: '))
interest = float(input('Enter interest: '))/100
period = int(input('Enter period: '))

total = principle * (1 + interest) ** period

for x in range(0, period):
    total = principle * (1 + interest) ** x
    print(f"${round(total , 2)}")