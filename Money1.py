def calculate_change(price, paid):
    if paid < price:
        return "เงินไม่พอสำหรับการชำระค่าสินค้า"

    change = paid - price
    denominations = {
        1000: 0,
        500: 0,
        100: 0,
        50: 0,
        20: 0,
        10: 0,
        5: 0,
        2: 0,
        1: 0,
    }

    for value in denominations.keys():
        denominations[value] = change // value
        change = change % value

    return denominations

def main():
    try:
        price = int(input("กรุณากรอกราคาสินค้า: "))
        paid = int(input("กรุณากรอกจำนวนเงินที่จ่าย: "))

        if price < 0 or paid < 0:
            print("กรุณากรอกจำนวนเงินที่เป็นบวก")
            return

        change = calculate_change(price, paid)

        if isinstance(change, str):
            print(change)
        else:
            total_change = sum([k * v for k, v in change.items()])
            print(f"\nจำนวนเงินทอน: {total_change} บาท")
            print("รายละเอียดเงินทอน:")
            for denom, count in change.items():
                if count > 0:
                    if denom >= 20:
                        print(f"{denom} บาท: {count} ใบ")
                    else:
                        print(f"{denom} บาท: {count} เหรียญ")

    except ValueError:
        print("กรุณากรอกจำนวนเงินที่ถูกต้อง")

if __name__ == "__main__":
    main()
