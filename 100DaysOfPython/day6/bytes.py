message=b"Here is your order!"


alt_message = bytearray(message)

alt_message[0] = ord("T")
alt_message[1] = ord("h")
alt_message[2] = ord("i")
alt_message[3] = ord("s")

check_message= memoryview(alt_message)

print(check_message[2:5].tobytes())