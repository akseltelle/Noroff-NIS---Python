import calculatepay

hourly = calculatepay.hourly_pay(40, 10)
monthly = calculatepay.monthly_pay(10, 50)

print('Hourly worker pay: ', hourly)
print('Monhly worker pay: ', monthly)


import calculatepay as pay

hourly = pay.hourly_pay(60, 10)
monthly = pay.monthly_pay(60, 50)

print('Hourly worker pay: ', hourly)
print('Monhly worker pay: ', monthly)




from calculatepay import hourly_pay as pay

hourly = pay(50, 10)

print('Hourly worker pay: ', hourly)