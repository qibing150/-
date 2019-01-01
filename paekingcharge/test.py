from car import Car
from door import Door
from stall import Stall
from order import Order
from car_owner import CarOwner
from park_record import Park_record
import car_owner

import time
#测试类
class Test(object):
    
        while True:
            print("""
            —————————————————————————
          |***欢迎进入筑梦园停车场***|
            —————————————————————————          
            """)
            module_key = input(
            '''
            1.进入停车场
            2.离开停车场
            3.退出系统   
            ''')
            if module_key == '3': #退出功能选择
                break
            elif module_key == '1':  #进入停车场功能选择
                Car.plate_number = input('请输入车牌号')
                #调用停车场开门方法
                doors = Door()
                doors.open_the_door()
                time.sleep(1)
                #调用车主驾驶方法
                carOwners = CarOwner('','')
                carOwners.driver()
                time.sleep(1)
                #调用车辆启动方法
                cars = Car('','',Car.plate_number,'')
                cars.car_start()
                time.sleep(1)
                
                #记录进入停车场时间
                park_records = Park_record('','','','')
                park_records.in_park_time = time.time()
                interTime = time.time()
                time.sleep(1)
                #调用车辆进入车位方法
                stalls = Stall('','')
                stalls.enter_stall()
                time.sleep(1)
                #记录进入车位时间
                park_records.in_stall_time = time.time()
                #调用车辆熄火方法
                cars.car_flameout()
                time.sleep(1)
                print('停车成功')
            elif module_key == '2':
                #调用车辆启动方法
                cars.car_start()
                time.sleep(1)
                #调用离开车位方法
                stalls.leave_stall()
                time.sleep(1)
                #记录出车位时间
                park_records.out_stall_time = time.time
                pl = input('输入车牌号：')
                if pl == Car.plate_number:
                    #记录出停车场时间
                    park_records.out_park_time = time.time
                    stopTime = time.time()
                    tt = interTime - stopTime
                    if tt < 3600:
                        print('您的停车费用为5元')
                        #调用缴费方法
                        carOwners.pay_the_fees()
                        time.sleep(1)
                        #停车场门开
                        doors.open_the_door()
                        time.sleep(1)
                    else:
                        num =((tt//3600)+1) * 5
                        print('您的停车费为',num,'元') 
                else:
                    print('车牌号不一致,请从新输入')
                    time.sleep(2)
                    continue 
            else:
                print('输入错误，请重新选择.')
            time.sleep(2)

Test()