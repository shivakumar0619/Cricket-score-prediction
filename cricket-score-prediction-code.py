total_overs=int(input("Enter total no of overs: "))
runs = int(input("Enter current runs: "))
overs_completed = float(input("Enter overs completed: "))
wickets = int(input("Enter wickets lost: "))
run_rate = runs / overs_completed
remaining_overs = total_overs - overs_completed

if wickets == 0:
    predicted_score = ( runs + (run_rate * remaining_overs) )- 0
elif wickets in (1,2):
    predicted_score = (runs + (run_rate * remaining_overs) )-(runs*0.05) #0.05 is percentage of 5
elif wickets in (3,4):
    predicted_score = (runs + (run_rate * remaining_overs) )-(runs*0.1)
elif wickets in (5,6):
    predicted_score = (runs + (run_rate * remaining_overs) )-(runs*0.15)
elif wickets == 7:
    predicted_score = (runs + (run_rate * remaining_overs) )-(runs*0.2)
elif wickets == 8:
    predicted_score = (runs + (run_rate * remaining_overs) )-(runs*0.25)
elif wickets == 9:
    predicted_score = (runs + (run_rate * remaining_overs) )-(runs*0.27)
else: 
    predicted_score = (runs + (run_rate * remaining_overs) )-(runs*0.3)
    
print("predicted_score: ",int(predicted_score))
