def func(goma, koma, kyukkyu):
    print('goma=', goma)
    print('koma', koma)
    print('kyukkyu', kyukkyu)

mydic = dict(goma=1, koma=2, kyukkyu=3)

p = mydic.pop('goma')
print('p =', p)
print('current mydic =', mydic)

func(goma=-10, **mydic)
