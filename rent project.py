# ##-----NEW Project -----
# ## RENT PER PERSON
rent=int(input("enter your room rent="))
food=int(input("enter your amount of food ="))
electricity_spend=int(input("enter the total electricity spend="))
charge_per_unit=int(input("enter the charge per unit="))
person=int(input("enter the num of person living in the room="))

total_bill=electricity_spend*charge_per_unit
total_money_per_person=(food+rent+total_bill)//person
print("each person will pay",total_money_per_person)
