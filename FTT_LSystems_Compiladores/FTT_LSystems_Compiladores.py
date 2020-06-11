
import turtle
from Grammar import Grammar
import canvasvg

SYSTEM_RULES = {} 


def derivation(axiom, steps):
    derived = [axiom]  
    for _ in range(int(steps)):
        next_seq = derived[-1]
        next_axiom = [rule(char) for char in next_seq]
        derived.append(''.join(next_axiom))
    return derived


def rule(sequence):
    if sequence in SYSTEM_RULES:
        return SYSTEM_RULES[sequence]
    return sequence


def draw_l_system(turtle, SYSTEM_RULES, seg_length, angle,alphabet):
    stack = []
    for command in SYSTEM_RULES:
        turtle.pd()
        if command in alphabet:
            turtle.forward(seg_length)
        elif command == "f":
            turtle.pu()
            turtle.forward(seg_length)
        elif command == "+":
            turtle.right(float(angle))
        elif command == "-":
            turtle.left(float(angle))
        elif command == "[":
            stack.append((turtle.position(), turtle.heading()))
        elif command == "]":
            turtle.pu()
            position, heading = stack.pop()
            turtle.goto(position)
            turtle.setheading(heading)


def set_turtle(alpha_zero):
    r_turtle = turtle.Turtle()
    r_turtle.screen.title("L-System Derivation")
    r_turtle.speed(0)
    r_turtle.setheading(alpha_zero) 
    return r_turtle


def main():
    rule_num = 1
    f = open("LSystemsCode.txt", "r", encoding='utf-8')
    lines = f.readlines()
    grammar = Grammar(lines) 

    for rule in grammar.rules:
        key, value = rule.split("->")
        SYSTEM_RULES[key.strip()] = value.strip()
        rule_num += 1

    axiom = grammar.axiom
    iterations = grammar.steps

    model = derivation(axiom, iterations)

    segment_length = 5
    alpha_zero = 90
    angle = grammar.angle

    r_turtle = set_turtle(alpha_zero)
    turtle_screen = turtle.Screen()
    turtle_screen.screensize(1500, 1500)
    draw_l_system(r_turtle, model[-1], segment_length, angle,grammar.alfabet)
 
    ts = turtle.getscreen().getcanvas()
    canvasvg.saveall("LSystem.svg",ts,None,10,None)

    turtle_screen.exitonclick()


if __name__ == "__main__":
    main()

