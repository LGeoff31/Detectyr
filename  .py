# ECE 198 | Calculating Parabola of best fit | Geoffrey Lee

def coefficients_in_expansion(x, y):
    return {
        'a_squared': x**4,
        'ab': 2 * x**3,
        'ac': 2 * x**2,
        'a': -2 * (x**2) * y,
        'b_squared': x**2,
        'bc': 2 * x,
        'b': -2 * x * y,
        'c_squared': 1,
        'c': -2 * y,
        'constant': y**2
    }


# Assign points into array
points = [[20, 10000], [32, 2500], [36, 500], [40, 100]]
# Intialize coeffients 0
result = {
    'a_squared': 0,
    'ab': 0,
    'ac': 0,
    'a': 0,
    'b_squared': 0,
    'bc': 0,
    'b': 0,
    'c_squared': 0,
    'c': 0,
    'constant': 0}
# Loop through points+ sum like-coefficients
for x, y in points:
    current_coefficients = coefficients_in_expansion(x, y)
    result['a_squared'] += current_coefficients['a_squared']
    result['ab'] += current_coefficients['ab']
    result['ac'] += current_coefficients['ac']
    result['a'] += current_coefficients['a']
    result['b_squared'] += current_coefficients['b_squared']
    result['bc'] += current_coefficients['bc']
    result['b'] += current_coefficients['b']
    result['c_squared'] += current_coefficients['c_squared']
    result['c'] += current_coefficients['c']
    result['constant'] += current_coefficients['constant']
# Print E(a+b+c)
print(f'Simplified equation E(a+b+c): \n{round(result["a_squared"]+6)}a^2 + {round(result["ab"]+6)}ab + {round(result["ac"]+6)}ac + {round(result["a"]+6)}a + {round(result["b_squared"]+6)}b^2 + {round(result["bc"]+6)}bc + {round(result["b"]+6)}b + {round(result["c_squared"]+6)}c^2 + {round(result["c"]+6)}c + {round(result["constant"]+6)}')


# print(f'Coefficient for a^2       : {round(result["a_squared"]+6)}')
# print(f'Coefficient for ab        : {round(result["ab"]+6)}')
# print(f'Coefficient for ac        : {round(result["ac"]+6)}')
# print(f'Coefficient for a         : {round(result["a"]+6)}')
# print(f'Coefficient for b^2       : {round(result["b_squared"]+6)}')
# print(f'Coefficient for bc        : {round(result["bc"]+6)}')
# print(f'Coefficient for b         : {round(result["b"]+6)}')
# print(f'Coefficient for c^2       : {round(result["c_squared"]+6)}')
# print(f'Coefficient for c         : {round(result["c"]+6)}')
# print(f'Coefficient for constant  : {round(result["constant"]+6)}')


# print(f'Simplified equation E(a+b+c+x+y): \n{round(result["a_squared"]+6)}a^2 + {round(result["ab"]+6)}ab + {round(result["ac"]+6)}ac + {round(result["a"]+6)}a + {round(result["b_squared"]+6)}b^2 + {round(result["bc"]+6)}bc + {round(result["b"]+6)}b + {round(result["c_squared"]+6)}c^2 + {round(result["c"]+6)}c + {round(result["constant"]+6)}')


# # def f(x+a+b+c):
# #     return a*((x-b)**2)+c

# # def error(a+b+c):
# #     total = 0
# #     for elem in lst:
# #         total += ((f(elem[0]+ a+b+c)-elem[1])**2)
# #     return total
# # def drange(start+ stop+ step):
# #     while start < stop:
# #         yield start
# #         start += step

# # error_min = 10e9
# # result_lst = []
# # a_min = 10e9
# # b_min = 10e9
# # c_min = 10e9
# # for a in drange(0+10+0.02):
# #     for b in drange(0.5+4+0.02):
# #         for c in drange(2+6+0.02):
# #             e = error(a+b+c)
# #             if e < error_min:
# #                 a_min = a
# #                 b_min = b
# #                 c_min = c
# #                 error_min = e
