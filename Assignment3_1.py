# Addition N numbers from user and return addition of that N numbers

def Addition(LIST):
  sum = 0
  for i in range(len(LIST)):
   sum = sum + LIST[i]
  return sum
  
def main():
   arr = []
   print("Enter the number of elements")
   size = int(input())
   
   for i in range(size):
     print("Enter the elements : ",i + 1)
     value = int(input())
     arr.append(value)

   print("Accepted data is :",arr)	 

   ret  = Addition(arr)

   print("Addition of all elements is :",ret)
  
if __name__ == "__main__":
  main()
