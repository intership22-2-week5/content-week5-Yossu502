DATA = [
    {
        'name': 'Carlos',
        'age': 72,
        'organization': 'Ciancoders',
        'position': 'Technical Leader',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 75,
        'organization': 'Ciancoders',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 76,
        'organization': 'Ciancoders',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Ciancoders',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'internship',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

# def pythondevs():
#   listFinal = [data for data in DATA if data['language'] == 'python']
#   return listFinal

def run():
    # Comprehensions solutions
    # 1. obtener todos los desarrolladores de python
  # print('Desarrolladores de python')
  # list = pythondevs()
  # for item in list:
  #   print(item)
    # 2. obtener todos los desarrolladores de python que tienen una edad mayor a 20
  # print('Desarrolladores de python con edad mayor a 20')
  # list = [data for data in list if data['age'] > 20]
  # list = pythondevs()
  # for item in list:
  #   print(item)
    # 3. obtener todos los trabajadores de ciancoders 
  print('Desarrolladores de CianCoders')
  listCianCoder = filter(lambda x: x['organization'] == 'Ciancoders', DATA)
  for item in listCianCoder:
    print(item)
    # 4. obtener todos los trabajadores de ciancoders que tienen una edad mayor a 30
  # print('Desarrolladores de Ciancoders con edad mayor a 30')
  # listFinal = [data for data in listFinal if data['age'] > 30]
  # for item in listFinal:
  #   print(item)
    # 5. obtener todos los trabajadores de mayores de 18 años
  # print('Trabajadores mayores a 18 años')
  # list18 = [data for data in DATA if data['age'] > 18]
  # for item in list18:
  #   print(item)
    # 6. obtener todos los trabajadores de mayores a 70 años
  print('Trabajadores mayores a 70 años')
  list70 = list(filter(lambda s: s['age'] > 70, DATA))
  print(list70)


if __name__ == '__main__':
    run()