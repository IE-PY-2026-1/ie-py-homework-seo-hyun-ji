# 파일이름 : Paw-Tune: 반려동물 가계부 & 힐링 가이드
# 작 성 자 : 서현지
user_name = str(input("집사 이름을 입력하세요: "))
pet_name = str(input("반려동물 이름을 입력하세요: "))
budget = int(input("이번 달 예산을 입력하세요(원): "))
weight = float(input("반려동물의 몸무게를 입력하세요(kg): "))
target_walk = int(input("목표 산책 시간을 입력하세요(분): "))

print("\n" + "="*40)
print(f"[Paw-Tune] {user_name} 집사님, 환영합니다!")
print(f"현재 {pet_name}의 몸무게는 {weight}kg입니다.")
print(f"이번 달 예산: {budget}원")
print(f"오늘의 목표 산책 시간: {target_walk}분")
print("="*45)
print("반려동물과의 건강한 밸런스 측정을 시작합니다!\n")

expenses = []
itens = []

print(f"{pet_name}를 위해 사용한 최근 지출 내역 3개를 입력해주세요.")

for i in range(3):
    item = input(f"{i+1}번째 지출 항목(예: 간식, 장난감): ")
    price = int(input(f"{item}의 가격을 입력하세요: "))
    items.append(item)
    expenses.append(price)

total_spent = sum(expenses)
expensive_price = max(expenses)

expenseive_index = expenses.index(expensive_price)
expensive_item = items[expensive_index]

count = len(items)

print("\n" + "-"*45)
print(f"{pet_name} 지출 분석 리포트")
print(f"기록된 항목 수: {count}개")
print(f"총 지출 금액: {total_spent}원 / 남은 예산: {budget - total_spent}원")
print(f"가장 큰 지출: '{expensive_item}' 항목({expensive_price}원)")
print("-"*45)

remaining_budget = budget
remaining_budget -= total_spent

print(f"\n {user_name} 집사님의 최종 성적표를 계산 중입니다...")

if total_spent > budget:
    grade = "F (지갑 파산)"
    message = "예산을 초과했어요! 다음 달은 아껴 써야 해요."
elif total_spent == budget:
    grade = "B (딱 맞춤)"
    message = "계획한 예산을 모두 사용하셨네요!"
  
else:
    
    if remaining_budget >= (budget * 0.2) and total_spent > 0:
        grade = "S (갓-집사)"
        message = "지출도 알뜰하고 반려동물도 행복한 완벽한 밸런스입니다!"
    else:
        grade = "A (훌륭한 집사)"
        message = "안정적으로 예산을 관리하고 계시네요."

print("-" * 45)
print(f"결과: [{grade}]")
print(f"남은 예산: {remaining_budget}원")
print(f"평가: {message}")
print("-" * 45)

if total_spent == 0:
    print("아직 지출 내역이 없네요. 활동을 기록해 보세요!")
  
