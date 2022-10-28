try: 

    while True:

        goals =input()

    

        team_a = 0

        team_b = 0

        for i,goal in enumerate(goals):

            if i < 10:

                if i % 2 == 0:

                    team_a += int(goal)

                else:

                    team_b += int(goal)

                

                if (team_b - team_a) > 5 - (i+2)//2:

                    print("TEAM-B", i+1)

                    break

                elif (team_a - team_b) > (5 - (i+1)//2):

                    print("TEAM-A", i+1)

                    break

                    

            else:

                if i % 2 == 0:

                    last = int(goal)

                else:

                    current = int(goal)

                    

                    if last == current:

                        pass

                    elif last > current:

                        print("TEAM-A", i+1)

                        break

                    else:

                        print("TEAM-B", i+1)

                        break

        else:

            print("TIE")

                        

except:

    pass

