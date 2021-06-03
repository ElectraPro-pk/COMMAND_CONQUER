import json
import os.path
from os import path, system, name
import time as t

game_data = {}

EAST = ["Forest", "Mountains", "Sea"]
WEST = ["Base", "Forest", "Barracks"]
NORTH = ["Sea", "Forest", "Barracks"]
SOUTH = ["Barracks", "Resources", "Mountains"]

enemy = {
  "easy":{
    "barracks":1,
    "soldiers":20,
    "elite":5,
    "tanks":5,
    "oil mine": True,
    "gold mine":False,
    "airport":False,
    "defence system":False
  },
  "medium":{
     "barracks":1,
    "soldiers":20,
    "elite":10,
    "tanks":10,
    "oil mine": True,
    "gold mine":False,
    "airport":2,
    "defence system":True
  },
  "hard":{
     "barracks":1,
    "soldiers":20,
    "elite":10,
    "tanks":15,
    "oil mine": True,
    "gold mine":True,
    "airport":3,
    "defence system":True
  }
}



def checkGameStatus():
    return path.exists("./config.json")


def init_game():
    global game_data
    print(
        "Welcome commander I was informed that you’ll be in charge of the new base since your information where confidential how would you like me to call you."
    )
    tmp = {
        "name":
        input("Your Name :"),
        "experience":
        input(
            "Commander can you tell me more about your experience:\nYoung Commander (easy) \nAdvanced Commander (Medium)\nExpert Commander (Hard)"
        )
    }
    game_data['player'] = tmp
    print(
        "Commander " + tmp['name'] +
        " building your fleet while defending your main base from any attacks most be your first priority If the main base is lost, we'll lose the fight"
    )

    game_data['status'] = {
        "resources": {
            "soldier": 5,
            "elite": 0,
            "tanks": 0,
            "airplanes": 0,
            "barracks": 0,
            "money": 10000,
            "currency": "€"
        },
        "damages": {
            "barracks": 0,
            "tanks": 0,
            "airport": 0,
            "defence system": 0
        }
    }
    game_data['build'] = {
        "barracks": True,
        "building": False,
        "tank factory": False,
        "airport": False,
        "defence system": True,
        "main base": True
    }

    with open('config.json', 'w') as outfile:
        json.dump(game_data, outfile, indent=4)


def getAvailibilty(s):
    if s:
        return "Available"
    else:
        return "Not Available"


def showStatus():
    global game_data
    for k in game_data['status']:
        print(k)
        for i in game_data['status'][k]:
            print("\t\t", i, "(", game_data['status'][k][i], ")")
    for k in game_data['build']:
        print("", k, "(", getAvailibilty(game_data['build'][k]), ")")


def clear():
    # for windows
    if name == 'nt':
        _ = system("pause")
        _ = system('cls')



    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def addResource(key, value):
    global game_data
    game_data['status']['resources'][key] += value


def buyTankFactory():
    global game_data
    available = game_data['build']['tank factory']
    if available:
        if game_data['status']['damages']['tanks'] > 75:
            print(
                "Tank Factory is Damaged You should repair\nreparing cost(500€) for 10% repair"
            )
            re = input("(y/n)")
            if re == "y" or re == "Y":
                print("Repairing Tanks Factory")
                prev = game_data['status']['damages']['tanks']
                game_data['status']['damages']['tanks'] -= 10
                t.sleep(2)
                print("Repaired Tank Factory from ", prev, "% to ",
                      game_data['status']['damages']['tanks'], "%")
        else:
            print("You can Buy Tanks\n 1 Tank costs (1000€)")
            opt = int(input("How much you want to buy tanks "))
            cost = opt * 1000
            bal = game_data['status']['resources']['money']
            if cost <= bal:
                print("Costs : ", cost, "\nYour Balance : ", bal)
                print("Buying ", opt, " Tanks")
                deductMoney(cost)
                t.sleep(2)
                addResource("tanks", opt)
                print(opt, "Tanks are added to your force")
            else:
                print("You Dont Have enough Money")
    else:
        print("You cannot Buy because Tank Factory is not available yet")


def buyAirport():
    global game_data
    available = game_data['build']['airport']
    if available:
        if game_data['status']['damages']['airport'] > 75:
            print(
                "Airport is Damaged You should repair\nreparing cost(500€) for 10% repair"
            )
            re = input("(y/n)")
            if re == "y" or re == "Y":
                print("Repairing Airport")
                prev = game_data['status']['damages']['airport']
                game_data['status']['damages']['airport'] -= 10
                t.sleep(2)
                print("Repaired Airport from ", prev, "% to ",
                      game_data['status']['damages']['airport'], "%")
        else:
            print("You can Buy Airplanes\n 1 Airplane costs (2000€)")
            opt = int(input("How much you want to buy airplanes"))
            cost = opt * 2000
            bal = game_data['status']['resources']['money']
            if cost <= bal:
                print("Costs : ", cost, "\nYour Balance : ", bal)
                print("Buying ", opt, " Airplanes")
                deductMoney(cost)
                t.sleep(2)
                deductMoney(500)
                addResource("airplanes", opt)
                print(opt, "Airplanes are added to your force")
            else:
                print("You Dont Have enough Money")
    else:
        print("You cannot Buy because airport is not available yet")


def deductMoney(i):
    global game_data
    game_data['status']['resources']['money'] -= i


def buyDS():
    global game_data
    available = game_data['build']['defence system']
    if available:
        if game_data['status']['damages']['defence system'] > 75:
            print(
                "Defence System is Damaged You should repair\nreparing cost(500€) for 10% repair"
            )
            re = input("(y/n)")
            if re == "y" or re == "Y":
                print("Repairing Defence System")
                prev = game_data['status']['damages']['defence system']
                game_data['status']['damages']['defence system'] -= 10
                t.sleep(2)
                deductMoney(500)
                print("Repaired Defence System from ", prev, "% to ",
                      game_data['status']['damages']['defence system'], "%")

    else:
        print("You cannot Buy because Baracks is not available yet")


def buyBaracks():
    global game_data
    available = game_data['build']['barracks']
    if available:
        if game_data['status']['damages']['barracks'] > 75:
            print(
                "Baracks is Damaged You should repair\nreparing cost(500€) for 10% repair"
            )
            re = input("(y/n)")
            if re == "y" or re == "Y":
                print("Repairing Barracks")
                prev = game_data['status']['damages']['barracks']
                game_data['status']['damages']['barracks'] -= 10
                t.sleep(2)
                deductMoney(500)
                print("Repaired Baracks from ", prev, "% to ",
                      game_data['status']['damages']['barracks'], "%")
        else:
            print("You can Buy Barracks\n 1 Barrack costs (2000€)")
            opt = int(input("How much you want to buy Barrack :"))
            cost = opt * 2000
            bal = game_data['status']['resources']['money']
            if cost <= bal:
                print("Costs : ", cost, "\nYour Balance : ", bal)
                print("Buying ", opt, " Barracks")
                deductMoney(cost)
                t.sleep(2)
                addResource("barracks", opt)
                print(opt, "Barracks are added to your force")
            else:
                print("You Dont Have enough Money")
    else:
        print("You cannot Buy because Baracks is not available yet")


def buyBuilding():
    global game_data
    available = game_data['build']['building']
    if available:
        print("You can Buy Building\n 1 Building costs (2000€)")
        opt = int(input("How much you want to buy building "))
        cost = opt * 2000
        bal = game_data['status']['resources']['money']
        if cost <= bal:
            print("Costs : ", cost, "\nYour Balance : ", bal)
            print("Buying ", opt, " Building")
            deductMoney(cost)
            t.sleep(2)
            print(opt, "Building are added to your force")
            game_data['status']['resources']['soldier'] += 5
        else:
            print("You Dont Have enough Money")
    else:
        print("You cannot Buy because Building is not available yet")


def buySoldier():
    global game_data
    print("You can Buy Solider\n 1  Solider costs (300€)")
    opt = int(input("How much you want to buy Soliders "))
    cost = opt * 300
    bal = game_data['status']['resources']['money']
    if cost <= bal:
        print("Costs : ", cost, "\nYour Balance : ", bal)
        print("Buying ", opt, " Solider")
        deductMoney(cost)
        t.sleep(2)
        print(opt, " Soldier are added to your force")
        game_data['status']['resources']['soldier'] += opt
    else:
        print("You Dont Have enough Money")


def buyEliteSoliders():
    global game_data
    print("You can Buy Elite Solider\n 1 Elite Solider costs (700€)")
    opt = int(input("How much you want to buy ELite Soliders "))
    cost = opt * 700
    bal = game_data['status']['resources']['money']
    if cost <= bal:
        print("Costs : ", cost, "\nYour Balance : ", bal)
        print("Buying ", opt, " Elite Solider")
        deductMoney(cost)
        t.sleep(2)
        print(opt, "Elite Soldier are added to your force")
        game_data['status']['resources']['soldier'] += 2
        game_data['status']['resources']['elite'] += opt
    else:
        print("You Dont Have enough Money")


def buy():
    global game_data
    print("Available Money :  ", game_data['status']['resources']['money'],
          game_data['status']['resources']['currency'])
    print("Select Item You ant to Buy : ")
    print("A -> Airport (6000€)")
    print("B -> Baracks (2000€)")
    print("T -> Tank Factory (4000€)")
    print("D -> Defence System (3000€)")
    print("________________________")
    #print("0 -> Building (Repair or Buy)")
    print("1 -> Elite Soldiers (700€)")
    print("2 -> Soldier (300€)")
    opt = input(">")
    if opt == "A" or opt == 'a':
        buyAirport()
    elif opt == "B" or opt == 'b':
        buyBaracks()
    elif opt == "T" or opt == 't':
        buyTankFactory()
    elif opt == "D" or opt == 'd':
        buyDS()
    elif opt == "0":
        buyBuilding()
    elif opt == "1":
        buyEliteSoliders()
    elif opt == "2":
        buySoldier()

def check_strenth(i,j):
    import random as re
    en_points = 0
    pl_points = 0
    en_points += i['barracks'] + i['soldiers'] + i['elite'] + i['tanks'] + i['airport']
    if i['defence system']:
        en_points +=5
    if i['oil mine'] or i['gold mine']:
        en_points += 3500

    r = j['resources']
    pl_points += r['barracks'] + r['soldier'] + r['elite'] + r['tanks'] + r['airplanes']
    if game_data['build']['defence system']:
        pl_points +=5
    pl_points += r['money']

    f =(re.randint(1,1000))/1000
    if f > 0.5:
        return True
    else:
        return False

  
def attack():
    global game_data
    en = game_data['player']['experience']
    if en == "easy":
      comp = check_strenth(enemy['easy'],game_data['status'])
      if comp:
        print("Congratulation Commander! you won the attack. Following loot we found")
        for s in enemy['easy']:
            print(s," -> ",enemy['easy'][s])
        print("Adding the loot to your Resources")
        t.sleep(2)
        game_data['status']['resources']['soldier'] += enemy['easy']['soldiers'];
        game_data['status']['resources']['elite'] += enemy['easy']['elite'];
        game_data['status']['resources']['tanks'] += enemy['easy']['tanks'];
      else:
        print("Commander You Lost the Attack")
        game_data['status']['resources']['soldier'] -= 5
        game_data['status']['resources']['elite'] -= 2
        game_data['status']['resources']['tanks'] -= 1
        game_data['status']['damages']['barracks'] += 10
        game_data['status']['damages']['tanks'] += 10
        game_data['status']['damages']['airport'] += 10
        game_data['status']['damages']['defence system'] += 10

      clear()
    elif en == "medium":
      comp = check_strenth(enemy['medium'],game_data['status'])
      if comp:
        print("Congratulation Commander! you won the attack. Following loot we found")
        for s in enemy['medium']:
            print(s," -> ",enemy['medium'][s])
        print("Adding the loot to your Resources")
        t.sleep(2)
        game_data['status']['resources']['soldier'] += enemy['medium']['soldiers'];
        game_data['status']['resources']['elite'] += enemy['medium']['elite'];
        game_data['status']['resources']['tanks'] += enemy['medium']['tanks'];
      else:
        print("Commander You Lost the Attack")
        game_data['status']['resources']['soldier'] -= 5
        game_data['status']['resources']['elite'] -= 2
        game_data['status']['resources']['tanks'] -= 1
        game_data['status']['damages']['barracks'] += 10
        game_data['status']['damages']['tanks'] += 10
        game_data['status']['damages']['airport'] += 10
        game_data['status']['damages']['defence system'] += 10
      clear()
    elif en == "hard":
      comp = check_strenth(enemy['hard'],game_data['status'])
      if comp:
        print("Congratulation Commander! you won the attack. Following loot we found")
        for s in enemy['hard']:
            print(s," -> ",enemy['hard'][s])
        print("Adding the loot to your Resources")
        t.sleep(2)
        game_data['status']['resources']['soldier'] += enemy['hard']['soldiers'];
        game_data['status']['resources']['elite'] += enemy['hard']['elite'];
        game_data['status']['resources']['tanks'] += enemy['hard']['tanks'];
      else:
        print("Commander You Lost the Attack")
        game_data['status']['resources']['soldier'] -= 5
        game_data['status']['resources']['elite'] -= 2
        game_data['status']['resources']['tanks'] -= 1
        game_data['status']['damages']['barracks'] += 10
        game_data['status']['damages']['tanks'] += 10
        game_data['status']['damages']['airport'] += 10
        game_data['status']['damages']['defence system'] += 10
      clear()



def save():
    global game_data
    print("Saving Game .....")
    t.sleep(2)
    with open('config.json', 'w') as outfile:
        json.dump(game_data, outfile, indent=4)
    print("Game Saved ")
    opt = input("Do You Want to Exit (Y/N) ?")
    if opt == "Y" or opt == 'y':
        exit()


def load_game():
    global game_data
    with open('config.json') as json_file:
        game_data = json.load(json_file)


def checkData():
    global game_data
    if game_data['status']['resources']['soldier'] > 25:
        game_data['build']['building'] = True
    elif game_data['status']['resources']['elite'] > 30:
        game_data['build']['barracks'] = True
    elif game_data['status']['resources']['elite'] > 35 and game_data[
            'status']['resources']['soldier'] > 35:
        game_data['build']['tank factory'] = True
        game_data['build']['airport'] = True


def checktreasure():
    import random as r
    minTreasure = 1000
    maxTreasure = 10001
    d = [f for f in range(minTreasure, maxTreasure, 50)]
    if r.randint(1, 10) % 2 == 0:
        a = r.choice(d)
        mines = ["Oil Mine", "Gold Mine"]
        print("Hey Commander you found (", r.choice(mines), ") with loot ", a,
              "€ loot")
        global game_data
        game_data['status']['resources'][
            'money'] = game_data['status']['resources']['money'] + a


if checkGameStatus():
    load_game()
else:
    init_game()

flag = True
previous_slection = ""
count = 0
OPTIONS = ["N", "E", "W", "S", "1", "2", "3", "4"]
while flag:
    t.sleep(2)
    clear()
    checkData()
    print("Please Select Option")
    print("|MOVEMENTS| => N (North), E(East), W(West), S(South)")
    print("|ACTIONS|   => 1(Status),2(Buy),3(Attack), 4(SAVE AND EXIT)")
    opt = input("Enter Option : ")
    if opt in OPTIONS:
        if previous_slection == opt:
            count += 1
        else:
            count = 0
        if count >= 10:
            print("Sea Found Cannot Move Forward")
            pass
    else:
        print("Invalid Option Selection")
        pass
    if opt == "N":
        print("Moving North Found ", NORTH[0], NORTH[1], NORTH[2])
        checktreasure()
    elif opt == "E":
        print("Moving East Found ", EAST[0], EAST[1], EAST[2])
        checktreasure()
    elif opt == "W":
        print("Moving West Found ", WEST[0], WEST[1], WEST[2])
        checktreasure()
    elif opt == "S":
        print("Moving South Found ", SOUTH[0], SOUTH[1], SOUTH[2])
        checktreasure()
    elif opt == "1":
        showStatus()
    elif opt == "2":
        buy()
    elif opt == "3":
        attack()
    elif opt == "4":
        save()
    else:
        print("Invalid Option Selection")
        pass
