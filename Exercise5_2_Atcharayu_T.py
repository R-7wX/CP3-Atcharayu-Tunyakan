#Input Section
distance = int(input("กรอกระยะทาง (หน่วยเป็นกิโลเมตร): "))
time = int(input("กรอกเวลา (หน่วยเป็นชั่วโมง): "))

#Check Section
if time == 0:
    print("เวลาไม่สามารถเป็นศูนย์ได้")
else:
    speed = distance / time
    print(f"อัตราเร็วคือ {speed} กิโลเมตรต่อชั่วโมง")