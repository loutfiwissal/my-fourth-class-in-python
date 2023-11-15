class mobile ():
    def __init__(self, name, serialnum, storage, dualsim, support4k) :
        self.name=name
        self.serialnum=serialnum
        self.storage=storage
        self.dualsim=dualsim
        self.support4k=support4k

    def info(self):
        print (" the mobile name {} his serialnum {} his storage {} dualsim {} support4k {}"
               .format(self.name, self.serialnum, self.storage, self.dualsim, self.support4k))

mobile1 = mobile("13 Pro Max", "XYOXYOY", "256GB", False,True)

mobile1.info()