from datetime import datetime

a = 12312323
b = "12312323"

print("dasdasd")
print(a)
print(b)

print(type(a))
print(type(b))

lunch_start = 1200
lunch_finish = 1330

now = datetime.now()
current_time = now.strftime('%H%M')     # 시분만 가져오기 (예: "1230")
current_time_int = int(current_time)    # 문자열을 정수로 변환

if lunch_start <= current_time_int <= lunch_finish:
    print("현재는 점심시간입니다.")
else:
    print("식사시간이 아닙니다.")

print(now.time())
print(type(now.time()))
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

current_format = datetime.now()

print(current_format)
print(current_format.hour * 100 + current_format.minute)