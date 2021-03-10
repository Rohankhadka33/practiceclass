''' The cost of the house is $1M. If the buyer has good credit, they need to put down  10% otherwise they need to put
 down 20%. print the down payment.'''
cost_of_house= 1000000
credit= True
if(credit==True):
    discount=10/100
    cost_of_house= cost_of_house-cost_of_house*discount
    print(cost_of_house)
else:
    discount= 20/100
    cost_of_house= cost_of_house-cost_of_house*discount
    print(cost_of_house)