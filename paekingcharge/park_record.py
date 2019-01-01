
# 停车记录类
class Park_record(object):
    #记录编号
    record_num = 0 
    def __init__(self,in_park_time,out_park_time,in_stall_time,out_stall_time):
        self.in_park_time = in_park_time #进入停车场时间
        self.out_park_time = out_park_time #出停车场时间
        self.in_stall_time = in_stall_time #进入车位时间
        self.out_stall_time = out_stall_time #出车位时间
    
    #计算记录编号
    @classmethod
    def getrecord_num(cls):
        cls.record_num += 1
        return cls.record_num

               
    
