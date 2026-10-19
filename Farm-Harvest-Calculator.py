Field1=(10)
Field2=(35)
Field3=(24)
Field4=(55)
Field5=(33)
total=(Field1+Field2+Field3+Field4+Field5)
print("Total Harvest: " , total , "Kg" )

average=total/5
print("Average per field: ",average,"Kg")

price_per_Kg=15
earning=total*price_per_Kg
print("Total Earnings: Rs. ",earning)

bags= total//25
leftover=total%25

print("Full Bags packed:",bags)
print("Leftover Grain:",leftover,"Kg")

last_year=500
print("Better than last year?" , total>last_year)
print("Same as last year?",total==last_year)
print("Atleast as good?",total>=last_year)

total=total+30
print("After bonus crop: ",total,"Kg")
total-=15
print("After seed reserve: ",total,"Kg")

