phone_book_list = [] # 데이터를 저장할 빈 리스트

def insert_data():
    print("-------------------------입력기능----------------------")
    name = input("성명>>> ")
    phone = input("전화>>> ")
    address = input("주소>>> ")
    phone_book_list.append({"name": name, "phone": phone, "address": address})
    print("주소 입력 완료!")

def print_all_data():
    print("-------------------------출력기능----------------------")
    if not phone_book_list:
        print("등록된 전화번호가 없습니다.")
        return
    print("번호         성명                             전화                               주소")
    print("---------------------------------------------------------------")
    for index, user in enumerate(phone_book_list, start=1):
        print(f"{str(index).ljust(12)}{user['name'].ljust(25)}{user['phone'].ljust(35)}{user['address']}")

def search_data():
    print("-------------------------- 검색기능--------------------------")
    search_name = input("이름을 입력해주세요\n이름: ")
    results = [(i, u) for i, u in enumerate(phone_book_list, start=1) if u['name'] == search_name]
    if not results:
        print(f"'{search_name}'님으로 등록된 정보가 없습니다.")
        return
    print("번호         성명                             전화                               주소")
    print("---------------------------------------------------------------")
    for idx, user in results:
        print(f"{str(idx).ljust(12)}{user['name'].ljust(25)}{user['phone'].ljust(35)}{user['address']}")

def update_data():
    print("---------------------------수정기능-------------------------")
    search_name = input("수정할 성명을 입력하세요: ")
    for user in phone_book_list:
        if user['name'] == search_name:
            print("수정할 이름, 연락처,주소를 입력하세요")
            user['name'] = input("새로운 이름: ")
            user['phone'] = input("새로운 전화번호: ")
            user['address'] = input("새로운 주소 : ")
            print("연락처가 수정되었습니다")
            return
    print(f"'{search_name}'님으로 등록된 정보가 없어 수정을 진행할 수 없습니다.")

def delete_data():
    print("----------------------------삭제기능-------------------------")
    search_name = input("삭제할 성명을 입력하세요 : ")
    for user in phone_book_list:
        if user['name'] == search_name:
            phone_book_list.remove(user)
            print("정보가 삭제되었습니다")
            return
    print("해당하는 정보가 없습니다")