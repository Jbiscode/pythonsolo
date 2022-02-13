from itertools import count


class House:
    def __init__(self,location,house_type,deal_type,price,completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
        
        
        
    def show_detail(self):
        print("{0} {1} {2} {3} {4}".format(self.location,self.house_type,self.deal_type,self.price,self.completion_year))
        
        

매물들 = []
        
매1= House("강남","아파트","매매","10억","2010년")
매2 = House("마포","오피스텔","전세","5억","2007년")
매3 = House("송파","빌라","월세","500/50","2000년")

매물들.append(매1)
매물들.append(매2)
매물들.append(매3)

print("총 {}대의 매물이 있습니다.".format(len(매물들)))
for 매물 in 매물들:
    매물.show_detail()