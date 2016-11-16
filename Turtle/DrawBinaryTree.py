'''
Created on Nov 16, 2016

@author: menon
'''
import turtle 
'''
This recursive function draw a binary tree. 
To understand recursion you have to first understand recursion :D
''' 
def binaryTree(branch_length_of_tree, tree):
    
    if branch_length_of_tree > 5:
        
        if branch_length_of_tree <= 30:
            tree.pencolor("#4B8531") # this give last two branch green color :) 
        else:
            tree.pencolor("#5E5D24")
        
        tree.pensize(branch_length_of_tree / 7) # resize our pen size
        
        tree.forward(branch_length_of_tree)
        tree.right(30)
        
        binaryTree(branch_length_of_tree - 10, tree) # build right subtree
        
        tree.left(60)
        
        binaryTree(branch_length_of_tree - 10, tree) # build left subtree 
        
        # fix the correct position and back to the root of subtree 
        tree.right(30)
        tree.penup()
        tree.backward(branch_length_of_tree) 
        tree.pendown()

def main():
    
    tree = turtle.Turtle() # create a turtle object
    main_window = turtle.Screen() # create screen 
    
    main_window.bgcolor('#292929') # change window background color
    
    
    # set our turtle object to a correct position
    tree.left(90)
    tree.penup()
    tree.backward(250)
    tree.pendown()
    tree.speed(0) # set turtle speed, 0 = high speed
    
    binaryTree(85, tree) # draw entire tree
    
    # draw base part of our tree :) 
    tree.color("#253502")
    tree.begin_fill()
    tree.goto(-100, -300)
    tree.goto(100, -300)
    tree.goto(0, -250)
    tree.end_fill()
    tree.shapesize(1, 1, 8)
    
    '''
    # draw base part of tree
    tree.pencolor("#476730")
    #tree.shape("circle")
    tree.shape("triangle")
    tree.fillcolor("#476730")
    tree.shapesize(7, 3, 1)
    '''
    
    turtle.done()
    
# Everything is done. Now just run the program 
main() 
