"""
The module will contain:
all the functions needed for task 1 and 2
"""
def root_bisection(f, x1, x2, accuracy=1.0e-6, max_steps=1000, root_debug=False):
    """Return root of f(x) in bracketed by x1, x2 with specified accuracy.
    Assumes that f(x) changes sign once in the bracketed interval.
    Uses bisection root-finding algorithm.
    """
    iterations = []
    f1 = f(x1)
    f2 = f(x2)
    if f1 * f2 > 0.0:
        raise Exception("f(x1) * f(x2) > 0.0")
    x_mid = (x1 + x2) / 2.0
    f_mid = f(x_mid)
    dx = x2 - x1
    step = 0
    if root_debug:
        iterations = []
        root_print_header("Bisection Search", accuracy)
        root_print_step(step, x_mid, dx, f_mid)
        iterations.append([x_mid,f_mid])
    while abs(dx) > accuracy:
        if f_mid == 0.0:
            dx = 0.0
        else:
            if f1 * f_mid > 0:
                x1 = x_mid
                f1 = f_mid
            else:
                x2 = x_mid
                f2 = f_mid
            x_mid = (x1 + x2) / 2.0
            f_mid = f(x_mid)
            dx = x2 - x1
        step += 1
        if step > max_steps:
            warning = "Too many steps (" + repr(step) + ") in root_bisection"
            raise Exception(warning)
        if root_debug:
            root_print_step(step, x_mid, dx, f_mid)
            iterations.append([x_mid,f_mid])
    return x_mid,np.array(iterations)
def root_tangent(f, fp, x0, accuracy=1.0e-6, max_steps=20, root_debug=False):
    """Return root of f(x) with derivative fp = df(x)/dx
    given initial guess x0, with specified accuracy.
    Uses Newton-Raphson (tangent) root-finding algorithm.
    """
    iterations = []
    f0 = f(x0)
    fp0 = fp(x0)
    if fp0 == 0.0:
        raise Exception(" root_tangent df/dx = 0 algorithm fails")
    dx = - f0 / fp0
    step = 0
    if root_debug:
        root_print_header("Tangent Search", accuracy)
        root_print_step(step, x0, dx, f0)
        iterations.append([x0,f0])
    if f0 == 0.0:
        return x0
    while True:
        fp0 = fp(x0)
        if fp0 == 0.0:
            raise Exception(" root_tangent df/dx = 0 algorithm fails")
        dx = - f0 / fp0
        x0 += dx
        f0 = f(x0)
        if abs(dx) <= accuracy or f0 == 0.0:
            return x0
        step += 1
        if step > max_steps:
            root_max_steps("root_tangent", max_steps)
        if root_debug:
            root_print_step(step, x0, dx, f0)
            iterations.append([x0,f0])
    return x0
