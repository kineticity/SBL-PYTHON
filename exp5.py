class Dog:
    animal = 'dog'
    def __init__(self,breed,color):
        self.breed = breed
        self.color = color

Nala = Dog("Pug","Black")
Bubby = Dog("Golden Retriever","Blonde")

print("Details of Nala: ")
print("Nala is a ", Nala.animal)
print("Breed: ",Nala.breed)
print("Color: ",Nala.color)

print("\nDetails of Bubby: ")
print("Bubby is a ", Bubby.animal)
print("Breed: ",Bubby.breed)
print("Color: ",Bubby.color)
