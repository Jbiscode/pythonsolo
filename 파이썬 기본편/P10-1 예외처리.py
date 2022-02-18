# try:
#     print("나누기 전용 계산기 입니다")
#     num1 = int(input("숫자1  :"))
#     num2 = int(input("숫자2  :"))
#     print("{0}나누기{1} = {2}".format(num1,num2,int(num1/num2)))
    
# except ValueError:
#     print("값을 다시 입력하세요")
# except ZeroDivisionError as err:
#     print("::Error::",err)
    
    
    # 리스트를 이용한
try:
    print("나누기 전용 계산기 입니다")
    num = []
    
    num.append(int(input("숫자1  :")))
    num.append(int(input("숫자2  :")))
    num.append(int(num[0]/num[1]))
    
    print("{0}나누기{1} = {2}".format(num[0],num[1],num[2]))
    
except ValueError:
    print("값을 다시 입력하세요")
    
except ZeroDivisionError as err:
    print("::Error::",err)
    
except Exception as err:
    print("::Error::",err)
    
except:
    print("알수 없는 에러") 