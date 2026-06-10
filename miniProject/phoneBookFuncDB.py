import pymysql

# [공통] DB 연결을 맺어주는 자판기 함수
def get_connection():
    return pymysql.connect(
        host='localhost', user='sample_user', password='1234', database='sample_db',
        charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor
    )

# [시스템] 테이블이 없을 때 자동 생성해 주는 함수
def create_table_if_not_exists():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
            CREATE TABLE IF NOT EXISTS phonebooks (
                num INT NOT NULL AUTO_INCREMENT,
                name VARCHAR(30) NOT NULL,
                phone VARCHAR(20) NOT NULL,
                address VARCHAR(100) NOT NULL,
                PRIMARY KEY (num)
            );
            """
            cursor.execute(sql)
        conn.commit()
        print("[시스템] phonebooks 테이블이 준비되었습니다.")
    except Exception as e:
        print(f"[시스템] 테이블 생성 오류: {e}")
    finally:
        conn.close()

def insert_data():
    print("-------------------------입력기능----------------------")
    name, phone, address = input("성명>>> "), input("전화>>> "), input("주소>>> ")
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO phonebooks (name, phone, address) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, phone, address))
        conn.commit()
        print("주소 입력 완료!")
    except Exception as e: print(f"오류: {e}")
    finally: conn.close()

def print_all_data():
    print("-------------------------출력기능----------------------")
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT num, name, phone, address FROM phonebooks")
            results = cursor.fetchall()
            if not results:
                print("등록된 전화번호가 없습니다.")
                return
            print("번호         성명                             전화                               주소")
            print("---------------------------------------------------------------")
            for row in results:
                print(f"{str(row['num']).ljust(12)}{row['name'].ljust(25)}{row['phone'].ljust(35)}{row['address']}")
    except Exception as e: print(f"오류: {e}")
    finally: conn.close()

def search_data():
    print("-------------------------- 검색기능--------------------------")
    search_name = input("이름을 입력해주세요\n이름: ")
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT num, name, phone, address FROM phonebooks WHERE name = %s"
            cursor.execute(sql, (search_name,))
            results = cursor.fetchall()
            if not results:
                print(f"'{search_name}'님으로 등록된 정보가 없습니다.")
                return
            print("번호         성명                             전화                               주소")
            print("---------------------------------------------------------------")
            for row in results:
                print(f"{str(row['num']).ljust(12)}{row['name'].ljust(25)}{row['phone'].ljust(35)}{row['address']}")
    except Exception as e: print(f"오류: {e}")
    finally: conn.close()

def update_data():
    print("---------------------------수정기능-------------------------")
    search_name = input("수정할 성명을 입력하세요: ")
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM phonebooks WHERE name = %s", (search_name,))
            if not cursor.fetchone():
                print(f"'{search_name}'님으로 등록된 정보가 없어 수정을 진행할 수 없습니다.")
                return
            print("수정할 이름, 연락처, 주소를 입력하세요")
            new_name, new_phone, new_address = input("새로운 이름: "), input("새로운 전화번호: "), input("새로운 주소 : ")
            sql = "UPDATE phonebooks SET name=%s, phone=%s, address=%s WHERE name=%s"
            cursor.execute(sql, (new_name, new_phone, new_address, search_name))
        conn.commit()
        print("연락처가 수정되었습니다")
    except Exception as e: print(f"오류: {e}")
    finally: conn.close()

def delete_data():
    print("----------------------------삭제기능-------------------------")
    search_name = input("삭제할 성명을 입력하세요 : ")
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM phonebooks WHERE name = %s", (search_name,))
            if not cursor.fetchone():
                print("해당하는 정보가 없습니다")
                return
            cursor.execute("DELETE FROM phonebooks WHERE name = %s", (search_name,))
        conn.commit()
        print("정보가 삭제되었습니다")
    except Exception as e: print(f"오류: {e}")
    finally: conn.close()