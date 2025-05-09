class Doctor:
    def __init__(self,doctorId,doctorName,specialization,consultationFee):
        self.doctorId=doctorId
        self.doctorName=doctorName
        self.specialization=specialization
        self.consultationFee=consultationFee

class Hospital:
    def __init__(self,doctorDB):
        self.doctorDB=doctorDB

    def searchByDoctorName(self,doc_name):
        if self.doctorDB is None:
            return None
        doc_name=doc_name
        obj=[]
        for i in self.doctorDB:
            if(doc_name==i.doctorName):
                obj.append(i)
        return obj

    def calculateConsultationFeeBySpecialization(self,spez):
        if self.doctorDB is None:
            return None
        spez=spez
        sum=0
        for i in self.doctorDB:
            if(spez==i.specialization):
                sum+=i.consultationFee
        return sum

if __name__=="__main__":
    n=int(input())
    doc_list=[]
    for i in range(n):
        doctorId=int(input())
        doctorName=input()
        specialization=input()
        consultationFee=int(input())
        d=Doctor(doctorId,doctorName,specialization,consultationFee)
        doc_list.append(d)
    doc_name=input()
    spez=input()

    h=Hospital(doc_list)
    ans1=h.searchByDoctorName(doc_name)

    if ans1 is None:
        print("No Doctor Exists with the given DoctorName")
    else:
        for i in ans1:
            print(i.doctorId)
            print(i.doctorName)
            print(i.specialization)
            print(i.consultationFee)

    ans2=h.calculateConsultationFeeBySpecialization(spez)
    if ans2 is None:
        print("No Doctor with the given specialization")
    else:
        print(ans2)


