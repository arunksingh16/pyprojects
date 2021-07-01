import sys
import os

def reading(filename):
  with open(filename, mode='rt', encoding='utf-8') as f:
    return[int(line.strip()) for line in f]
  
# you dont close in this
  
