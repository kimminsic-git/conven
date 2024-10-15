while True:
    print('=====편의점 재고 관리 프로그램=====')
    print('1.재고_등록')
    print('2.재품_판매')
    print('3.재고_조회')
    print('0.프로그램_종료')

    choice=input("메뉴를 선택하세요:")
    
    if choice=='0':  
        print('프로그램을 종료합니다.')
        break
    
    elif choice=='1':
        print('재고 등록 기능을 구현합니다.')
        
    elif choice=='2':
        print('제품 판매 기능을 구현합니다.')
        
    elif choice=='3':
        print('재고 조회 기능을 구현합니다.')
    
    else:
        print('잘못된 입력입니다. 다시 입력해주세요.')