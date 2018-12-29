


""" 使用面向对象的思路实现『停车收费』场景：
1. 车主开车进入停车场，产生停车记录，
2. 车主开车继续向前，将车停到车位上，修改前面的停车记录，
3. 车主停车完成，
一段时间(购物、吃饭...)之后，车主驾车准备离开停车场，
4. 车主开车离开车位，修改停车记录，
5. 车主开车到达出口，系统根据停车的时间生成订单，
6. 车主缴纳停车费，
7. 车主离开停车场。
至此，整个停车收费的场景完成。 """


import time
from Car import *

#停车收费类
class park():
    plateNum = ''
    #plateNum 车牌号  stopTime停车时间   drivTime出车时间 
    def __init__(self,stopTime=0, drivTime=0):
        self.stopTime = stopTime
        self.drivTime = drivTime

    #计算停车费用方法
    def exit(self):
            drivTime = time.time() #记录出车时间
            tt = drivTime - stopTime  #tt 在停车场的停车时间
            #计算小于1小时的费用
            if tt <3600:  
                print('您的停车费为5元')
                cars.out_park()
            #计算大于1小时的费用    
            else:
                num =((tt//3600)+1) * 5
                print('您的停车费为',num,'元')
                cars.out_park()
#创建车类实例
cars = car()
while True:
    #功能选择
    module_key = input(
        '''
        欢迎进入：
        1.停车
        2.出车
        3.退出系统   
        '''
        )
    if module_key == '3': #退出功能选择
        break
    elif module_key == '1':  #停车功能选择
        cars.into_park()
        pla = input('输入车牌号：') 
        #把车牌号存入变量
        plateNum = park(pla)
        #记录停车时间
        stopTime = time.time() 
        cars.into_stall()
        print('停车成功')
    #出车功能选项    
    elif module_key == '2':
        cars.out_stall()
        pl = input('输入车牌号：')
        #判断出车牌号是否与进车一致
        #一致 ：计算费用
        if pl == pla:
            #判断出车车辆
            carr = park(pl) 
            #调用收费方法
            carr.exit()
        #不一致：从新输入    
        else:
            print('车牌号不一致,请从新输入')
            time.sleep(2)
            continue    
    else:
        print('输入错误，请重新选择.')
    time.sleep(2)
    continue              

                