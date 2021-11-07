from PIL import Image
import colorama
from colorama import Fore, Back, Style 
import numpy as np
import random

##===========================================================================
'''PIXELATION'''
##===========================================================================
def PIXELATION(file_name):
  line_word, list_all, stroka, line_lenght = [], [], [], []
  file = open(file_name, 'rb')
  while (byte := file.read(1)): ##read file.txt
    line_word.append(byte[0])
  file.close
  lenf = len(line_word)
  if len(line_word) % 3 != 0:
    while len(line_word) % 3 != 0:
      line_word.append(random.randrange(1, 255))
  leght_s = len(line_word) // 3
  while lenf > 0:
    line_lenght.append(((lenf % 256), 0, 0))
    lenf = lenf // 256
  for k in range(0, (leght_s - len(line_lenght))):
    line_lenght.append((0, random.randrange(1, 255), random.randrange(1, 255)))  
  for i in range(leght_s):
    tiple = (line_word[i*3], line_word[i*3+1], line_word[i*3+2])
    stroka.append(tiple)
  list_all.append(stroka)
  list_all.append(line_lenght)
  array = np.array(list_all, dtype=np.uint8)
  new_image = Image.fromarray(array)
  return new_image.save('new' + str(random.randrange(1, 10000000)) + '.png') 
##===========================================================================
'''UNPIXELATION'''
##===========================================================================
def UNPIXELATION(file_name):
  im = Image.open(file_name, 'r') 
  lenght, width = im.size 
  pixel_values = list(im.getdata()) 
  im.close()
  massive, massive_lenghttrue, init, massive_tr, massive1 = [], [], 0, [], []
  for l_pixel in range(lenght):
    massive.append(pixel_values[l_pixel])
  for i in range(len(massive)):
    massive1.append(massive[i][0])
    massive1.append(massive[i][1])
    massive1.append(massive[i][2])  
  for j in range(lenght*2):
    if pixel_values[j][1] == 0 and pixel_values[j][2] == 0 and pixel_values[j][0] != 0:
          massive_lenghttrue.append(pixel_values[j][0])
  for i in range(len(massive_lenghttrue)): 
      init += massive_lenghttrue[i] * (256 ** i)
  for i in range(init):
    massive_tr.append(massive1[i])
  file_out = open('result' + str(random.randrange(1, 10000000)) + '.txt', 'wb')
  MassiveByte = bytearray(massive_tr)
  file_out.write(MassiveByte)  
  file_out.close()  
##===========================================================================
colorama.init()
print("\033[3;32;40m                      _        _                                             \033[0;32;40m")
print("\033[3;32;40m                     | |      | |                                            \033[0;32;40m")
print("\033[3;32;40m  _ __ ___   __ _  __| | ___  | |__  _   _   _ __ ___   ___  _ __ ___ _ __   \033[0;32;40m")
print("\033[3;32;40m | '_ ` _ \ / _` |/ _` |/ _ \ | '_ \| | | | | '_ ` _ \ / _ \| '__/ _ \ '_ \  \033[0;32;40m")
print("\033[3;32;40m | | | | | | (_| | (_| |  __/ | |_) | |_| | | | | | | | (_) | | |  __/ | | | \033[0;32;40m")
print("\033[3;32;40m |_| |_| |_|\__,_|\__,_|\___| |_.__/ \__, | |_| |_| |_|\___/|_|  \___|_| |_| \033[0;32;40m")
print("\033[3;32;40m                                      __/ |                                  \033[0;32;40m")
print("\033[3;32;40m                                     |___/                                   \033[0;32;40m")
print('\033[5;37;40m--|{HEX CODER V3}|--\033[0;37;40m')
print('\033[5;37;40mchoose the type of script\033[0;37;40m')
print('\033[5;37;40m1 -- encode txt to png\033[0;37;40m')
print('\033[5;37;40m2 -- decode png to txt\033[0;37;40m')
print('|{-------------------------------------WARNING:this script works with all symbols(finaly)----------------------------------------------------------------------------------------}|')
print('|if you have any problems or questions, then write here (Herman Garsky#2574). When publishing a question / problem, describe in detail with attaching screenshots. good using :-) |')
while True:
  choose = int(input('num type: '))
  if choose == 1:
    print('|write the things you are interested in in the txt file and put its address here|>>> ')
    ff = input()
    print(PIXELATION(ff))
  elif choose == 2:
    print('Throw in the address of a picture like "new(numbers).png" along with its above name')
    ff = input()
    print(UNPIXELATION(ff))