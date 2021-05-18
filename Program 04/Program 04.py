# Once a variable is defined in the 'def __init__' method, in this case the variable is 'self.candyList'. It can be used anywhere in the class it is defined in.
# The variable may also be used in other classes if it is the child of a super class.

class Stack:
    def __init__(self):
        self.candyList = [] #creates an empty STACK list called "candyList"

    def isEmpty(self):
        return self.candyList == [] #return an empty STACK list

    def push(self, x):
        self.candyList.append(x) #add an item to the STACK list

    def pop(self):
        return self.items.pop() #remove an item from the STACK list

    def peek(self):
        return self.candyList[len(self.items) - 1] # Looks at the most recent item added

    def size(self):
        return len(self.candyList) #Prints the length STACK list
    

def main():
  pez_candy_list = ['Red', 'Yellow', 'Blue', 'Orange', 'Purple', 'Red', 'Red', 'Orange',
  'Blue', 'Blue', 'Orange', 'Purple', 'Purple', 'Yellow', 'Yellow', 'Yellow', 'Purple',
  'Orange', 'Blue', 'Blue', 'Blue', 'Blue', 'Purple', 'Purple', 'Purple', 'Purple',
  'Orange', 'Orange', 'Orange', 'Orange']
  s = Stack() #Creates 's' as an object of the class 'Stack', allows the use of the class in 'main'

  for item in pez_candy_list: #For every item in the pez_candy_list
    if item == 'Yellow': #If the item is yellow
      pass #Don't add it to the STACK list
    else:#If any other color add it to the STACK list
      s.push(item)
  
  print(pez_candy_list)#Prints original list
  print()
  print('There are', len(pez_candy_list), 'Pez candies before Phil eats the yellow ones.')
  print()
  print(s.candyList)#Prints list without Yellow color
  print()
  print('Now there are only', s.size(), 'Pez candies left.')
  
main()
