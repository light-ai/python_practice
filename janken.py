import random

print("グー>>1, チョキ>>2 パー>>3だよ！数字で入力してね！")
print("ジャンケン…")
d = input()

l = random.randint(1,3)
print("ポン！！")
print("対戦相手>>", l)

if d == str(1):
  if l == 1:
    print("残念、引き分け！w")
  elif l == 2:
    print("おめでとう、勝ち！")
  else:
    print("お疲れ様、負けてますよww")
elif d == str(2):
  if l == 1:
    print("お疲れ様、負けてますよww")
  elif l == 2:
    print("残念、引き分け！w")
  else:
    print("おめでとう、勝ち！")
else:
  if l == 1:
    print("おめでとう、勝ち！")
  elif l == 2:
    print("お疲れ様、負けてますよww")
  else:
    print("残念、引き分け！w")          


