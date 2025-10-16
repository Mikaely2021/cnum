n = max(1, n0)
prev = None
whille n <= n_max:
    y = math.exp(n * math.log1p(x / n))
    if prev is not None:
        if abs(y - prev) < tol:
            break
    prev = y
    n *= 2


        #inicio do código
    ativiadade 4
    xs = [-20 + 40 * i / 199 for i in range(200)]
    errs = [abs(cos_series(x)[0] - math.cos(x)) for x in xs]
    print(f"xs={xs[:10]}\nerrs={errs[:10]}...")
