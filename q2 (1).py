'''This code will ask the user for the total amount they have spent at Metro,and determine an according discount, if one is applicable.'''
#Ask the user for the totol amount spent.
amountSpent = int(input('Please enter the amount you have spent at Metro:'))

if amountSpent < 10:
    print ('You have not qualified for a discount.')

if 10 <= amountSpent < 50:
    cuponAmount = amountSpent * 0.05
    print ('You have earned a coupon worth','$',format (cuponAmount,'.2f'),'.')

elif 50 <= amountSpent < 100:
    cuponAmount = amountSpent *0.10
    print ('You have earned a coupon worth','$',format (cuponAmount,'.2f'),'.')

elif 100 <= amountSpent <150:
    cuponAmount = amountSpent *0.12
    print ('You have earned a coupon worth','$',format (cuponAmount,'.2f'),'.')

elif amountSpent >= 150: 
    cuponAmount  = amountSpent *0.15
    print ('You have earned a coupon worth','$',format (cuponAmount,'.2f'),'.')

'''The code has ended after giving the user an appropriate response as to whether they have received a discount.'''
