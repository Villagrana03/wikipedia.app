# from itertools import product

# password = "8742"
# digits = 'ABCDEFG'

# num = 4

# def repeatCount(num):
#         if len(combo) == num:
#                 num = num+1

# combinations = product(digits, repeat=repeatCount(num))



# for combo in combinations:
#         #example = ''.join(combo)
#         print(''.join(combo))
        



# array = ["a", "b", "b", "a", "b"]
# counts = {}

# def main():
#     for v in array:
#         if v in counts:
#                 counts[v] += 1
#         else:
#                 counts[v] = 1

#     values = list(counts.values())
#     for result in values:
#         if result == 3:
#                 return True
#         return False

# print()




# import string as s

# #print(dir(s))

# base =s.ascii_letters

# conversionInicial = base[2:] #recortar de la segunda poscicion al ultimo
# consersionFinal = base[:2] #Recortar hasta el indice 1, 2 no se incluye
# conversion = conversionInicial + consersionFinal
# print(consersionFinal)


# answer = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}"
# finalAnswer = ""

# for value in answer:
#     if value not in conversion:
#         finalAnswer += value
#         #print(finalAnswer)
#     else:
#         index = conversion.index(value)
#         d = base[index]
#         finalAnswer += d
#         #print(index, end = " ")

# #print(finalAnswer)

# import math 

# result = math.e != math.pow(2,4)
# print(int(result))



# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         # Handle POST request (form submission)
#         name = request.form['name']
#         return f"Hello, {name}!"
#     return '''
#         <form method="POST">
#             Name: <input type="text" name="name">
#             <button type="submit">Submit</button>
#         </form>
#     '''

# if __name__ == "__main__":
#     app.run(debug=True)



#SQL Alchemy

