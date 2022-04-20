from PIL import Image

name = input("type your name:  ")
print("Welcome," ,name, "to this adventure")

image1 = Image.open('ship.jpeg')
image1.show('ship.jpeg')


image2 = Image.open('spaceshipcrash.jpeg')
image2.show('spaceshipcrash.jpeg')


answer = input(
    "You are on a space ship, and it has crashed. Somehow you have survived, do you want to explore the ship for survivors or move and seek shelter ").lower()
  

if answer == "explore for survivors":
    answer = input("You come across an injured person who is on the brink of death. But you are low on your oxygen level do you want leave them behind or try to save them. Type Leave them behind or Save them ")

    if answer == "leave them Behind":
        print= ("You leave them behind which they eventually suffoicate to death but you reach to a secure spot with stable oxygen")
    elif answer == "save them":
        print = ("You find a some duct tape to seal any leaks of oxygen that injured survivor has and you drag them to safety just in time, so they survive")
    else:
        print("not a valid option. You Died")    
elif answer == "seek shelter":
    answer = input("You were able to find shelter, but you find two more people who is fighting for supplies to survive. Do you want them to get along anf form a team or secretly take supplies for you self? Type help them get a long or scretly take them")

    if answer == "help them get a long":
        print("You manage to get them to be calm and they aggreed to work together as a team")
        image3 = Image.open('2pplworking.jpeg')
        image3.show('2pplworking.jpeg')
    elif answer == " secretly take supples":
        print("you take the supplies and run out of the safety valve but they are chasing you but their oxygen dies before they can catch you")
        image4 = Image.open('twoppplfighting.jpeg')
        image4.show('twopplfighting.jpeg')
    else:
         print("Not a valid option. You died")
else:
    print("Not a valid option. You died")

print('you still die not matter what GAME OVER')