
# 车类
class Car():

    #车的颜色color = ''
    #车的型号model = ''
    #车牌号plate_number = ''
    #车主car_owner = ''
    def __init__(self,color,model,plate_number,car_owners):
        self.color = color
        self.model = model
        self.plate_number = plate_number
        self.car_owners = car_owners

    #车辆启动方法
    def car_start(self):
        print('车已启动')

    #车辆熄火方法
    def car_flameout(self):
        print('车已熄火')    

cars = Car('','','','')
