#derive 3e**x + 2ln(x)
deriv_f = "3e**x + 2/x"


### Your code here!
M1_ans1 = 3*1 + 1*0 #3
M1_ans2 = 0*1 + 2*0 #0
matrix_1 = [[M1_ans1,M1_ans2]]

M2_ans1 = 3*5 + 1*6 #21
M2_ans2 = 0*5 + 2*6 #12
matrix_2 = [[M2_ans1,M2_ans2]]


inventory = {'pumpkin' : 20,
             'fruit' : ['apple', 'pear'],
             'vegetable' : ['potato', 'onion', 'lettuce']}

inventory["meat"] = ["beef","chicken","pork"]
inventory["vegetable"].sort()
inventory["pumpkin"] += 5
print(inventory)