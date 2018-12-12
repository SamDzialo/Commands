"""
author: Sam Dzialo
Email: sad8333@rit.edu
language: python3.7
description: Interpreter Program solution
"""
import turtle as tt


def processing(commands):
    """The processing function takes in a in a string that runs through the string using the key symbols to access the
     if statements and then uses the findnum function to get the numbers that are used in each process"""
    while commands != "":
        ch = commands[0]
        chnum = 0
        if ch == "<":
            if commands[1].isdigit():
                pass
            else:
                print("Error")
                break
            chnum += 1
            num = findnum(commands[1:])
            chnum += len(num)
            left(int(num))
            commands = commands[chnum:]
        elif ch == ">":
            if commands[1].isdigit():
                pass
            else:
                print("Error")
                break
            chnum += 1
            num = findnum(commands[1:])
            chnum += len(num)
            right(int(num))
            commands = commands[chnum:]
        elif ch == "S":
            if commands[1].isdigit():
                pass
            else:
                print("Error")
                break
            chnum += 1
            num = findnum(commands[1:])
            chnum += len(num)
            square(int(num))
            commands = commands[chnum:]
        elif ch == "T":
            if commands[1].isdigit():
                pass
            else:
                print("Error")
                break
            chnum += 1
            num = findnum(commands[1:])
            chnum += len(num)
            triangle(int(num))
            commands = commands[chnum:]
        elif ch == "C":
            if commands[1].isdigit():
                pass
            else:
                print("Error")
                break
            chnum += 1
            num = findnum(commands[1:])
            chnum += len(num)
            circle(int(num))
            commands = commands[chnum:]
        elif ch == "F":
            if commands[1].isdigit():
                pass
            else:
                print("Error")
                break
            chnum += 1
            num = findnum(commands[1:])
            chnum += len(num)
            forward(int(num))
            commands = commands[chnum:]
        elif ch == "B":
            if commands[1].isdigit():
                pass
            else:
                print("Error")
                break
            chnum += 1
            num = findnum(commands[1:])
            chnum += len(num)
            backwards(int(num))
            commands = commands[chnum:]
        elif ch == "U":
            chnum += 1
            tt.up()
            commands = commands[chnum:]
        elif ch == "D":
            chnum += 1
            tt.down()
            commands = commands[chnum:]
        elif ch == "R":
            if commands[1].isdigit():
                pass
            else:
                print("Error")
                break
            chnum += 1
            length = findnum(commands[1:])
            chnum += len(length)
            if commands[chnum] == ",":
                chnum += 1
                width = findnum(commands[chnum:])
                chnum += len(width)
            else:
                print("Incorrect Input")
                break
            rectangle(int(length), int(width))
            commands = commands[chnum:]
        elif ch == "P":
            if commands[1].isdigit():
                pass
            else:
                print("Error")
                break
            chnum += 1
            side = findnum(commands[1:])
            chnum += len(side)
            if commands[chnum] == ",":
                chnum += 1
                length = findnum(commands[chnum:])
                chnum += len(length)
            else:
                print("Incorrect Input")
                break
            polygon(int(side), int(length))
            commands = commands[chnum:]
        elif ch == "G":
            if commands[1].isdigit():
                pass
            else:
                print("Error")
                break
            chnum += 1
            x = findnum(commands[1:])
            chnum += len(x)
            if commands[chnum] == ",":
                chnum += 1
                y = findnum(commands[chnum:])
                chnum += len(y)
            else:
                print("Incorrect Input")
                break
            goto(int(x), int(y))
            commands = commands[chnum:]
        elif ch == "Z":
            if commands[1].isdigit():
                pass
            else:
                print("Error")
                break
            chnum += 1
            num = findnum(commands[1:])
            chnum += len(num)
            color(int(num))
            commands = commands[chnum:]
        else:
            print("Incorrect Command")
            break


def left(deg):
    """Turns the turtle left deg degrees"""
    tt.left(deg)


def right(deg):
    """Turns the turtle right deg degrees"""
    tt.right(deg)


def square(length):
    """Makes a square with side length of length using turtle"""
    tt.left(90)
    tt.fd(length)
    tt.left(90)
    tt.fd(length)
    tt.left(90)
    tt.fd(length)
    tt.left(90)
    tt.fd(length)


def triangle(length):
    """Makes a triangle with side length of length using turtle"""
    tt.left(120)
    tt.fd(length)
    tt.left(120)
    tt.fd(length)
    tt.left(120)
    tt.fd(length)


def circle(rad):
    """Makes a circle with a radius of rad"""
    tt.circle(rad)


def forward(dist):
    """Moves the turtle forward a length of dist"""
    tt.fd(dist)


def backwards(dist):
    """Moves the turtle backwards a length of dist"""
    tt.fd(-dist)


def rectangle(length, width):
    """Takes two ints and then creates a rectangle with sides of length and width"""
    tt.left(90)
    tt.fd(width)
    tt.left(90)
    tt.fd(length)
    tt.left(90)
    tt.fd(width)
    tt.left(90)
    tt.fd(length)


def polygon(sides, length):
    """Takes in a side int and length int and reates a polygon
    with the number of sides at that length"""
    angle = 360 / sides
    tt.left(angle)
    for i in range(sides):
        tt.fd(length)
        tt.left(angle)
    tt.right(angle)


def goto(x, y):
    """Takes in two ints and then moves turtle to those coordinates. """
    tt.goto(x, y)


def color(num):
    """Takes in a number and then selects the color that it correspond with"""
    if num == 0:
        tt.pencolor("red")
    elif num == 1:
        tt.pencolor("blue")
    elif num == 2:
        tt.pencolor("green")
    elif num == 3:
        tt.pencolor("yellow")
    elif num == 4:
        tt.pencolor("brown")
    else:
        tt.pencolor("black")


def findnum(string):
    """Finds the first numbers in the string received"""
    number = ""
    for ch in string:
        if ch.isdigit():
            number += ch
        else:
            break
    return number


def main():
    """Takes in the Command string and then sends it to be processed"""
    commands = input("Enter the commands: ")
    processing(commands)
    turtle.done()


main()
