# 데이터를 담을 빈 리스트 생성
phone_book_list = []

def insert_data():
    print("-------------------------입력기능----------------------")
    # 실행 화면에 나온 >>> 모양을 그대로 살렸습니다.
    name = input("성명>>> ")
    phone = input("전화>>> ")
    address = input("주소>>> ")
    
    # 입력받은 정보를 딕셔너리로 만듭니다.
    user_info = {
        "name": name,
        "phone": phone,
        "address": address
    }
    
    # 리스트에 추가합니다.
    phone_book_list.append(user_info)
    print("주소 입력 완료!")

def print_all_data():
    print("-------------------------출력기능----------------------")
    if not phone_book_list:
        print("등록된 전화번호가 없습니다.")
        return
        
    # 리스트 안의 딕셔너리들을 하나씩 꺼내서 출력합니다.
    for index, user in enumerate(phone_book_list, start=1):
        print(f"[{index}] 성명: {user['name']} | 전화: {user['phone']} | 주소: {user['address']}")
        
def search_data():
    print("-------------------------- 검색기능--------------------------")
    print("이름을 입력해주세요")
    search_name = input("이름: ")
    
    # 입력한 이름과 일치하는 데이터가 있는지 먼저 확인합니다.
    # 리스트 안의 딕셔너리들을 돌면서 'name'이 일치하는 것만 추려냅니다.
    results = []
    for index, user in enumerate(phone_book_list, start=1):
        if user['name'] == search_name:
            # 나중에 출력할 때 원래 몇 번째 번호였는지 알기 위해 index도 함께 저장합니다.
            results.append((index, user))
    
    # 검색 결과가 없을 때 처리
    if not results:
        print(f"\n'{search_name}'님으로 등록된 정보가 없습니다.")
        return
        
    # 검색 결과가 있을 때: 실행 화면 양식 그대로 출력
    print("번호         성명                             전화                               주소")
    print("---------------------------------------------------------------")
    
    for idx, user in results:
        # ljust(숫자)는 글자 뒤에 공백을 채워 일정한 간격을 유지해 주는 함수입니다.
        p_idx = str(idx).ljust(12)
        p_name = user['name'].ljust(25)
        p_phone = user['phone'].ljust(33)
        p_address = user['address']
        
        print(f"{p_idx}{p_name}{p_phone}{p_address}")
        
def update_data():
    print("---------------------------수정기능-------------------------")
    # 화면과 똑같이 '수정할 성명을 입력하세요:' 문구로 변경
    search_name = input("수정할 성명을 입력하세요: ")
    
    is_found = False
    for user in phone_book_list:
        if user['name'] == search_name:
            is_found = True
            
            # 안내 문구 출력
            print("수정할 이름, 연락처,주소를 입력하세요")
            
            # 새로운 정보 입력받기 (화면의 콜론(:) 기호와 띄어쓰기 반영)
            new_name = input("새로운 이름: ")
            new_phone = input("새로운 전화번호: ")
            new_address = input("새로운 주소 : ")
            
            # 딕셔너리의 이름, 전화번호, 주소를 모두 새 값으로 변경!
            user['name'] = new_name
            user['phone'] = new_phone
            user['address'] = new_address
            
            print("연락처가 수정되었습니다")
            break  # 수정 완료 후 반복문 탈출
            
    if not is_found:
        print(f"\n'{search_name}'님으로 등록된 정보가 없어 수정을 진행할 수 없습니다.")
        
def delete_data():
    print("----------------------------삭제기능-------------------------")
    # 화면에 나온 '삭제할 성명을 입력하세요 : ' 형태를 그대로 적용
    search_name = input("삭제할 성명을 입력하세요 : ")
    
    is_found = False
    for user in phone_book_list:
        if user['name'] == search_name:
            is_found = True
            
            # 리스트에서 해당 유저 딕셔너리를 통째로 삭제합니다.
            phone_book_list.remove(user)
            
            print("정보가 삭제되었습니다")
            break  # 삭제 완료 후 반복문 탈출
            
    # 해당하는 이름이 없을 때 처리
    if not is_found:
        print("해당하는 정보가 없습니다")