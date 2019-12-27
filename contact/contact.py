class Contact:  # Contact 클래스 생성
    def __init__(self, name, phone_number, e_mail, addr):  # Contact 생성자, 클래스 메소드에선 가장 앞에 self 인자가 있어야 함.
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):  # Contact 정보 출력 메소드
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)


def print_menu():  # 프로그램 메뉴 출력 메소드
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴 선택")
    return int(menu)


def store_contact(contact_list):  # Contact 정보 메모장에 저장하는 메소드
    txt = open("./contact/contact.txt", "wt")
    for contact in contact_list:
        txt.write(contact.name + '\n')
        txt.write(contact.phone_number + '\n')
        txt.write(contact.e_mail + '\n')
        txt.write(contact.addr + '\n')
    txt.close()


def load_contact(contact_list):
    txt = open("./contact/contact.txt", "rt")
    lines = txt.readlines()
    num = len(lines) / 4
    num = int(num)

    for i in range(num):
        name = lines[4 * i].rstrip('\n')
        phone = lines[4 * i + 1].rstrip('\n')
        email = lines[4 * i + 2].rstrip('\n')
        addr = lines[4 * i + 3].rstrip('\n')
        contact = Contact(name, phone, email, addr)
        contact_list.append(contact)
    txt.close()


def print_info(print_list):  # Contact들의 정보를 출력하는 메소
    for contact in print_list:
        contact.print_info()


def set_contact():  # Contact 정보를 입력하는 메소드
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact


def delete_contact(contact_list, name):  # Contact 정보를 삭제하는 메소드
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]


def run():
    contact_list = []
    load_contact(contact_list)
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 2:
            print_info(contact_list)
        elif menu == 3:
            name = input("Name: ")
            delete_contact(contact_list, name)
        elif menu == 4:
            store_contact(contact_list)
            break


if __name__ == "__main__":
    run()
