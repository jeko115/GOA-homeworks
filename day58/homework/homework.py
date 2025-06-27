print("HELLO".lower())      
print("PyThOn".lower())     
print("123 ABC!".lower())   

print("hello".upper())     
print("PyThOn".upper())     
print("123 abc!".upper())   

print("hello world".capitalize())    
print("pYTHON".capitalize())          
print("123 abc".capitalize())        

print("hello world".find("world"))   
print("banana".find("na"))            
print("apple".find("z"))             

print(len("hello"))                  
print(len([1, 2, 3, 4]))              
print(len([]))                        

lst = [1, 2, 3]
lst.append(4)
print(lst)                           

lst.append([5, 6])
print(lst)                           

lst.append('a')
print(lst)                           

lst = [1, 2, 3]
lst.insert(1, 10)
print(lst)                          

lst.insert(0, 0)
print(lst)                          

lst.insert(len(lst), 99)
print(lst)                          

lst = [10, 20, 30, 40]
print(lst.pop())                  
print(lst)                        

print(lst.pop(1))                 
print(lst)                      

