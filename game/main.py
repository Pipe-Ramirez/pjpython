import random
options = ('piedra', 'papel', 'tijera')

def chooisOptions():
  user_option = input('Escoja entre piedra, papel o tijera => ')
  user_option = user_option.lower()

  if not user_option in options:
    print('Esa opción no es válida')
    return None, None
#    continue

  computer_option = random.choice(options)
  print('User option =>', user_option)
  print('Computer option =>', computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, p1, p2):
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('Piedra gana a tijera')
      print('User ganó una partida!')
      p1 += 1
    else:
      print('Papel gana a piedra')
      print('Computer ganó una partida!')
      p2 += 1

  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('Papel gana a piedra')
      print('User ganó una partida!')
      p1 += 1

    else:
      print('Tijera gana a papel')
      print('Computer ganó una partida!')
      p2 += 1

  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('Tijera gana a papel')
      print('User ganó una partida!')
      p1 += 1

    else:
      print('Piedra gana a tijera')
      print('Computer ganó una partida!')
      p2 += 1
  print('*' * 15)
  print(f'User point => {p1} Computer point => {p2}')
  return p1, p2

def end_game(p1, p2):
  if p1 > p2:
    print('Fin de la partida!')
    print(f'El ganador es el usuario con {p1} puntos')
  else:
    print('Fin de la partida!')
    print(f'El ganador es el computador con {p2} puntos')
  
def run_game():
  p1 = 0
  p2 = 0
  while p1 < 2 and p2 < 2:
    user_option, computer_option = chooisOptions()
    p1, p2 = check_rules(user_option, computer_option, p1, p2)
    end_game(p1, p2)
  
run_game()