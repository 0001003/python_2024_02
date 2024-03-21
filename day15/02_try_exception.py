    # 에러가 날 것 같은 곳을 try로 감싼다고 생각하면 된다.

try:
    num = int(input("숫자 입력 : "))
    print(f"결과:{10 / num}")
except ValueError:
    print("숫자를 넣으세요")
except ZeroDivisionError:
    print("0을 넣지 마세요")
except Exception:
    print("암튼 에러 발생")
else:
    print("에러 안 남")
finally:
    print("끝") # << 에러가 나든 안 나든, 이 문구는 무조건 실행 시켜라 라는 뜻 == finally

    # 얘네 일일히 다 쓸 거니?
    # 아니.. Exception 사용하면 한번에 해결 가능.
    # else 위에 Exception 써야 한다. 순서 때문에 (절차지향, 즉 논리 순서 때문에)


# num = int(input("숫자 입력 : "))
# print(f"결과:{10 / num}") << 얘를 실행하면 ValueError 에러가 뜬다. 그래서 위에 except 뒤에 저걸 넣어주는 게 문법.
# 0이 분모에 있으면 ZeroDivisionError가 뜨니까 except 안에 넣어주면 해결이 된다.


