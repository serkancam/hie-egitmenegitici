class FileTool():
    __extension = ".csv"

    def __init__(self, address="kayit", **kwargs):
        self.address = address + FileTool.__extension
        self.file = self.openFile()
        self.fields = ["Adı", "Soyadı", "Telefon"]
        self.records = self.file.readlines()
        for key, value in kwargs.items():
            if key == "fields":
                self.fields = value

    def openFile(self):
        import os
        if os.path.exists(self.address):
            return open(self.address, "r+", encoding="utf-8")
        else:
            return open(self.address, "w+", encoding="utf-8")

    def getEntries(self):
        entries = []
        for item in self.fields:
            entries.append(input(f"{item} giriniz:"))
        record = ";".join(entries)+"\n"
        return record

    def listRecords(self):
        for i in range(len(self.records)):
            print(f"{i+1}", *self.records[i].split(";"), end="")

    def insertRecord(self):
        self.records.append(self.getEntries())

    def updateRecord(self):
        self.listRecords()
        recordIndex = int(input("değişecek kaydın numarasını giriniz:"))
        self.records[recordIndex-1] = self.getEntries()

    def deleteRecord(self):
        self.listRecords()
        recordIndex = int(input("silinecek kaydın numarasını giriniz:"))
        del self.records[recordIndex-1]

    def menu(self):
        menu = """
        1- listeleme
        2- Ekleme
        3- Güncelleme 
        4- Silme
        5- Çıkış
        işlem seçiniz
        """

        liste = [self.listRecords, self.insertRecord,
                 self.updateRecord, self.deleteRecord]
        switchKey = 1

        while switchKey == 1:
            choice = int(input(menu))
            if 0 < choice < 5:
                liste[choice-1]()
            elif choice == 5:
                switchKey = 0
        else:
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(self.records)
            self.file.flush()
    
    
    def __str__(self):
        return self.address

    def __del__(self):
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(self.records)
        self.file.close()


telefonDefter = FileTool()
telefonDefter.menu()




BankaIslemleri = FileTool(address="Account",fields=["Banka Adı","Tutar","Tip"])
BankaIslemleri.Menu()


print(BankaIslemleri.__dict__["fields"])
