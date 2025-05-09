# class Serial:
#     def __init__(self, serial_id: int, name: str, budget: float, trp: float):
#         self.serial_id = serial_id
#         self.name = name
#         self.budget = budget
#         self.trp = trp

# class Channel:
#     def __init__(self, channel_name: str, serialList: list):
#         self.channel_name = channel_name
#         self.serialList = serialList

#     def sortSerialsByTRP(self):
#         if not self.serialList:
#             return None
#         return sorted(self.serialList, key=lambda serial: serial.trp)

# if __name__ == "__main__":
#     n = int(input())
#     serials = []
#     for _ in range(n):
#         serial_id = int(input())
#         name = input()
#         budget = float(input())
#         trp = float(input())
#         serial = Serial(serial_id, name, budget, trp)
#         serials.append(serial)

#     channel_name = "Star Plus"
#     channel = Channel(channel_name, serials)

#     sorted_serials = channel.sortSerialsByTRP()

#     if sorted_serials:
#         for serial in sorted_serials:
#             print(serial.trp)
#     else:
#         print("No Data Found")

n = int(input()) #indicates how many fields/entries will be there
ans = []
for _ in range(n):
    serial_id=input()
    name=input()
    budget=float(input())
    trp=float(input())
    ans.append(trp)
ans.sort()
    
if not ans:
    print("No Data Found")
else:
    for i in ans:
        print(i)

