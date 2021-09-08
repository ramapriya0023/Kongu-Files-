class Filedata:
    def __init__(self,cost,max_size, files_avail,storage_cap,pass_protec,ads):
        self.cost=cost
        self.max_size=max_size
        self.storage_cap=storage_cap
        self.pass_protec=pass_protec
        self.ads=ads

    def filedata(plan="free"):
        cost = 0
        max_size=10
        files_avail=15
        storage_cap=50
        pass_protec="No"
        ads="Yes"
    def filedata(plan="pro"):
        cost = 1000
        max_size=100
        files_avail=None
        storage_cap=200
        pass_protec="Yes"
        ads="No"
    def filedata(plan="business"):
        cost = 3000
        max_size = 500
        files_avail = None
        storage_cap = 1500
        pass_protec = "Yes"
        ads = "No"
fileObj=Filedata()
fileObj.filedata("free")