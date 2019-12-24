class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("addr: ", self.addr)


def run():
    user = Contact("홍길동", '010XXXXXXXX', "xxxx1234@xxx.com", "서울시")
    user.print_info()


if __name__ == "__main__":
    run()
