"""
OUTPUT:

Country code for India - 0091
Country code for Japan - Not Found

"""




country_code = {
    'India' : '0091',
    'Australia' : '0025',
    'Nepal' : '00977'
}

print(country_code['India'])
print(country_code.get('Japan', "not found"))