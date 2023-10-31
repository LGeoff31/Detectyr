# # Math IA: Estimating # of Gumballs | Nov 20+ 2020

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
points = [[11.83, 5.8], [12.92, 4.75], [14.07, 3.99],
          [15.46, 3.55], [16.9, 3.7], [18.17, 4.3], [19.3, 5.1]]
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
