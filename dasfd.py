namecard['박은수']='2022100081'
total_namecards = 0

def name_count():
    global total
    total = len(namecard)

while True:
    print("")
    print("명함 관리 ver 1.0")
    print("1. 명함 검색")
    print("2. 명함 추가")
    print("3. 명함 삭제")
    print("4. 전체 명함 출력")
    print("5. 파일에서 읽어오기")
    print("6. 파일에 저장하기")
    print("q. 프로그램 종료")

    num = input("선택하세요 : ")

    if num == '1': #명함 검색, 없는 명함이면 추가 y/n?
        print("1. 명함 검색")
        name = input("명함 입력 : ")
        if name in namecard:
            print(namecard[name])
        else:
            print("등록되지 않은 명함입니다.")
            new = input(" 명함을 등록하시겠습니까? ( y / n ) : ")
            if new.lower() == 'y':
                name = input("추가할 명함 입력 : ")
                number = input("학번 입력 : ")
                if name in namecard:
                    print("이미 등록된 명함입니다")
                else:
                    namecard[name] = number
                    name_count()
                    print("등록되었습니다")
            elif new.lower() == 'n':
                continue
            else:
                print("잘못된 입력입니다. 다시 시도하세요.")

    elif num == '2': 
        print("2. 명함 추가")
        name = input("추가할 명함 입력 : ")
        number = input("학번 입력 : ")
        if name in namecard:
            print("이미 등록된 명함입니다")
        else:
            namecard[name] = number
            name_count()
            print("등록되었습니다")

    elif num == '3':
        print("3. 명함 삭제")
        name = input("삭제할 명함 입력 : ")
        if name in namecard:
            del namecard[name]
            name_count() 
            print("삭제되었습니다")
        else:
            print("등록되지 않은 명함입니다.")

    elif num == '4': 
        print("4. 전체 명함 출력")

        for k, v in namecard.items():
            print("%-20s %-20s" % (k, v))
       
        print("총 %d 명" % total)

    elif num == '5':
        namecard.clear()
        print("5. 파일에서 읽어오기")
       
        ifile = open("namecard.txt", "r")
        for line in ifile:
            line = line.rstrip()
            word = line.split()
            namecard[word[0]] = word[1]
        ifile.close()
       name_count() 
        print("파일에서 읽어왔습니다")

    elif num == '6':
        print("6. 파일에 저장하기")
        ofile = open("namecard.txt", "w")  # 파일을 쓰기모드(w)로 열기
        for k, v in namecard.items():
            ofile.write("%s %s\n" % (k, v))  # 파일에 데이터 작성 - 파이썬 파일이 저장된 위치에 파일이 생성됨
        ofile.close()
       name_count()  
        print("파일 저장 완료")

    elif num == 'q':
        print("q. 프로그램 종료")
        break

    else:
        print("잘못된 선택입니다")
        
