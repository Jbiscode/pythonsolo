# import travel.thailand     # tavel.[]    []에는 모듈이나 패키지만 올수있다. 클래스나 함수는 못옴    from에서는 사용가능
# trip_to = travel.thailand.TailandPackage()
# trip_to.detail()


# from travel.thailand import TailandPackage
# trip_to = TailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from travel import *        # *(all)을 불러와도 공개된것과 비공개가 나뉘어서  __init__폴더에 all 설정해야함
trip_to = vietnam.VietnamPackage()
trip_to1 = thailand.TailandPackage() 
trip_to.detail()
trip_to1.detail()


import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))
 