from os import device_encoding


class Info:
    def __init__(self,userId,deviceId,value,month,year,userAddress):
        self.userId = userId
        self.deviceId = deviceId
        self.value=value
        self.month=month
        self.year=year
        self.userAddress=userAddress