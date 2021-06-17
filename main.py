
import art
#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Divide
def divide(n1, n2):
  return n1/n2

#Multiply
def multiply(n1, n2):
  return n1 * n2


operations = {
  "+" : add,
  "-" : subtract,
  "/" : divide,
  "*" : multiply,
}


def calculator():
    print(art.logo)
    done = False

    num1 = float(input("What is the first number? "))
    for operand in operations:
        print(operand)
    answer = num1    
    while done == False:
        operation_symbol = input("Pick an operation. ") 
        num2 = float(input("What is the next number? "))

        result = operations[operation_symbol](answer, num2)
        
        print(f"{answer} {operation_symbol} {num2} = {result}")
        carry_on = input((f"Type 'y' to continue calculating with {result}, or type 'n' to exit: "))
        answer = result
        if carry_on == "n":
          done = True
          print("---------------------------------------------------------------------")
          calculator()  

calculator()