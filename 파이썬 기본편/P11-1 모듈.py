import theater_module
theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(5)

print("-------------------------")
import theater_module as mv             #모듈은 mv로 별명사용
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

print("-----------------------")
from theater_module import *
# from random import *             # *은 모든함수불러오기, 또는 필요한것만 지칭해서 불러올수있음 e.g)price,price_morning (일반,조조)만 불러오기
price(3)
price_morning(4)
price_soldier(5)

print("-------------------------")
from theater_module import price_soldier as price            # 군인할인만 필요해서 불러오고 그것만 별명 따로 붙혀 정의하는것
price(3)               #여기서 price는 price_soldier 을 의미한다
# price_soldier(3)       # 별명을 붙혔기때문에 price_soldier 라고 치면 안나온다. 
