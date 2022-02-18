def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance,money):       #입금
    print("{1}원 입금이 확인되었습니다. 잔액은{0}원 입니다.".format(balance + money,money))
    return balance+money    #return(반환)을 통해서 함수에 값을 전달

def withdraw(balance,money):      #출금
    if balance >= money:
        print("{1}원 출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money,money))  
        return balance - money
    
    elif balance < money:
        print("{1}원 출금실패. 현재 남은 잔액은 {0}원 입니다.".format(balance,money))
        return balance

def withdraw_night(balance,money):
    수수료 = 100
    
    return 수수료, balance - money - 수수료 , money      

balance = 0
balance = deposit(balance,1000)
print(balance)

balance = withdraw(balance,500)
print(balance)


수수료,balance,money = withdraw_night(balance,200)      #수수료는 withdraw_night 안에 설정되어있고 불러오는역할
print("{2}원 야간 출금이 완료되었습니다. 수수료{0}원,잔액{1}원.".format(수수료,balance,money))
                                                                   #  {0}     {1}    {2}