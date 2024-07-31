for i in range(0, len(xored_flag)):
    flag += chr(ord(password[i]) ^ ord(xored_flag[i % len(password)]))
