# 長針は60minで2pi回転する
# 短針は12h = 720min で2pi回転する

N, M = map(int, input().split(" "))

theta_m = 360 * M / 60
theta_n = 360 * ((N % 12) * 60 + M) / 720

print(min(abs(theta_n - theta_m), 360 - abs(theta_n - theta_m)))

# AC 12