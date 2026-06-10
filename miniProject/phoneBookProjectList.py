import phoneBookFuncList as pb

def main():
    while True:
        print("\n1.입력 2.출력 3.검색 4.수정 5.삭제 6.종료")
        choice = input("선택: ")
        
        if choice == '1': pb.insert_data()
        elif choice == '2': pb.print_all_data()
        elif choice == '3': pb.search_data()
        elif choice == '4': pb.update_data()
        elif choice == '5': pb.delete_data()
        elif choice == '6':
            print("\n프로그램을 종료합니다. 이용해 주셔서 감사합니다.")
            break
        else:
            print("\n[오류] 1번부터 6번 사이의 숫자를 입력해 주세요.")

if __name__ == "__main__":
    main()