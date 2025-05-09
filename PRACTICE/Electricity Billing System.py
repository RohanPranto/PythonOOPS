class Bill:
    def __init__(self, billNo, name, typeOfConnection, billAmount, status):
        self.__billNo = billNo
        self.__name = name
        self.__typeOfConnection = typeOfConnection
        self.__billAmount = billAmount
        self.__status = status

    def getBillNo(self):
        return self.__billNo

    def getName(self):
        return self.__name

    def getTypeOfConnection(self):
        return self.__typeOfConnection

    def getBillAmount(self):
        return self.__billAmount

    def getStatus(self):
        return self.__status


class Solution:
    @staticmethod
    def findBillWithMaxBillAmountBasedOnStatus(billList, status):
        filtered = [b for b in billList if b.getStatus() == status]
        if not filtered:
            return None
        max_amt = max(b.getBillAmount() for b in filtered)
        result = [b for b in filtered if b.getBillAmount() == max_amt]
        return sorted(result, key=lambda x: x.getBillNo())

    @staticmethod
    def getCountWithTypeOfConnection(billList, connectionType):
        count = 0
        for b in billList:
            if b.getTypeOfConnection().lower() == connectionType.lower():
                count += 1
        return count


# Main Code
if __name__ == "__main__":
    n = int(input())
    bills = []
    for _ in range(n):
        billNo = int(input())
        name = input()
        typeOfConnection = input()
        billAmount = float(input())
        status = input().lower() == "true"
        bills.append(Bill(billNo, name, typeOfConnection, billAmount, status))

    status_input = input().lower() == "true"
    type_input = input()

    result_bills = Solution.findBillWithMaxBillAmountBasedOnStatus(bills, status_input)
    if result_bills:
        for bill in result_bills:
            print(f"{bill.getBillNo()}#{bill.getName()}")
    else:
        print("There are no bill with the given status")

    count = Solution.getCountWithTypeOfConnection(bills, type_input)
    if count > 0:
        print(count)
    else:
        print("There are no bills with given type of connection")
