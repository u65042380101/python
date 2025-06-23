คะแนน = int(input("กรอกคะแนนของคุณ: "))

if คะแนน >= 80:
    print("เกรด A")
elif คะแนน >= 75:
    print("เกรด B+")
elif คะแนน >= 70:
    print("เกรด B")
elif คะแนน >= 65:
    print("เกรด C+")
elif คะแนน >= 60:
    print("เกรด C")
elif คะแนน >= 55:
    print("เกรด D+")
elif คะแนน >= 50:
    print("เกรด D")
else:
    print("เกรด F (ตก)")
