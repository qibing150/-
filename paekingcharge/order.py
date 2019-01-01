
from park_record import Park_record


# 订单类
class Order():
    #停车费用/每小时park_money
    #订单编号order_id
    order_id = 0
    def __init__(self,park_money = 5):
        self.park_money = park_money

    #订单编号
    @classmethod
    def calculate(cls):
        cls.order_id += 1 
        return cls.order_id             