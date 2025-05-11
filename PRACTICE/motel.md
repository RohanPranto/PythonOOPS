You are given details of multiple motels. Each motel has the following attributes:

roomId (Integer): Unique ID for the motel room

numberOfRooms (Integer): Number of rooms in the motel

cabFacility (String): Indicates if cab facility is available (yes or no)

bills (Integer): Total bill amount for the motel

name (String): Name of the motel

✍️ Input Requirements:
First, take an integer input n – the number of motels.

Then, for each of the n motels, take inputs in the following order:

roomId (int)

numberOfRooms (int)

cabFacility (String)

bills (int)

name (String)

✅ Task 1:
Find and print the names of motels that have cab facility available (cabFacility = "yes").
Matching should be case-insensitive.

✅ Task 2:
Take an integer input called threshold.

Calculate and print the total bills of motels where numberOfRooms is greater than the given threshold.

Sample input 1
5
101
10
yes
5000
Sunrise Inn
102
8
no
3000
Moonlight Stay
103
15
yes
7000
Star Hotel
104
6
no
2000
Hill View
105
20
yes
9000
Sea Breeze
10

Sample Output:
Sunrise Inn
Star Hotel
Sea Breeze
16000

Sample input 2
3
201
5
no
1500
Green View
202
7
no
4500
Blue Hill
203
9
no
3200
River Side
10

Sample output 2
0
