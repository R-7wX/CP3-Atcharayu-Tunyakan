# -------------------------------
# Store Program
# -------------------------------

# Define Username and Password
USERNAME = "admin"
PASSWORD = "1234"

# Products
products = {
    "1": ["ข้าวสาร", 50],
    "2": ["น้ำปลา", 25],
    "3": ["น้ำมันพืช", 45],
    "4": ["บะหมี่กึ่งสำเร็จรูป", 10],
    "5": ["ปลากระป๋อง", 30]
}


# Login Function
def login():
    print("=== ระบบล็อกอิน ===")
    username = input("กรอก Username: ")
    password = input("กรอก Password: ")

    if username == USERNAME and password == PASSWORD:
        print("\nเข้าสู่ระบบสำเร็จ! ยินดีต้อนรับคุณ", username)
        return True
    else:
        print("\nชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
        return False


# Catalog
def show_products():
    print("\n=== รายการสินค้า ===")
    for key, value in products.items():
        print(f"{key}. {value[0]} - {value[1]} บาท")


# Shopping Fuction
def shopping():
    cart = []
    while True:
        choice = input("พิมพ์หมายเลขสินค้าที่ต้องการซื้อ (หรือ 'q' เพื่อคิดเงิน): ")
        if choice.lower() == 'q':
            break
        elif choice in products:
            try:
                qty = int(input(f"จำนวน {products[choice][0]} ที่ต้องการซื้อ: "))
                if qty > 0:
                    cart.append((products[choice][0], products[choice][1], qty))
                else:
                    print("กรุณาใส่จำนวนที่มากกว่า 0")
            except ValueError:
                print("กรุณาใส่จำนวนเป็นตัวเลข")
        else:
            print("ไม่มีสินค้าที่เลือก กรุณาลองใหม่")
    return cart


# Checkout Function
def checkout(cart):
    print("\n=== สรุปรายการสั่งซื้อ ===")
    total = 0
    for item in cart:
        name, price, qty = item
        item_total = price * qty
        print(f"{name} x {qty} = {item_total} บาท")
        total += item_total
    print(f"\nราคารวมทั้งหมด: {total} บาท")
    print("ขอบคุณที่อุดหนุน!")


# -------------------------------
# Main
# -------------------------------
if login():
    show_products()
    cart = shopping()
    checkout(cart)
else:
    print("โปรแกรมจบการทำงาน")
