class Baggage: #定義行李類別
    def __init__(self, baggage_id, baggage_weight, baggage_in_airport, baggage_out_airport, baggage_name): #定義建構子，有行李ID、旅客姓名、行李重量、出發機場、目的地機場
        #定義行李ID、旅客姓名、行李重量、出發機場、目的地機場的屬性
        self.baggage_id = baggage_id
        self.baggage_weight = baggage_weight
        self.baggage_in_airport = baggage_in_airport
        self.baggage_out_airport = baggage_out_airport
        self.baggage_name = baggage_name

    def baggage_info(self): #輸出所有資料的副函式
        print("行李ID:", self.baggage_id)
        print("旅客姓名:", self.baggage_name)
        print("行李重量:", self.baggage_weight)
        print("出發機場:", self.baggage_in_airport)
        print("目的地機場:", self.baggage_out_airport)

    def modify(self): #修改資料用的副函式
        print("1. 修改旅客姓名")
        print("2. 修改行李重量")
        print("3. 修改出發機場")
        print("4. 修改目的地機場")

        #根據選擇要修改的選向來直接修改原本的資料
        choice = input("請選擇要修改的項目 (輸入對應的數字): ") 

        if choice == "1":
            self.baggage_name = input("請輸入新的旅客姓名: ")
        elif choice == "2":
            self.baggage_weight = int(input("請輸入新的行李重量: "))
        elif choice == "3":
            self.baggage_in_airport = input("請輸入新的出發機場: ")
        elif choice == "4":
            self.baggage_out_airport = input("請輸入新的目的地機場: ")
        else:
            print("無效的選擇")


class Airpass: #定義登機證類別
    def __init__(self, pass_name, pass_id, pass_time, pass_gate_id, pass_sit, pass_number, baggage_id): #定義建構子，有旅客姓名、登機證編號、登機時間、登機門編號、座號位置、行李件數、行李ID
        self.pass_name = pass_name
        self.pass_id = pass_id
        self.pass_time = pass_time
        self.pass_gate_id = pass_gate_id
        self.pass_sit = pass_sit
        self.pass_number = pass_number
        self.baggage_id = baggage_id

    def pass_info(self):#輸出所有資料的副函式
        print("旅客姓名:", self.pass_name)
        print("登機證編號:", self.pass_id)
        print("登機時間:", self.pass_time)
        print("登機門編號:", self.pass_gate_id)
        print("座號位置:", self.pass_sit)
        print("行李件數:", self.pass_number)
        print("行李ID:", self.baggage_id)

    def modify(self):#根據選擇要修改的選向來直接修改原本的資料
        print("1. 修改旅客姓名")
        print("2. 修改登機證編號")
        print("3. 修改登機時間")
        print("4. 修改登機門編號")
        print("5. 修改座號位置")
        print("6. 修改行李件數")
        print("7. 修改行李ID")

        choice = input("請選擇要修改的項目 (輸入對應的數字): ")

        if choice == "1":
            self.pass_name = input("請輸入新的旅客姓名: ")
        elif choice == "2":
            self.pass_id = input("請輸入新的登機證編號: ")
        elif choice == "3":
            self.pass_time = input("請輸入新的登機時間: ")
        elif choice == "4":
            self.pass_gate_id = input("請輸入新的登機門編號: ")
        elif choice == "5":
            self.pass_sit = input("請輸入新的座號位置: ")
        elif choice == "6":
            self.pass_number = input("請輸入新的行李件數: ")
        elif choice == "7":
            self.baggage_id = input("請輸入新的玲李ID: ")
        else:
            print("無效的選擇")

def main():
    choice = input("請選擇要操作的功能 (1. 行李, 2. 登機證): ")

    if choice == "1":
        #建立行李類別的物件
        baggage1 = Baggage("A123", 20, "臺南機場", "東京機場", "高盛新")
        baggage2 = Baggage("B456", 15, "臺北機場", "成田機場", "林又與")
        baggage3 = Baggage("C789", 25, "桃園機場", "札幌機場", "王文心")
        #用類別物件建立清單並根據後續的輸入項查詢
        baggage_list = [baggage1, baggage2, baggage3]
        
        search_id = input("請輸入行李ID: ")
        #初始化查詢結果
        found_baggage = None

        for baggage_object in baggage_list:
            if baggage_object.baggage_id == search_id:
                found_baggage = baggage_object
                break
        #選擇要操作的功能
        if found_baggage:
            operation = input("選擇操作 (1. 查詢, 2. 修改): ") #查詢/修改

            if operation == "1":
                found_baggage.baggage_info() #呼叫輸出所有資料的副函式
            elif operation == "2":
                found_baggage.modify() #呼叫修改資料的副函式
                print("行李資料已更新")
                found_baggage.baggage_info() #呼叫輸出資料的副函式
            else:
                print("無效的選擇")

        else:
            print("未找到與輸入ID相符的行李")

    elif choice == "2":
        #建立登機證類別的物件
        pass1 = Airpass("高盛新", "A1234", "2023/9/5 10:51", "C1", "A/3", 1, "A123")
        pass2 = Airpass("林又與", "B4567", "2023/9/7 8:56", "A2", "B/9", 1, "B456")
        pass3 = Airpass("王文心", "C8912", "2023/9/6 9:24", "B3", "C/6", 1, "C789")
        #用類別物件建立清單並根據後續的輸入項查詢
        pass_list = [pass1, pass2, pass3]
        
        search_name = input("請輸入旅客姓名: ")
        #初始化查詢結果
        found_airpass = None

        for airpass_object in pass_list:
            if airpass_object.pass_name == search_name:
                found_airpass = airpass_object
                break

        if found_airpass:
            operation = input("選擇操作 (1. 查詢, 2. 修改): ")

            if operation == "1":
                found_airpass.pass_info() #呼叫輸出所有資料的副函式
            elif operation == "2":
                found_airpass.pass_info() #呼叫修改資料的副函式
                print("---------------------------------------")
                print("登機證資料已更新")
                found_airpass.pass_info() #呼叫輸出資料的副函式
            else:
                print("無效的選擇")

        else:
            print("未找到與輸入姓名相符的登機證")

    else:
        print("無效的選擇")


if __name__ == "__main__":
    main()
