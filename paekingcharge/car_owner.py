
# 车主类
class CarOwner():
    
    #车主姓名owner_name 
    #车主电话owner_phone 
    def __init__(self,owner_name,owner_phone):
        self.owner_name = owner_name
        self.owner_phone = owner_phone

    #车主驾驶方法
    def driver(self):
        print('车主已驾驶车辆')

    #车主缴费方法
    def pay_the_fees(self):
        print('车主已缴费')    
