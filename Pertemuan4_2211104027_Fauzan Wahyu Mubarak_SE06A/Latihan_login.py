login = 0
while True:
    username = input("Masukkan Username ")
    password = input("Masukkan Password ")

    if login == 3:
        print("Jajalen Sandi karo Password mungkin enek seng salah!")
        break
    if username == "fauzanwahyum" and password == "210310":
        print("Sugeng Rawuh", username, "!")
        break
    else:
        print("Login raiso, Dang dijajal maneh")
        login += 1 
