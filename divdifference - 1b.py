def divided_differences(x, y):
    n = len(x)
    coeffs = y[:]
    
    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            coeffs[j] = (coeffs[j] - coeffs[j-1]) / (x[j] - x[j-i])
    
    return coeffs

def interpolate(x, y, val):
    coeffs = divided_differences(x, y)
    n = len(coeffs)
    result = coeffs[0]

    for i in range(1, n):
        term = coeffs[i]
        for j in range(i):
            term *= (val - x[j])
        result += term

    return result

x = [0.6, 0.7, 0.8, 1.0]
y = [-0.17694460, 0.01375227, 0.22363362, 0.65809197]

divided_diff_values = divided_differences(x, y)
print("Divided differences:", divided_diff_values)

val = 0.9
fx_value = interpolate(x, y, val)
print(f"The interpolated value at x = {val} is {fx_value}")
