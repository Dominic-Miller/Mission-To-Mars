
missions=[]
miles=[]
mphs=[]
f=open('marsdata.txt','r')
lines=f.readlines()
for line in lines:
  line=line.strip('\n')
  mission,mile_mph=line.split(':') #Splits the line at the : and assigns each side to a different value
  mile,mph=mile_mph.split(' ')
  # debug=input('stop')
  missions.append(mission)
  mile=float(mile)
  miles.append(mile)
  mph=float(mph)
  mphs.append(mph)
  # print(missions)
  # debug=input('stop')
 
  
#CREATING THE TIME FUNCTION AND APPLYING IT TO EACH mission


num=0
for mile in miles:
  miles[num]=(miles[num]*1000000) #Converts the millions of miles into miles
  num+=1

times=[]
def time(d,r):
  return (d/r)

num=0
for x in range(len(mphs)):
  Time=time(miles[num],mphs[num])
  times.append(Time)
  num+=1


# PRINTING THE LENGTH OF EACH MISSION IN NEW File

num=0
for mission in range(len(missions)):
  mission_time=times[num]
  outfile=open('LengthMissions','a')
  outfile.write(f'{missions[num]} time to mars: {int(mission_time//24)} days, {int(mission_time%24)} hours, {int((mission_time-int(mission_time))*60)} minutes, {int(((((mission_time-int(mission_time))*60)-(int((mission_time-int(mission_time))*60))))*60)} seconds.\n') #Complex because the total time in hours is converted into days, hours, minutes, and seconds
  num+=1
outfile.close()


#PRINTING THE LENGTH OF THE SHORTEST MISSION 


# print(min(times))

# print(missions[(times.index(min(times)))])

shortest_mission=(missions[(times.index(min(times)))])
shortest_time=(min(times))

print(f'{shortest_mission} has the shortest time: {int(shortest_time//24)} days, {int(shortest_time%24)} hours, {int((shortest_time-int(shortest_time))*60)} minutes, {int(((((shortest_time-int(shortest_time))*60)-(int((shortest_time-int(shortest_time))*60))))*60)} seconds.')


# print(int((shortest_time-int(shortest_time))*60))

# print(((shortest_time-int(shortest_time))-((shortest_time-int(shortest_time))*60)))

# print(int(((((shortest_time-int(shortest_time))*60)-(int((shortest_time-int(shortest_time))*60))))*60))

