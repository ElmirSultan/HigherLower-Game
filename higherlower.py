from datam import datam as dt
import random


print(""" 
  __  __                                         __                                          
/\ \/\ \                                       /\ \                                         
\ \ \_\ \    ___   __  __  __     __   _ __    \ \ \        ___   __  __  __     __   _ __  
 \ \  _  \  / __`\/\ \/\ \/\ \  /'__`\/\`'__\   \ \ \  __  / __`\/\ \/\ \/\ \  /'__`\/\`'__\
  \ \ \ \ \/\ \L\ \ \ \_/ \_/ \/\  __/\ \ \/     \ \ \L\ \/\ \L\ \ \ \_/ \_/ \/\  __/\ \ \/ 
   \ \_\ \_\ \____/\ \___x___/'\ \____\\ \_\      \ \____/\ \____/\ \___x___/'\ \____\\ \_\ 
    \/_/\/_/\/___/  \/__//__/   \/____/ \/_/       \/___/  \/___/  \/__//__/   \/____/ \/_/ 
""")



is_game_finished = False


count = 0
right_answer = 0 

def get_random_indexes():
    index1 = random.randint(0, len(dt)-1)
    index2 = random.randint(0, len(dt)-1)
    while index2 == index1:
        index2 = random.randint(0, len(dt)-1)
    return index1, index2


def hoverlower():
    global right_answer 
    
    random_indexA, random_indexB = get_random_indexes()
    random_catchA = dt[random_indexA]
    random_catchA_name = random_catchA["name"]
    random_catchA_job = random_catchA["description"]
    random_catchA_country = random_catchA["country"]
    random_catchA_follower = random_catchA["followers"]

    random_catchB = dt[random_indexB]
    random_catchB_name = random_catchB["name"]
    random_catchB_job = random_catchB["description"]
    random_catchB_country = random_catchB["country"]
    random_catchB_follower = random_catchB["followers"]

    print(f"Compare A : {random_catchA_name}, a {random_catchA_job}, from {random_catchA_country}")
    print(f"Against B : {random_catchB_name}, a {random_catchB_job}, from {random_catchB_country}")

    choice = input("A or B ?").lower()
    

    if choice == "a" and random_catchA_follower > random_catchB_follower:
        print("correct \n")
        print(f"{random_catchB_name} : {random_catchB_follower}")
        print(f"{random_catchA_name} : {random_catchA_follower}")
        right_answer += 1    
    elif choice == "b" and random_catchB_follower > random_catchA_follower:
        print("correct \n")
        print(f"{random_catchB_name} : {random_catchB_follower}")
        print(f"{random_catchA_name} : {random_catchA_follower}")
        right_answer += 1

    else:
        print("wrong \n")
        print(f"{random_catchB_name} : {random_catchB_follower}")
        print(f"{random_catchA_name} : {random_catchA_follower}")

    

while count < len(dt):
    count += 1
    is_game_finished = True
    print(count)
    hoverlower()
    if count >= len(dt):
        print("The game finished")
        print(f"Your total score is: {right_answer}")
        break
        








