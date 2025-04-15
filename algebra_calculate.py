import pygame, time, sys, random, os, arcade, math
from pygame.locals import *
from fractions import *
from time import gmtime, strftime

pygame.display.set_mode()
screen = pygame.display.set_mode((1800, 1000),pygame.FULLSCREEN)
pygame.init()

pygame.display.set_caption('Show Text') 
font = pygame.font.Font('freesansbold.ttf', 64) 
bigger_font = pygame.font.Font('freesansbold.ttf', 96) 

run = True

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

screen.fill(black)

                #numbers
def zero(x, y):
    zero = font.render('0', True, blue)
    screen.blit(zero, (x, y)) 
def one(x, y):
    one = font.render('1', True, blue)
    screen.blit(one, (x, y)) 
def two(x, y):
    two = font.render('2', True, blue)
    screen.blit(two, (x, y)) 
def three(x, y):
    three = font.render('3', True, blue)
    screen.blit(three, (x, y))     
def four(x, y):
    four = font.render('4', True, blue)
    screen.blit(four, (x, y)) 
def five(x, y):
    five = font.render('5', True, blue)
    screen.blit(five, (x, y)) 
def six(x, y):
    six = font.render('6', True, blue)
    screen.blit(six, (x, y)) 
def seven(x, y):
    seven = font.render('7', True, blue)
    screen.blit(seven, (x, y)) 
def eight(x, y):
    eight = font.render('8', True, blue)
    screen.blit(eight, (x, y)) 
def nine(x, y):
    nine = font.render('9', True, blue)
    screen.blit(nine, (x, y)) 

press0 = False
press1 = False
press2 = False
press3 = False
press4 = False
press5 = False
press6 = False
press7 = False
press8 = False
press9 = False
press_x = False
            #operation signs
def plus(x, y):
    plus = bigger_font.render('+', True, blue)
    screen.blit(plus, (x, y)) 
def minus(x, y):
    minus = bigger_font.render('-', True, blue)
    screen.blit(minus, (x, y)) 
def multiply(x, y):
    multiply = bigger_font.render('*', True, blue)
    screen.blit(multiply, (x, y)) 
def divide(x, y):
    divide = bigger_font.render('/', True, blue)
    screen.blit(divide, (x, y)) 

def exponentiate(x, y):
    exponentiate = font.render('^', True, blue)
    screen.blit(exponentiate, (x, y)) 

def open_parenthesis(x, y):
    open_parenthesis = bigger_font.render('(', True, blue)
    screen.blit(open_parenthesis, (x, y)) 

def closed_parenthesis(x, y):
    closed_parenthesis = bigger_font.render(')', True, blue)
    screen.blit(closed_parenthesis, (x, y)) 

def equal(x, y):
    equal = bigger_font.render('=', True, green)
    screen.blit(equal, (x, y)) 

def X(x, y):
    X = bigger_font.render('x', True, darkBlue)
    screen.blit(X, (x, y)) 

press_plus = False
press_minus = False
press_multiply = False
press_divide = False
press_equal = False
press_exponentiate = False
press_open_parenthesis = False
press_closed_parenthesis = False


def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier
showing_answer = False
answer = 0
def show_answer(x, y):
    show_answer = bigger_font.render(("x = " + str(round_half_up(answer, 3))), True, (255, 40, 0))
    screen.blit(show_answer, (x, y)) 




added_number = False

digits = []

part1 = True
part2 = False
expression1 = []
expression2 = []
digit_count = 0

equation = ""

first_number = True
adding = False
subtracting = False
multiplying = False
dividing = False
multiply_by_negative = False
multiply_by_negative2 = False
multiply_by_negative_in_parenthesis = False
multiply_by_negative_in_parenthesis2 = False
exponentiating = False
in_parenthesis = False
there_is_parenthesis = False 
there_is_parenthesis2 = False 


adding_numbers = []
adding_numbers_in_parenthesis = []
subtracting_numbers = []
subtracting_numbers_in_parenthesis = []
multiplying_numbers = []
multiplying_numbers_in_parenthesis = []
dividing_numbers = []
dividing_numbers_in_parenthesis = []
exponents = []
exponents_in_parenthesis = []

adding_numbers2 = []
adding_numbers_in_parenthesis2 = []
subtracting_numbers2 = []
subtracting_numbers_in_parenthesis2 = []
multiplying_numbers2 = []
multiplying_numbers_in_parenthesis2 = []
dividing_numbers2 = []
dividing_numbers_in_parenthesis2 = []
exponents2 = []
exponents_in_parenthesis2 = []


def show_equation(x, y):
    show_equation = font.render(equation, True, red)
    screen.blit(show_equation, (x, y)) 

simplify = False
step_zero = False
step_one = False
step_one_v2 = False
step_two = False
step_two_v2 = False
step_three = False
step_three_v2 = False
step_four = False
step_four_v2 = False
step_five = False
step_five_v2 = False
step_six = False
step_six_v2 = False

def show_step1(x, y):
    show_step1 = font.render(step1, True, red)
    screen.blit(show_step1, (x, y)) 
def show_step2(x, y):
    show_step2 = font.render(step2, True, red)
    screen.blit(show_step2, (x, y)) 
def show_step3(x, y):
    show_step3 = font.render(step3, True, red)
    screen.blit(show_step3, (x, y)) 
def show_step4(x, y):
    show_step4 = font.render(step4, True, red)
    screen.blit(show_step4, (x, y)) 
def show_step5(x, y):
    show_step5 = font.render(step5, True, red)
    screen.blit(show_step5, (x, y)) 
def show_x(x, y):
    show_x = font.render(("x = " + str(answer)), True, (255,165,0))
    screen.blit(show_x, (x, y)) 

check_mouse = False


                    #method to combine coeeficients of x
number = 1/3 + 1/6
a = Fraction(1, 6)
b = Fraction(2, 6)
number = a + b

while run:
    zero(200, 100)
    one(350, 100)
    two(500, 100)
    three(650, 100)
    four(800, 100)
    five(950, 100)
    six(1100, 100)
    seven(1250, 100)
    eight(1400, 100)
    nine(1550, 100)

    plus(300, 300)
    minus(700, 300)
    multiply(1100, 300)
    divide(1500, 300)
    exponentiate(1650, 85)
    open_parenthesis(500, 470)
    closed_parenthesis(1300, 470)

    equal(900, 300)

    X(900, 470)

                                                        #typing numbers

    if press0:
        digits.append(0)
        digit_count += 1
        equation += "0"
        press0 = False
    if press1:
        digits.append(1)
        digit_count += 1
        equation += "1"
        press1 = False
    if press2:
        digits.append(2)
        digit_count += 1
        equation += "2"
        press2 = False
    if press3:
        digits.append(3)
        digit_count += 1
        equation += "3"
        press3 = False
    if press4:
        digits.append(4)
        digit_count += 1
        equation += "4"
        press4 = False
    if press5:
        digits.append(5)
        digit_count += 1
        equation += "5"
        press5 = False
    if press6:
        digits.append(6)
        digit_count += 1
        equation += "6"
        press6 = False
    if press7:
        digits.append(7)
        digit_count += 1
        equation += "7"
        press7 = False
    if press8:
        digits.append(8)
        digit_count += 1
        equation += "8"
        press8 = False
    if press9:
        digits.append(9)
        digit_count += 1
        equation += "9"
        press9 = False
         
    if press_x:   
        if digit_count == 1:
            number = digits[0]
        if digit_count == 2:
            number = str(digits[0]) + str(digits[1])
        if digit_count == 3:
            number = str(digits[0]) + str(digits[1]) + str(digits[2])
        if digit_count == 4:
            number = str(digits[0]) + str(digits[1]) + str(digits[2]) + str(digits[3])
        if digit_count > 0 and dividing is not True:
            multiplying_numbers.append(number)
        if subtracting:
            multiply_by_negative = True

        if part1:
            expression1.append("x")
        if part2:
            expression2.append("x")
            
        if digit_count > 0:
            equation += "x "
        if digit_count == 0:
            equation += " x "

        first_number = False
        press_x = False        

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
                                                        #pressing numbers
            if mousex >= 200 and mousex <= 240 and mousey >= 100 and mousey <= 160 or press0:
                digits.append(0)
                digit_count += 1
                equation += "0"
                press0 = False
            if mousex >= 350 and mousex <= 390 and mousey >= 100 and mousey <= 160:
                digits.append(1)
                digit_count += 1
                equation += "1"
                press1 = False
            if mousex >= 500 and mousex <= 540 and mousey >= 100 and mousey <= 160 or press2:
                digits.append(2)
                digit_count += 1
                equation += "2"
                press2 = False
            if mousex >= 650 and mousex <= 690 and mousey >= 100 and mousey <= 160 or press3:
                digits.append(3)
                digit_count += 1
                equation += "3"
                press3 = False
            if mousex >= 800 and mousex <= 840 and mousey >= 100 and mousey <= 160 or press4:
                digits.append(4)
                digit_count += 1
                equation += "4"
                press4 = False
            if mousex >= 950 and mousex <= 990 and mousey >= 100 and mousey <= 160 or press5:
                digits.append(5)
                digit_count += 1
                equation += "5"
                press5 = False
            if mousex >= 1100 and mousex <= 1140 and mousey >= 100 and mousey <= 160 or press6:
                digits.append(6)
                digit_count += 1
                equation += "6"
                press6 = False
            if mousex >= 1250 and mousex <= 1290 and mousey >= 100 and mousey <= 160 or press7:
                digits.append(7)
                digit_count += 1
                equation += "7"
                press7 = False
            if mousex >= 1400 and mousex <= 1440 and mousey >= 100 and mousey <= 160 or press8:
                digits.append(8)
                digit_count += 1
                equation += "8"
                press8 = False
            if mousex >= 1550 and mousex <= 1590 and mousey >= 100 and mousey <= 160 or press9:
                digits.append(9)
                digit_count += 1
                equation += "9"
                press9 = False
                                                                                          #pressing operations
            if mousex >= 300 and mousex <= 360 and mousey >= 300 and mousey <= 380:
                if digit_count == 1:
                    number = digits[0]
                if digit_count == 2:
                    number = str(digits[0]) + str(digits[1])
                if digit_count == 3:
                    number = str(digits[0]) + str(digits[1]) + str(digits[2])
                if digit_count == 4:
                    number = str(digits[0]) + str(digits[1]) + str(digits[2]) + str(digits[3])

                        #(for previous number) 
                if part1:
                    if first_number and digit_count >= 1 and subtracting is False and number not in multiplying_numbers and not in_parenthesis:
                        adding_numbers_in_parenthesis.append(number)
                    if first_number and digit_count >= 1 and subtracting is False and number not in multiplying_numbers and in_parenthesis:
                        adding_numbers.append(number)
                    if adding and number not in multiplying_numbers and not in_parenthesis:
                        adding_numbers.append(number)
                    if adding and number not in multiplying_numbers and in_parenthesis:
                        adding_numbers_in_parenthesis.append(number)

                    if subtracting and number not in multiplying_numbers and not in_parenthesis:
                        subtracting_numbers.append(number)
                    if subtracting and number not in multiplying_numbers and in_parenthesis:
                        subtracting_numbers_in_parenthesis.append(number)

                    if multiplying and not in_parenthesis:
                        multiplying_numbers.append(number)
                    if multiplying and in_parenthesis:
                        multiplying_numbers_in_parenthesis.append(number)

                    if dividing and not in_parenthesis:
                        dividing_numbers.append(number)
                    if dividing and in_parenthesis:
                        dividing_numbers_in_parenthesis.append(number)

                if part2:
                    if first_number and digit_count >= 1 and subtracting is False and number not in multiplying_numbers2 and not in_parenthesis:
                        adding_numbers_in_parenthesis2.append(number)
                    if first_number and digit_count >= 1 and subtracting is False and number not in multiplying_numbers2 and in_parenthesis:
                        adding_numbers2.append(number)
                    if adding and number not in multiplying_numbers2 and not in_parenthesis:
                        adding_numbers2.append(number)
                    if adding and number not in multiplying_numbers2 and in_parenthesis:
                        adding_numbers_in_parenthesis2.append(number)

                    if subtracting and number not in multiplying_numbers2 and not in_parenthesis:
                        subtracting_numbers2.append(number)
                    if subtracting and number not in multiplying_numbers2 and in_parenthesis:
                        subtracting_numbers_in_parenthesis2.append(number)

                    if multiplying and not in_parenthesis:
                        multiplying_numbers2.append(number)
                    if multiplying and in_parenthesis:
                        multiplying_numbers_in_parenthesis2.append(number)

                    if dividing and not in_parenthesis:
                        dividing_numbers2.append(number)
                    if dividing and in_parenthesis:
                        dividing_numbers_in_parenthesis2.append(number)


                adding = True
                subtracting = False
                multiplying = False
                dividing = False

                try:
                   if part1 and expression1[-1] != "x":
                       expression1.append(number)
                       expression1.append("+")
                except:
                    expression1.append(number)
                    expression1.append("+")
                if part2 and "x" not in expression2:
                    expression2.append(number)
                    expression2.append("+")
                digits.clear()
                digit_count = 0
                

                equation += " + "

                if first_number:
                    first_number = False
            if mousex >= 700 and mousex <= 780 and mousey >= 275 and mousey <= 400:
                if digit_count == 1:
                    number = digits[0]
                if digit_count == 2:
                    number = str(digits[0]) + str(digits[1])
                if digit_count == 3:
                    number = str(digits[0]) + str(digits[1]) + str(digits[2])
                if digit_count == 4:
                    number = str(digits[0]) + str(digits[1]) + str(digits[2]) + str(digits[3])

                        #(for previous number)    

                if part1:
                    if first_number and digit_count >= 1:
                        if not in_parenthesis:
                            adding_numbers.append(number)
                        if in_parenthesis:
                            adding_numbers_in_parenthesis.append(number)
                    if adding:
                        if not in_parenthesis:
                            adding_numbers.append(number)
                        if in_parenthesis:
                            adding_numbers_in_parenthesis.append(number)
                    if subtracting:
                        if not in_parenthesis:
                            subtracting_numbers.append(number)
                        if in_parenthesis:
                            subtracting_numbers_in_parenthesis.append(number)
                    if multiplying:
                        if not in_parenthesis:
                            multiplying_numbers.append(number)
                        if in_parenthesis:
                            multiplying_numbers_in_parenthesis.append(number)
                    if dividing:
                        if not in_parenthesis:
                            dividing_numbers.append(number)
                        if in_parenthesis:
                            dividing_numbers_in_parenthesis.append(number)
                if part2:
                    if first_number and digit_count >= 1:
                        if not in_parenthesis:
                            adding_numbers2.append(number)
                        if in_parenthesis:
                            adding_numbers_in_parenthesis2.append(number)
                    if adding:
                        if not in_parenthesis:
                            adding_numbers2.append(number)
                        if in_parenthesis:
                            adding_numbers_in_parenthesis2.append(number)
                    if subtracting:
                        if not in_parenthesis:
                            subtracting_numbers2.append(number)
                        if in_parenthesis:
                            subtracting_numbers_in_parenthesis2.append(number)
                    if multiplying:
                        if not in_parenthesis:
                            multiplying_numbers2.append(number)
                        if in_parenthesis:
                            multiplying_numbers_in_parenthesis2.append(number)
                    if dividing:
                        if not in_parenthesis:
                            dividing_numbers2.append(number)
                        if in_parenthesis:
                            dividing_numbers_in_parenthesis2.append(number)

                adding = False
                subtracting = True
                multiplying = False
                dividing = False

                if part1 and digit_count > 0 and number not in expression1:
                    expression1.append(number)
                if part1:
                    expression1.append("-")
                if part2 and digit_count > 0 and number not in expression1:
                    expression2.append(number)
                if part2:
                    expression2.append("-")

                if not first_number:
                    equation += " - "
                if first_number and digit_count == 0:
                    equation += " -"

                digits.clear()
                digit_count = 0
                

                first_number = False
            if mousex >= 1100 and mousex <= 1160 and mousey >= 300 and mousey <= 380:
                if digit_count == 1:
                    number = digits[0]
                if digit_count == 2:
                    number = str(digits[0]) + str(digits[1])
                if digit_count == 3:
                    number = str(digits[0]) + str(digits[1]) + str(digits[2])
                if digit_count == 4:
                    number = str(digits[0]) + str(digits[1]) + str(digits[2]) + str(digits[3])

                        #(for previous number)   
                if part1:             
                    if adding or subtracting or multiplying:
                        if number not in multiplying_numbers:
                            if not in_parenthesis:
                                multiplying_numbers.append(number)
                            if in_parenthesis:
                                multiplying_numbers_in_parenthesis.append(number)
                    if subtracting:
                        if not in_parenthesis:
                            multiply_by_negative = True
                        if in_parenthesis:
                            multiply_by_negative_in_parenthesis = True
                    if dividing:
                        if not in_parenthesis:
                            dividing_numbers.append(number)
                        if in_parenthesis:
                            dividing_numbers_in_parenthesis.append(number)

                if part2:             
                    if adding or subtracting or multiplying:
                        if number not in multiplying_numbers2:
                            if not in_parenthesis:
                                print(str(number) + " is in multiplying numbers")
                                multiplying_numbers2.append(number)
                            if in_parenthesis:
                                multiplying_numbers_in_parenthesis2.append(number)
                    if subtracting:
                        if not in_parenthesis:
                            multiply_by_negative2 = True
                        if in_parenthesis:
                            multiply_by_negative_in_parenthesis2 = True
                    if dividing:
                        if not in_parenthesis:
                            dividing_numbers2.append(number)
                        if in_parenthesis:
                            dividing_numbers_in_parenthesis2.append(number)

                adding = False
                subtracting = False
                multiplying = True
                dividing = False

                if part1:
                    expression1.append(number)
                    expression1.append("*")
                if part2:
                    expression2.append(number)
                    expression2.append("*")
                digits.clear()
                digit_count = 0
                
                if first_number:
                    first_number = False

                equation += " * "
            if mousex >= 1500 and mousex <= 1560 and mousey >= 300 and mousey <= 380:
                if digit_count == 1:
                    number = digits[0]
                if digit_count == 2:
                    number = str(digits[0]) + str(digits[1])
                if digit_count == 3:
                    number = str(digits[0]) + str(digits[1]) + str(digits[2])
                if digit_count == 4:
                    number = str(digits[0]) + str(digits[1]) + str(digits[2]) + str(digits[3])

                        #(for previous number)  
                if part1:              
                    if len(expression1) > 0:
                        if expression1[-1] == "x":
                            number = 1

                    if subtracting:
                        if not in_parenthesis:
                            multiply_by_negative = True
                        if in_parenthesis:
                            multiply_by_negative_in_parenthesis = True
                    if adding or subtracting or multiplying or first_number:
                        if not in_parenthesis:
                            multiplying_numbers.append(number)
                        if in_parenthesis:
                            multiplying_numbers_in_parenthesis.append(number)
                    if dividing:
                        if not in_parenthesis:
                            dividing_numbers.append(number)
                        if in_parenthesis:
                            dividing_numbers_in_parenthesis.append(number)

                if part2:              
                    if len(expression2) > 0:
                        if expression2[-1] == "x":
                            number = 1

                    if subtracting:
                        if not in_parenthesis:
                            multiply_by_negative2 = True
                        if in_parenthesis:
                            multiply_by_negative_in_parenthesis2 = True
                    if adding or subtracting or multiplying or first_number:
                        if not in_parenthesis:
                            dividing_numbers2.append(number)
                        if in_parenthesis:
                            dividing_numbers_in_parenthesis2.append(number)
                    if dividing:
                        if not in_parenthesis:
                            dividing_numbers2.append(number)
                        if in_parenthesis:
                            dividing_numbers_in_parenthesis2.append(number)

                adding = False
                subtracting = False
                multiplying = False
                dividing = True
                if part1:
                    expression1.append(number)
                    expression1.append("/")
                if part2:
                    expression2.append(number)
                    expression2.append("/")
                digits.clear()
                digit_count = 0
                

                first_number = False

                equation += "/"
                                                    #exponents
            if mousex >= 1640 and mousex <= 1700 and mousey >= 80 and mousey <= 145:
                if digit_count == 1:
                    number = digits[0]
                if digit_count == 2:
                    number = str(digits[0]) + str(digits[1])
                if digit_count == 3:
                    number = str(digits[0]) + str(digits[1]) + str(digits[2])
                if digit_count == 4:
                    number = str(digits[0]) + str(digits[1]) + str(digits[2]) + str(digits[3])

                        #(for previous number)   
                if part1:        
                    if subtracting:
                        if not in_parenthesis:
                            multiply_by_negative = True
                        if in_parenthesis:
                            multiply_by_negative_in_parenthesis = True
                    if adding or first_number:
                        if not in_parenthesis:
                            adding_numbers.append(number)
                        if in_parenthesis:
                            adding_numbers_in_parenthesis.append(number)
                    if subtracting:
                        if not in_parenthesis:
                            subtracting_numbers.append(number)
                        if in_parenthesis:
                            subtracting_numbers_in_parenthesis.append(number)
                    if multiplying:
                        if not in_parenthesis:
                            multiplying_numbers.append(number)
                        if in_parenthesis:
                            multiplying_numbers_in_parenthesis.append(number)
                    if dividing:
                        if not in_parenthesis:
                            dividing_numbers.append(number)
                        if in_parenthesis:
                            dividing_numbers_in_parenthesis.append(number)

                    if expression1[-1] == ")":
                        exponentiating_parenthesis = True
                        print("exponent on parenthesis")

                if part2:        
                    if subtracting:
                        if not in_parenthesis:
                            multiply_by_negative2 = True
                        if in_parenthesis:
                            multiply_by_negative_in_parenthesis2 = True
                    if adding or first_number:
                        if not in_parenthesis:
                            adding_numbers2.append(number)
                        if in_parenthesis:
                            adding_numbers_in_parenthesis2.append(number)
                    if subtracting:
                        if not in_parenthesis:
                            subtracting_numbers2.append(number)
                        if in_parenthesis:
                            subtracting_numbers_in_parenthesis2.append(number)
                    if multiplying:
                        if not in_parenthesis:
                            multiplying_numbers2.append(number)
                        if in_parenthesis:
                            multiplying_numbers_in_parenthesis2.append(number)
                    if dividing:
                        if not in_parenthesis:
                            dividing_numbers2.append(number)
                        if in_parenthesis:
                            dividing_numbers_in_parenthesis2.append(number)

                    if expression2[-1] == ")":
                        exponentiating_parenthesis2 = True
                        print("exponent on parenthesis")
                #base.append(number)
        
                adding = False
                subtracting = False
                multiplying = False
                dividing = False
                exponentiating = True
                

                if part1:
                    expression1.append("^(")
                if part2:
                    expression2.append("^(")

                digits.clear()
                digit_count = 0

                equation += "^("

                if first_number:
                    first_number = False
                                                        #parenthesis
                                    #open parenthesis
            if mousex >= 490 and mousex <= 560 and mousey >= 460 and mousey <= 540:
                if digit_count == 1:
                    number = digits[0]
                if digit_count == 2:
                    number = str(digits[0]) + str(digits[1])
                if digit_count == 3:
                    number = str(digits[0]) + str(digits[1]) + str(digits[2])
                if digit_count == 4:
                    number = str(digits[0]) + str(digits[1]) + str(digits[2]) + str(digits[3])

                if part1:
                    if digit_count > 0 and not dividing:
                        multiplying_numbers.append(number)
                    if subtracting:
                        multiply_by_negative = True
                    if dividing:
                        dividing_numbers.append(number)

                if part2:
                    if digit_count > 0 and not dividing:
                        multiplying_numbers2.append(number)
                    if subtracting:
                        multiply_by_negative2 = True
                    if dividing:
                        dividing_numbers2.append(number)
        
                adding = False
                subtracting = False
                multiplying = False
                dividing = False
                exponentiating = False
                in_parenthesis = True
                

                if part1:
                    expression1.append("(")
                if part2:
                    expression2.append("(")

                digits.clear()
                digit_count = 0

                equation += "("

                if part1:
                    there_is_parenthesis = True
                if part2:
                    there_is_parenthesis2 = True

                first_number = True
                                    #closed parenthesis
            if mousex >= 1290 and mousex <= 1370 and mousey >= 460 and mousey <= 540:
                if digit_count == 1:
                    number = digits[0]
                if digit_count == 2:
                    number = str(digits[0]) + str(digits[1])
                if digit_count == 3:
                    number = str(digits[0]) + str(digits[1]) + str(digits[2])
                if digit_count == 4:
                    number = str(digits[0]) + str(digits[1]) + str(digits[2]) + str(digits[3])
          
                if part1:
                    if adding or first_number:
                        adding_numbers_in_parenthesis.append(number)
                    if subtracting:
                        subtracting_numbers_in_parenthesis.append(number)
                    if multiplying:
                        multiplying_numbers_in_parenthesis.append(number)
                    if dividing:
                        dividing_numbers_in_parenthesis.append(number)

                if part2:
                    if adding or first_number:
                        adding_numbers_in_parenthesis2.append(number)
                    if subtracting:
                        subtracting_numbers_in_parenthesis2.append(number)
                    if multiplying:
                        multiplying_numbers_in_parenthesis2.append(number)
                    if dividing:
                        dividing_numbers_in_parenthesis2.append(number)
        
                adding = False
                subtracting = False
                multiplying = False
                dividing = False
                exponentiating = False
                in_parenthesis = False
                

                if part1:
                    expression1.append(")")
                if part2:
                    expression2.append(")")

                digits.clear()
                digit_count = 0

                equation += ")"

                if first_number:
                    first_number = False
            if mousex >= 900 and mousex <= 960 and mousey >= 300 and mousey <= 380 and part1:
                if digit_count > 0:
                    if digit_count == 1:
                        number = digits[0]
                    if digit_count == 2:
                        number = str(digits[0]) + str(digits[1])
                    if digit_count == 3:
                        number = str(digits[0]) + str(digits[1]) + str(digits[2])
                    if digit_count == 4:
                        number = str(digits[0]) + str(digits[1]) + str(digits[2]) + str(digits[3])
                    if number not in expression1:
                        expression1.append(number)
                    digits.clear()
                    digit_count = 0

                        #(for previous number)                
                if adding and number not in multiplying_numbers:
                    adding_numbers.append(number)
                if subtracting and number not in multiplying_numbers:
                    subtracting_numbers.append(number)
                if multiplying:
                    multiplying_numbers.append(number)
                if dividing:
                    dividing_numbers.append(number)

                
                part1 = False
                part2 = True

                adding = True
                subtracting = False
                multiplying = False
                dividing = False

                first_number = True

                equation += "  =  "
                press_equal = False
            if mousex >= 900 and mousex <= 960 and mousey >= 470 and mousey <= 550:   
                if digit_count == 1:
                    number = digits[0]
                if digit_count == 2:
                    number = str(digits[0]) + str(digits[1])
                if digit_count == 3:
                    number = str(digits[0]) + str(digits[1]) + str(digits[2])
                if digit_count == 4:
                    number = str(digits[0]) + str(digits[1]) + str(digits[2]) + str(digits[3])

                if part1:
                    if digit_count > 0 and dividing is not True:
                        if not in_parenthesis:
                            multiplying_numbers.append(number)
                        if in_parenthesis:
                            multiplying_numbers_in_parenthesis.append(number)
                    if subtracting:
                        if not in_parenthesis:
                            multiply_by_negative = True
                        if not in_parenthesis:
                            multiply_by_negative_in_parenthesis = True
                if part2:
                    if digit_count > 0 and dividing is not True:
                        if not in_parenthesis:
                            multiplying_numbers2.append(number)
                        if in_parenthesis:
                            multiplying_numbers_in_parenthesis2.append(number)
                    if subtracting:
                        if not in_parenthesis:
                            multiply_by_negative2 = True
                        if not in_parenthesis:
                            multiply_by_negative_in_parenthesis2 = True

                if part1:
                    if digit_count > 0:
                        expression1.append(number)
                    expression1.append("x")
                   
                if part2:
                    if digit_count > 0:
                        expression2.append(number)
                    expression2.append("x")
            
                if digit_count > 0:
                    equation += "x "
                if digit_count == 0:
                    equation += " x "

                first_number = False
                press_x = False
        if event.type == pygame.KEYUP:
                    #typing numbers on keyboard
            if event.key == pygame.K_0:
                press0 = True
            if event.key == pygame.K_1:
                press1 = True
            if event.key == pygame.K_2:
                press2 = True
            if event.key == pygame.K_3:
                press3 = True
            if event.key == pygame.K_4:
                press4 = True
            if event.key == pygame.K_5:
                press5 = True
            if event.key == pygame.K_6:
                press6 = True
            if event.key == pygame.K_7:
                press7 = True
            if event.key == pygame.K_8:
                press8 = True
            if event.key == pygame.K_9:
                press9 = True
            if event.key == pygame.K_x:
                press_x = True   

    #        if event.key == pygame.K_KP_PLUS:
     #           press_plus = True   
      #      if event.key == pygame.K_KP_MINUS:
       #         press_minus = True   
        #    if event.key == pygame.K_KP_MULTIPLY:
         #       press_multiply = True                   
          #  if event.key == pygame.K_KP_DIVIDE:
           #     press_divide = True 
            #if event.key == pygame.K_EQUALS:
             #   press_divide = True   
                                                        #not exponentiating anymore
            if event.key == pygame.K_DOWN:
                if digit_count == 1:
                    number = digits[0]
                if digit_count == 2:
                    number = str(digits[0]) + str(digits[1])
                if digit_count == 3:
                    number = str(digits[0]) + str(digits[1]) + str(digits[2])
                if digit_count == 4:
                    number = str(digits[0]) + str(digits[1]) + str(digits[2]) + str(digits[3])

                if in_parenthesis is False or exponentiating_parenthesis:
                    exponents.append(number)
                if in_parenthesis:
                    exponents_in_parenthesis.append(number)

                equation += ")"
                if part1:
                    expression1.append(number)
                    expression1.append(")")
                if part2:
                    expression2.append(number)
                    expression2.append(")")
                exponentiating = False
                exponentiating_parenthesis = False
                                                                                               #for deleting
   #         if event.key == pygame.K_BACKSPACE:
                    #appending the digits that were just plugged in (so they can be deleted)
    #            if digit_count == 1:
     #               number = digits[0]
      #          if digit_count == 2:
       #             number = str(digits[0]) + str(digits[1])
         #       if digit_count == 3:
        #            number = str(digits[0]) + str(digits[1]) + str(digits[2])
          #      if digit_count == 4:
           #         number = str(digits[0]) + str(digits[1]) + str(digits[2]) + str(digits[3])

    #            if part1 and digit_count > 0:
     #               expression1.append(digits[-1])
      #          if part2 and digit_count > 0:
       #             expression2.append(digits[-1])
        #        if digit_count > 0:
         #           del digits[-1]
          #          digit_count -=1

                                 #deleting from screen and lists
       #         screen.fill(black)
        #        if part1 and len(expression1) == 0:
         #           equation = ""
          #          first_number = True
           #     if part1 and len(expression1) > 0:
            #        del expression1[-1]
             #       if len(expression1) == 1:
              #          equation = str(expression1[0])
               #         first_number = True
                #    if len(expression1) == 2:
                 #       equation = str(expression1[0]) + str(expression1[1])
                  #  if len(expression1) == 3:
                   #     equation = str(expression1[0]) + str(expression1[1]) + str(expression1[2])
                    #if len(expression1) == 4:
                     #   equation = str(expression1[0]) + str(expression1[1]) + str(expression1[2]) + str(expression1[3])
                    #if len(expression1) == 5:
                    #    equation = str(expression1[0]) + str(expression1[1]) + str(expression1[2]) + str(expression1[3]) + str(expression1[4])
                    #if len(expression1) == 6:
                     #   equation = str(expression1[0]) + str(expression1[1]) + str(expression1[2]) + str(expression1[3]) + str(expression1[4]) + str(expression1[5])
                        
            if event.key == pygame.K_KP_ENTER:
                #for last number
                if digit_count > 0:
                    if digit_count == 1:
                        number = digits[0]
                    if digit_count == 2:
                        number = str(digits[0]) + str(digits[1])
                    if digit_count == 3:
                        number = str(digits[0]) + str(digits[1]) + str(digits[2])
                    if digit_count == 4:
                        number = str(digits[0]) + str(digits[1]) + str(digits[2]) + str(digits[3])


                            #(for previous number)                
                    if adding and number not in multiplying_numbers2:
                        adding_numbers2.append(number)
                    if subtracting and number not in multiplying_numbers2:
                        subtracting_numbers2.append(number)
                    if multiplying:
                        multiplying_numbers2.append(number)
                    if dividing:
                        dividing_numbers2.append(number)

                    expression2.append(number)
                    digits.clear()
                    digit_count = 0

                part2 = False
                
                                                                                                                  #calculating the steps
                                                #combining like terms (if there's an x on both sides)
                if len(multiplying_numbers) > 0 and len(dividing_numbers) > 0:
                    coefficient1 = Fraction(multiplying_numbers[0], dividing_numbers[0])
                if len(multiplying_numbers2) > 0 and len(dividing_numbers2) > 0:
                    print("multiplying numbers is " + str(multiplying_numbers2[0]))
                    print(str(dividing_numbers2[0]))
                    coefficient2 = Fraction(multiplying_numbers2[0], dividing_numbers2[1])
                    simplify = True
                    if multiply_by_negative2 is False:
                        simplified_coefficient = coefficient1 - coefficient2
                    if multiply_by_negative2:
                        simplified_coefficient = coefficient1 + coefficient2

                #expression2.remove("x")
     #           if "*" in expression2:
     #               expression2.remove(multiplying_numbers2[0])
     #               expression2.remove("*")
     #           if "/" in expression2:
      #              expression2.remove(dividing_numbers2[0])
       #             expression2.remove("/")
        #        if multiply_by_negative2:
         #           expression2.remove("-")
          #      if "+" in expression2:
           #         expression2.remove("+")
            #    if "-" in expression2:
             #       expression2.remove("-")

            #    expression2.remove("+")
             #   expression2.remove("x")
              #  expression2.remove("4")
               # expression2.remove("/")
                #expression2.remove("2")

                answer = int(expression2[0])

                if simplify:
                    if multiply_by_negative2 is False:
                        step0 = "subtract " + str(coefficient2) + "x from both sides   ----> " + str(simplified_coefficient) + "x = " + str(answer)  
                    if multiply_by_negative2:
                        step0 = "add " + str(coefficient2) + "x to both sides"   
                    step_zero = True
                    step_four = True
                    step_five = True
              #  print("starting answer is " + str(answer))
                
                if len(adding_numbers) > 0:
                    answer -= int(adding_numbers[0])
                    step1 = "subtract both sides by " + str(adding_numbers[0]) + "        ---->   " + str(round_half_up(answer, 3))
                    step_one = True
                if len(subtracting_numbers) > 0:
                    answer += int(subtracting_numbers[0])
                    step2 = "add " + str(subtracting_numbers[0]) + " to both sides          ---->   " + str(round_half_up(answer, 3))
                    step_two = True
                if multiply_by_negative:
                    answer *= -1
                    step3 = "multiply both sides by negative one   ---->  " + str(round_half_up(answer))
                    step_three = True
                if len(multiplying_numbers) > 0:
                    if simplify:
                        step4 = "divide both sides by " + str(simplified_coefficient) + "     ---->   " + str(round_half_up(answer, 3))
                    if not simplify and multiplying_numbers[0] != 1:
                        answer /= int(multiplying_numbers[0])
                        step4 = "divide both sides by " + str(multiplying_numbers[0]) + "     ---->   " + str(round_half_up(answer, 3))
                    step_four = True
                if len(dividing_numbers) > 0 and simplify is False:
                    answer *= int(dividing_numbers[0])
                    if dividing_numbers[0] != 1:
                        step5 = "multiply both sides by " + str(dividing_numbers[0]) + "     ---->   " + str(round_half_up(answer, 3))
                        step_five = True
                  
                                                          #combining steps 
                    #multiply/divide by negative number
                if step_three and step_four and step_five is False:
                    step_three = False
                    step4 = "divide both sides by -" + str(multiplying_numbers[0]) + "     ---->   " + str(round_half_up(answer, 3))
                if step_three and step_four and dividing_numbers[0] == 1:
                    step_three = False
                    step4 = "divide both sides by -" + str(multiplying_numbers[0]) + "     ---->   " + str(round_half_up(answer, 3))
                if step_three and step_five is True and step_four is False:
                    step_three = False
                    step5 = "multiply both sides by -" + str(dividing_numbers[0]) + "     ---->   " + str(round_half_up(answer, 3))
                if step_three and step_five and multiplying_numbers[0] == 1:
                    step_three = False
                    step5 = "multiply both sides by -" + str(dividing_numbers[0]) + "     ---->   " + str(round_half_up(answer, 3))
                    #fraction
                if step_four and step_five and dividing_numbers[0] != 1 and multiplying_numbers[0] != 1 and step_three is False:
                    if simplify is False:         
                        step4 = "multiply both sides by " + str(dividing_numbers[0]) + "/" + str(multiplying_numbers[0]) + "     ---->   " + str(round_half_up(answer))
                    if simplify:
                        answer /= simplified_coefficient
                        print("simplified coefficient is " + str(simplified_coefficient))
                        step4 = "divide both sides by " + str(simplified_coefficient) + "     ---->   " + str(round_half_up(answer))
                    step_five = False
                if step_three and step_four and step_five and dividing_numbers[0] != 1 and multiplying_numbers[0] != 1:
                    step_three = False
                    step_five = False
                    step4 = "multiply both sides by -" + str(dividing_numbers[0]) + "/" + str(multiplying_numbers[0]) + "     ---->   " + str(round_half_up(answer))
                            #exponents
                if len(exponents) > 0:
                    answer = pow(answer, (1/int(exponents[0])))
                    if exponents[0] % 1 == 0 and exponents[0] != 2 and exponents[0] != 3:
                        step6 = "raise both sides to the power of 1/" + str(exponents[0]) + "     ---->   " + str(round_half_up(answer, 3))
                    if exponents[0] == 2:
                        step6 = "square root both side        ---->  " + str(round_half_up(answer))
                    if exponents[0] == 3:
                        step6 = "cube root both side        ---->  " + str(round_half_up(answer))
                    step_six = True  
                
                                                                            
                                                                            #for the part in the parenthesis
                if len(adding_numbers_in_parenthesis) > 0:
                    answer -= int(adding_numbers_in_parenthesis[0])
                    step1_v2 = "subtract both sides by " + str(adding_numbers_in_parenthesis[0]) + "        ---->   " + str(round_half_up(answer, 3))
                    step_one_v2 = True
                if len(subtracting_numbers_in_parenthesis) > 0:
                    answer += int(subtracting_numbers_in_parenthesis[-1])
                    step2_v2 = "add " + str(subtracting_numbers_in_parenthesis[-1]) + " to both sides          ---->   " + str(round_half_up(answer, 3))
                    step_two_v2 = True
                if multiply_by_negative_in_parenthesis:
                    answer *= -1
                    step3_v2 = "multiply both sides by negative one   ---->  " + str(round_half_up(answer))
                    step_three_v2 = True
                if len(multiplying_numbers_in_parenthesis) > 0 and multiplying_numbers_in_parenthesis[0] != 1:
                    answer /= int(multiplying_numbers_in_parenthesis[0])
                    step4_v2 = "divide both sides by " + str(multiplying_numbers_in_parenthesis[0]) + "     ---->   " + str(round_half_up(answer, 3))
                    step_four_v2 = True
                if len(dividing_numbers_in_parenthesis) > 0:
                    answer *= int(dividing_numbers_in_parenthesis[0])
                    if dividing_numbers_in_parenthesis[0] != 1:
                        step5_v2 = "multiply both sides by " + str(dividing_numbers_in_parenthesis[0]) + "     ---->   " + str(round_half_up(answer, 3))
                        step_five_v2 = True
                  
                                                          #combining steps 
                    #multiply/divide by negative number
                if step_three_v2 and step_four_v2 and step_five_v2 is False and there_is_parenthesis:
                    step_three_v2 = False
                    step4_v2 = "divide both sides by -" + str(multiplying_numbers_in_parenthesis[0]) + "     ---->   " + str(round_half_up(answer, 3))
                if step_three_v2 and step_four_v2 and dividing_numbers_in_parenthesis[0] == 1 and there_is_parenthesis:
                    step_three_v2 = False
                    step4_v2 = "divide both sides by -" + str(multiplying_numbers_in_parenthesis[0]) + "     ---->   " + str(round_half_up(answer, 3))
                if step_three_v2 and step_five_v2 is True and step_four_v2 is False and there_is_parenthesis:
                    step_three_v2 = False
                    step5_v2 = "multiply both sides by -" + str(dividing_numbers_in_parenthesis[0]) + "     ---->   " + str(round_half_up(answer, 3))
                if step_three_v2 and step_five_v2 and multiplying_numbers_in_parenthesis[0] == 1 and there_is_parenthesis:
                    step_three_v2 = False
                    step5_v2 = "multiply both sides by -" + str(dividing_numbers_in_parenthesis[0]) + "     ---->   " + str(round_half_up(answer, 3))
                    #fraction
                if step_four_v2 and step_five_v2 and step_three_v2 is False and there_is_parenthesis:
                    if dividing_numbers_in_parenthesis[0] != 1 and multiplying_numbers_in_parenthesis[0] != 1:
                        step_five_v2 = False
                        step4_v2 = "multiply both sides by " + str(dividing_numbers_in_parenthesis[0]) + "/" + str(multiplying_numbers_in_parenthesis[0]) + "     ---->   " + str(round_half_up(answer, 3))
                if step_three_v2 and step_four_v2 and step_five_v2 and there_is_parenthesis:
                    if dividing_numbers_in_parenthesis[0] != 1 and multiplying_numbers_in_parenthesis[0] != 1:
                        step_three_v2 = False
                        step_five_v2 = False
                        step4_v2 = "multiply both sides by -" + str(dividing_numbers_in_parenthesis[0]) + "/" + str(multiplying_numbers_in_parenthesis[0]) + "     ---->   " + str(round_half_up(answer, 3))
                            #exponents
                if len(exponents_in_parenthesis) > 0 and there_is_parenthesis:
                    answer = pow(answer, (1/int(exponents_in_parenthesis[0])))
                    if exponents_in_parenthesis[0] % 1 == 0 and exponents_in_parenthesis[0] != 2 and exponents_in_parenthesis[0] != 3:
                        step6_v2 = "raise both sides to the power of 1/" + str(exponents_in_parenthesis[0]) + "     ---->   " + str(round_half_up(answer, 3))
                    if exponents_in_parenthesis[0] == 2:
                        step6_v2 = "square root both side        ---->  " + str(round_half_up(answer, 3))
                    if exponents_in_parenthesis[0] == 3:
                        step6_v2 = "cube root both side        ---->  " + str(round_half_up(answer, 3))
                    step_six_v2 = True  



                run = False
                second_screen = True
                pygame.display.set_mode()
                screen = pygame.display.set_mode((1800, 1000), pygame.FULLSCREEN)
              #to restart program
            if event.key == pygame.K_r:
                screen.fill(black)
                added_number = False
                digits.clear()
                part1 = True
                part2 = False
                expression1.clear()
                expression2.clear()
                digit_count = 0
                equation = ""
                adding = False
                subtracting = False
                multiplying = False
                dividing = False
                exponentiating = False
                multiply_by_negative = False
                adding_numbers.clear()
                subtracting_numbers.clear()
                multiplying_numbers.clear()
                dividing_numbers.clear()
                exponents.clear()
                multiply_by_negative2 = False
                adding_numbers2.clear()
                subtracting_numbers2.clear()
                multiplying_numbers2.clear()
                dividing_numbers2.clear()
                exponents2.clear()
                first_number = True
                step_one = False
                step_two = False
                step_three = False
                step_four = False
                step_five = False
                pygame.display.update()
        if event.type == pygame.QUIT:
            run = False  
    if run:
        show_equation(300, 800)
    pygame.display.update()
                                                #setting up for screen showing steps
step_list = []
num_of_steps = 0
if step_zero:
    step_list.append(step0)
    num_of_steps += 1
if step_one:
    step_list.append(step1)
    num_of_steps += 1
if step_two:
    step_list.append(step2)
    num_of_steps += 1
if step_three:
    step_list.append(step3)
    num_of_steps += 1
if step_four:
    step_list.append(step4)
    num_of_steps += 1
if step_five:
    step_list.append(step5)
    num_of_steps += 1
if step_six:
    step_list.append(step6)
    num_of_steps += 1
                #if there is parenthesis
if step_one_v2:
    step_list.append(step1_v2)
    num_of_steps += 1
if step_two_v2:
    step_list.append(step2_v2)
    num_of_steps += 1
if step_three_v2:
    step_list.append(step3_v2)
    num_of_steps += 1
if step_four_v2:
    step_list.append(step4_v2)
    num_of_steps += 1
if step_five_v2:
    step_list.append(step5_v2)
    num_of_steps += 1
if step_six_v2:
    step_list.append(step6_v2)
    num_of_steps += 1


if num_of_steps == 1:
    steps = str(step_list[0])

if num_of_steps == 2:
    steps = (str(step_list[0]) + str(step_list[1]))

if num_of_steps == 3:
    steps = str(step_list[0]) + str(step_list[1]) + str(step_list[2])

if num_of_steps == 4:
    steps = str(step_list[0]) + str(step_list[1]) + str(step_list[2]) + str(step_list[3])

if num_of_steps == 5:
    steps = str(step_list[0]) + str(step_list[1]) + str(step_list[2]) + str(step_list[3]) + str(step_list[4])

if num_of_steps == 6:
    steps = str(step_list[0]) + str(step_list[1]) + str(step_list[2]) + str(step_list[3]) + str(step_list[4]) + str(step_list[5])

if num_of_steps == 7:
    steps = str(step_list[0]) + str(step_list[1]) + str(step_list[2]) + str(step_list[3]) + str(step_list[4]) + str(step_list[5]) + str(step_list[6])

if num_of_steps == 8:
    steps = str(step_list[0]) + str(step_list[1]) + str(step_list[2]) + str(step_list[3]) + str(step_list[4]) + str(step_list[5]) + str(step_list[6]) + str(step_list[7])

#if num_of_steps == 9:
 #   steps = str(step_list[0]) + str(step_list[1]) + str(step_list[2]) + str(step_list[3]) + str(step_list[4]) + str(step_list[5]) + str(step_list[6]) + str(step_list[7]) + str(step_list[8])

#if num_of_steps == 10:
 #   steps = str(step_list[0]) + str(step_list[1]) + str(step_list[2]) + str(step_list[3]) + str(step_list[4]) + str(step_list[5]) + str(step_list[6]) + str(step_list[7]) + str(step_list[8]) + str(step_list[9])

if num_of_steps == 1:
    def show_line1(x, y):
        show_line1 = font.render(("Step #1:  " + step_list[0]), True, red)
        screen.blit(show_line1, (x, y)) 
if num_of_steps == 2:
    def show_line1(x, y):
        show_line1 = font.render(("Step #1:  " + step_list[0]), True, red)
        screen.blit(show_line1, (x, y)) 
    def show_line2(x, y):
        show_line2 = font.render(("Step #2:  " + step_list[1]), True, red)
        screen.blit(show_line2, (x, y)) 
if num_of_steps == 3:
    def show_line1(x, y):
        show_line1 = font.render(("Step #1:  " + step_list[0]), True, red)
        screen.blit(show_line1, (x, y)) 
    def show_line2(x, y):
        show_line2 = font.render(("Step #2:  " + step_list[1]), True, red)
        screen.blit(show_line2, (x, y)) 
    def show_line3(x, y):
        show_line3 = font.render(("Step #3:  " + step_list[2]), True, red)
        screen.blit(show_line3, (x, y)) 
if num_of_steps == 4:
    def show_line1(x, y):
        show_line1 = font.render(("Step #1:  " + step_list[0]), True, red)
        screen.blit(show_line1, (x, y))  
    def show_line2(x, y):
        show_line2 = font.render(("Step #2:  " + step_list[1]), True, red)
        screen.blit(show_line2, (x, y)) 
    def show_line3(x, y):
        show_line3 = font.render(("Step #3:  " + step_list[2]), True, red)
        screen.blit(show_line3, (x, y)) 
    def show_line4(x, y):
        show_line4 = font.render(("Step #4:  " + step_list[3]), True, red)
        screen.blit(show_line4, (x, y)) 
if num_of_steps == 5:
    def show_line1(x, y):
        show_line1 = font.render(("Step #1:  " + step_list[0]), True, red)
        screen.blit(show_line1, (x, y))  
    def show_line2(x, y):
        show_line2 = font.render(("Step #2:  " + step_list[1]), True, red)
        screen.blit(show_line2, (x, y)) 
    def show_line3(x, y):
        show_line3 = font.render(("Step #3:  " + step_list[2]), True, red)
        screen.blit(show_line3, (x, y)) 
    def show_line4(x, y):
        show_line4 = font.render(("Step #4:  " + step_list[3]), True, red)
        screen.blit(show_line4, (x, y)) 
    def show_line5(x, y):
        show_line5 = font.render(("Step #5:  " + step_list[4]), True, red)
        screen.blit(show_line5, (x, y)) 
if num_of_steps == 6:
    def show_line1(x, y):
        show_line1 = font.render(("Step #1:  " + step_list[0]), True, red)
        screen.blit(show_line1, (x, y))  
    def show_line2(x, y):
        show_line2 = font.render(("Step #2:  " + step_list[1]), True, red)
        screen.blit(show_line2, (x, y)) 
    def show_line3(x, y):
        show_line3 = font.render(("Step #3:  " + step_list[2]), True, red)
        screen.blit(show_line3, (x, y)) 
    def show_line4(x, y):
        show_line4 = font.render(("Step #4:  " + step_list[3]), True, red)
        screen.blit(show_line4, (x, y)) 
    def show_line5(x, y):
        show_line5 = font.render(("Step #5:  " + step_list[4]), True, red)
        screen.blit(show_line5, (x, y)) 
    def show_line6(x, y):
        show_line6 = font.render(("Step #6:  " + step_list[5]), True, red)
        screen.blit(show_line6, (x, y)) 
#if num_of_steps == 7:
 #   def show_line1(x, y):
  #      show_line1 = font.render(("Step #1:  " + step_list[0]), True, red)
   #     screen.blit(show_line1, (x, y))  
   # def show_line2(x, y):
   #     show_line2 = font.render(("Step #2:  " + step_list[1]), True, red)
   #     screen.blit(show_line2, (x, y)) 
   # def show_line3(x, y):
   #     show_line3 = font.render(("Step #3:  " + step_list[2]), True, red)
   #     screen.blit(show_line3, (x, y)) 
   # def show_line4(x, y):
   #     show_line4 = font.render(("Step #4:  " + step_list[3]), True, red)
   #     screen.blit(show_line4, (x, y)) 
    #def show_line5(x, y):
     #   show_line5 = font.render(("Step #5:  " + step_list[4]), True, red)
      #  screen.blit(show_line5, (x, y)) 
    #def show_line6(x, y):
     #   show_line6 = font.render(("Step #6:  " + step_list[5]), True, red)
      #  screen.blit(show_line6, (x, y)) 
 #   def show_line7(x, y):
  #      show_line7 = font.render(("Step #7:  " + step_list[6]), True, red)
   #     screen.blit(show_line7, (x, y)) 

def show_initial_equation(x, y):
    show_initial_equation = font.render(("Initial Equation: " + str(equation)), True, red)
    screen.blit(show_initial_equation, (x, y)) 


                                                                                    #displaying steps/answer on new screen
while second_screen:
    show_initial_equation(420, 40)
    if num_of_steps == 1:
        show_line1(50, 150)
        show_answer(800, 300)
    if num_of_steps == 2:
        show_line1(50, 150)
        show_line2(50, 300)
        show_answer(800, 450)
    if num_of_steps == 3:
        show_line1(50, 150)
        show_line2(50, 300)
        show_line3(50, 450)
        show_answer(800, 600)
    if num_of_steps == 4:
        show_line1(50, 150)
        show_line2(50, 300)
        show_line3(50, 450)
        show_line4(50, 600)
        show_answer(800, 750)
    if num_of_steps == 5:
        show_line1(50, 150)
        show_line2(50, 300)
        show_line3(50, 450)
        show_line4(50, 600)
        show_line5(50, 750)
        show_answer(800, 850)
    if num_of_steps == 6:
        show_line1(50, 150)
        show_line2(50, 300)
        show_line3(50, 450)
        show_line4(50, 600)
        show_line5(50, 750)
        show_line6(50, 850)
        show_answer(800, 920)
    pygame.display.update()




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            second_screen = False  
