
# phoneBookFunc 파일을 가져오면서 pb라는 별명으로 부릅니다.
import phoneBookFunc as pb

def main():
    while True:
        # 실행 화면에 나온 메뉴 스타일을 그대로 구현했습니다.
        print("\n1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료")
        choice = input("선택: ")
        
        if choice == '1':
            pb.insert_data()      # 입력 함수 호출
        elif choice == '2':
            pb.print_all_data()   # 출력 함수 호출
        elif choice == '3':
            pb.search_data()
        elif choice == '4':
           pb.update_data()
        elif choice == '5':
           pb.delete_data()
        elif choice == '6':
            print("\n프로그램을 종료합니다. 이용해 주셔서 감사합니다.")
            break                # while 무한루프를 탈출하여 프로그램 종료
        else:
            print("\n[오류] 잘못된 선택입니다. 1번부터 6번 사이의 숫자를 입력해 주세요.")

if __name__ == "__main__":
    main()