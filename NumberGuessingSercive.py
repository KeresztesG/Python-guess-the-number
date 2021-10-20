import random

def main():
  print("Hello, My Dear Friend! I randomly generated a number between 0 and 100000. Can you find out?\n")

  newNumber = random.randint(0,100000)
  guess = str(input())
  
  
if __name__ == "__main__":
    main()
