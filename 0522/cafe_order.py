menu = {
    "아메리카노": 3000,
    "카페라떼": 3500,
    "바닐라라떼": 4500,
    "아이스티": 2500,
    "딸기라떼": 5000
}

basket = {}

print("카페에 오신 걸 환영합니다!")

while True:
    print("/n--- 메뉴판---")
    for name, price in menu.items():
        print(f" {name}: {price}원")
    print("-----------------")

    choice = input("주문할 메뉴 이름을 입력하세요 (종료하려면 '종료' 입력): ")

    if choice == "종료":
        break
    if choice in menu:
        count = input(f"{choice}를 몇 잔 주문하시겠습니까? (숫자만 입력): ")

        count = int(count)

        if choice in basket:
            basket[choice] += count

        else:
            basket[choice] = count

        print(f"장바구니에 {choice} {count}잔이 담겼습니다.")
    else:
        print("메뉴판에 없는 메뉴입니다. 이름을 다시 확인해주세요.")

    print("="*20)
    print("주문 영수증")
    print("="*20)

    total_price = 0

    for name, count in basket.items():
        item_price = menu[name] * count
        total_price += item_price
        print(f"- {name} {count}잔 : {item_price}원")

    print("-" * 20)
    print(f"총 결제 금액: {total_price}원")
    print("="*20)
    print("감사합니다! 준비해 드릴게요.")