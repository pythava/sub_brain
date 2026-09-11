import windows

def main():
        while(True):
                print("My sub_brain")
                print("어떤 작업을 원하시나요?")
                print("[1] 알림 작업\n[2] 메모리 작업")
                work_ans = input()
                if work_ans == "1":
                        print("언제 알람을 받고 싶으신가요?")
                        print("=" * 30)
                        print("[1] 특정 시간에")
                        print("[2] 특정 날짜 특정 시간에")
                        alert_ans = input()
                        if alert_ans == "1":
                                print("시간을 입력해주세요 (예 : 14 : 03)")
                                j_alert_time = input()
                        else:
                                print("날짜를 입력해주세요 (예 : 4 / 12)")
                                t_alert_date = input()
                                print("시간을 입력해주세요 (예 : 14 : 03)")
                                t_alert_time = input()
                elif work_ans == "2":
                        print("메모리 작업")
                else: 
                        print("다시 입력해주세요")


if __name__=="__main__":
        main()

