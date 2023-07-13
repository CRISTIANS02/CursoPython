lista=[]
indice=0
palabra= ''
while len(lista)<5:
   dato =input('ingrese el dato: ')
   lista.append(dato)
for texto in range(0, len(lista)): 
    if lista[texto]=='disco':
        palabra=lista[texto]
        indice=texto
print(f'''
el disco se encuentra en el indice,{indice} y el texto es: {palabra} ''')    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# # Prompt the user for a list of 5 elements

# elements = []
# for i in range(5):
#     element = input("Enter an element: ")
#     elements.append(element)
#  # Check if the word "disco" is present in the list
# if "disco" in elements:
#     # Find the word, its location, and its positive index
#     for index, word in enumerate(elements):
#         if word == "disco":
#             print("Word:", word)
#             print("Location:", index)
#             print("Positive Index:", index + 1)
# else:
#     print("The word 'disco' is not present in the list.")