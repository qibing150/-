from park import Park
#车位类
class Stall(Park):

    #stall_id 车位编号
    #stall_state 车位状态 是否已停车
    #stall_quantity 剩余车位数量
    #stall_number 车位总数量
    def __init__(self,stall_id,stall_state,stall_quantity=50,stall_number=100):
        self.stall_id = stall_id
        self.stall_state = stall_state
        self.stall_quantity = stall_quantity
        self.stall_number = stall_number
    
    #车辆进入车位
    def enter_stall(self):
        stalls.stall_quantity += 1
        print('车位剩余',stalls.stall_quantity)
        return stalls.stall_quantity


    #车辆离开车位
    def leave_stall(self):
        stalls.stall_quantity -= 1
        print('车位剩余',stalls.stall_quantity)
        return stalls.stall_quantity       
     
stalls = Stall(1,'',)
