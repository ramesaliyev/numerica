import numerica as n

fn1 = n.fnx(degree=2, coefficients=[1, -6, 5], baseExp=1) # (x^2 - 6x + 5)^1
fn2 = n.fnx(degree=3, coefficients=[1, -6.5, 13.5, -9], baseExp=1) # (1x^3 - 6.5x^2 + 13.5x - 9)^1