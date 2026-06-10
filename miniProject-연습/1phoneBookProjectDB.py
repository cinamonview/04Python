import pymysql

# =========================================================================
# [공통 기능] MariaDB 연결을 새로 만들어주는 자판기 함수
# =========================================================================
def get_connection():
    return pymysql.connect(
        host='localhost',
        user='sample_user',          # 본인의 MariaDB 계정명 (예: root)
        password='1234',      # 本인의 MariaDB 비밀번호 (예: root)
        database='sample_db',         # 본인의 데이터베이스 이름
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor # 결과를 딕셔너리 형태로 받아오기 위함
    )

# =========================================================================
# [시스템 기능] 프로그램 시작 시 테이블이 없으면 자동으로 생성해주는 함수
# =========================================================================
def create_table_if_not_exists():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # IF NOT EXISTS를 붙여서 이미 테이블이 있으면 에러 없이 넘어갑니다.
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
        print(f"[시스템] 테이블 생성 중 오류 발생: {e}")
    finally:
        conn.close()

# =========================================================================
# [1번 기능] 데이터 입력 (INSERT)
# =========================================================================
def insert_data():
    print("-------------------------입력기능----------------------")
    name = input("성명>>> ")
    phone = input("전화>>> ")
    address = input("주소>>> ")
    
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # 일련번호(num)는 auto_increment이므로 생략하고 데이터를 넣습니다.
            sql = "INSERT INTO phonebooks (name, phone, address) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, phone, address))
        conn.commit() # INSERT 후에는 반드시 commit을 해야 DB에 영구 저장됩니다.
        print("주소 입력 완료!")
    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        conn.close()

# =========================================================================
# [2번 기능] 전체 데이터 출력 (SELECT)
# =========================================================================
def print_all_data():
    print("-------------------------출력기능----------------------")
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # 테이블의 모든 데이터를 조회합니다.
            sql = "SELECT num, name, phone, address FROM phonebooks"
            cursor.execute(sql)
            results = cursor.fetchall() # 모든 행(Row)을 가져옵니다.
            
            if not results:
                print("등록된 전화번호가 없습니다.")
                return
                
            # 정렬 서식에 맞춰서 출력
            print("번호         성명                             전화                               주소")
            print("---------------------------------------------------------------")
            for row in results:
                p_num = str(row['num']).ljust(12)
                p_name = row['name'].ljust(25)
                p_phone = row['phone'].ljust(35)
                p_address = row['address']
                print(f"{p_num}{p_name}{p_phone}{p_address}")
    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        conn.close()

# =========================================================================
# [3번 기능] 특정 이름 검색 (SELECT ... WHERE)
# =========================================================================
def search_data():
    print("-------------------------- 검색기능--------------------------")
    print("이름을 입력해주세요")
    search_name = input("이름: ")
    
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # WHERE 절을 사용하여 입력한 성명과 정확히 일치하는 데이터만 가져옵니다.
            sql = "SELECT num, name, phone, address FROM phonebooks WHERE name = %s"
            cursor.execute(sql, (search_name,))
            results = cursor.fetchall()
            
            if not results:
                print(f"'{search_name}'님으로 등록된 정보가 없습니다.")
                return
                
            print("번호         성명                             전화                               주소")
            print("---------------------------------------------------------------")
            for row in results:
                p_num = str(row['num']).ljust(12)
                p_name = row['name'].ljust(25)
                p_phone = row['phone'].ljust(35)
                p_address = row['address']
                print(f"{p_num}{p_name}{p_phone}{p_address}")
    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        conn.close()

# =========================================================================
# [4번 기능] 데이터 수정 (UPDATE)
# =========================================================================
def update_data():
    print("---------------------------수정기능-------------------------")
    search_name = input("수정할 성명을 입력하세요: ")
    
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # 수정하기 전에 실제로 해당 성명이 존재하는지 먼저 확인합니다.
            sql_check = "SELECT * FROM phonebooks WHERE name = %s"
            cursor.execute(sql_check, (search_name,))
            if not cursor.fetchone():
                print(f"'{search_name}'님으로 등록된 정보가 없어 수정을 진행할 수 없습니다.")
                return
            
            # 존재한다면 새로운 수정을 위한 입력 창을 띄웁니다.
            print("수정할 이름, 연락처, 주소를 입력하세요")
            new_name = input("새로운 이름: ")
            new_phone = input("새로운 전화번호: ")
            new_address = input("새로운 주소 : ")
            
            # 해당 성명을 찾아 새로운 값들로 UPDATE 합니다.
            sql_update = "UPDATE phonebooks SET name=%s, phone=%s, address=%s WHERE name=%s"
            cursor.execute(sql_update, (new_name, new_phone, new_address, search_name))
        conn.commit() # 수정 사항을 DB에 영구 반영합니다.
        print("연락처가 수정되었습니다")
    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        conn.close()

# =========================================================================
# [5번 기능] 데이터 삭제 (DELETE)
# =========================================================================
def delete_data():
    print("----------------------------삭제기능-------------------------")
    search_name = input("삭제할 성명을 입력하세요 : ")
    
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # 삭제하기 전에 실제로 해당 성명이 존재하는지 먼저 확인합니다.
            sql_check = "SELECT * FROM phonebooks WHERE name = %s"
            cursor.execute(sql_check, (search_name,))
            if not cursor.fetchone():
                print("해당하는 정보가 없습니다")
                return
            
            # 해당 성명을 가진 행을 삭제(DELETE) 합니다.
            sql_delete = "DELETE FROM phonebooks WHERE name = %s"
            cursor.execute(sql_delete, (search_name,))
        conn.commit() # 삭제 사항을 DB에 영구 반영합니다.
        print("정보가 삭제되었습니다")
    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        conn.close()