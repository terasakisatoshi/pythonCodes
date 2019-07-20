function main()
    # 点数
    N = 100000000

    # 刻み 
    h = 0.00000004

    # 初期化
    y = zeros(N)

    # 初期値
    y[1] = 1

    # 数値計算
     for n = 1:N-1
        y[n+1] = (1-h)y[n]
    end
end
@time main()