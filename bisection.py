import math

def f(x):
    return x**6 - x - 1

def min_iters_to_beat_error_bound(a, b, e):
   return math.log((b-a)/e) / math.log(2)

def max_root_bisection(f, a, b, e):
    if f(a)*f(b) >= 0:
        return None

    iteration = 0
    # The following condition is not quite right -- min  =/= sufficient
    while iteration <= min_iters_to_beat_error_bound(a, b, e):
        midpoint = (a + b) / 2
        if f(midpoint)*f(b) < 0:
            a = midpoint
        else:
            b = midpoint
        iteration += 1

    return midpoint, iteration

def abs_error(true_root, estimate):
    return (estimate - true_root)

if __name__ == "__main__":
    error_bound = 0.001
    root, iterations = max_root_bisection(f, 1, 2, error_bound)
    print(f"x = {root} ; f(x) = {f(root)} ; in {iterations} iters.")
    true_root = 1.1347241384 # w.r.t current f(x), this is an approx. too
    print(f"For true root = {true_root}, absolute error = {abs_error(true_root, root)}")
