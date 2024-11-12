'''
schelling_objects.py

Dec 2022

This program has classes that are used in the main file to create the different objects and scenes in the window.
The first class object is Person which is inherited by the classes Red and Blue which show the population race type.
The classes Red and Blue are represented in the window as a red square and a blue square. The class Line draws a line 
the window given from the starting point to the last point given as an argument. The class Arrow inherits the fields
and methods from the Line class but adds an arrow to the last point given. The class DataPoint refers to a green point
/a small circle/ drawn onto the screen. The class Text creates a text on to the screen. The class SubmitButton is creates
a rectangle box with a text inside and waits till the user clicks the button. And runs the onclick function if there is 
a onclick field filled or else just returns None and moves on to the next line of code. The class Input has both a text
and entry object. The text is place before the the entry box. Overall, this file serves as a library for the main file.
'''

# importing packages
import graphicsPlus as gr


class Person:
    '''Creates a person object which is shown as a square that has the necessary attributes and Methods for the main file'''

    def __init__(self, win, the_type, px, py, dx = 1, dy = 1):
        '''Constructor function to initialize the fields'''

        # assignment of the default values for the class object
        self.win = win
        self.type = the_type
        self.pos = [px, py]
        self.width = dx
        self.height = dy
        self.scale = 10
        self.happiness = False


    def getPosition(self):
        '''Returns the position of the object as a tuple'''

        return tuple(self.pos)


    def getWidth(self):
        '''Returns the width of the object visualized'''
        dx = self.width
        return dx


    def getHeight(self):
        '''Returns the height of the object visualized'''
        dy = self.height
        return dy


    def getHappiness(self):
        '''Returns the boolean value of whether the person is happy or not'''
        happy  = self.happiness
        return happy


    def getType(self):
        '''Returns the type field'''
        person_type = self.type
        return person_type


    def setType(self, the_type):
        '''Sets the type/race of the person to the field'''
        self.type = the_type


    def setPosition(self, px, py):
        '''Sets the position of the person to the new position given as parameters'''

        # gets the old positions of the objects and assigns them to local variables
        oldPosX = self.pos[0]
        oldPosY = self.pos[1]

        # the change in both the x and y direction fixed to scale 
        dx = (px - oldPosX) * self.scale
        dy = (py - oldPosY) * -self.scale

        # move the object to the new position
        self.vis.move(dx, dy)

        # updates the position field to the new position given
        self.pos = [px, py]


    def setHappiness(self, val):
        '''Sets the happiness field to the boolean value'''
        self.happiness = val


class Red(Person):
    '''Inherits the class Person and creates a person of type "red" and draws a red square on to the window'''

    def __init__(self, win, px, py, dx=1, dy=1):
        '''Constructor function'''

        # links with the parent cass assigning the type to red
        Person.__init__(self, win, 'red', px, py, dx, dy)
        # draws the object
        self.draw()


    def draw(self):
        '''Draws the object on to the window'''

        # creates the visualized object, which is a square
        self.vis = gr.Rectangle(gr.Point((self.pos[0]-self.width/2)*self.scale, self.win.getHeight()-(self.pos[1]-self.height/2)*self.scale), gr.Point((self.pos[0]+self.width/2)*self.scale, self.win.getHeight() - (self.pos[1] + self.height/2)*self.scale))
        # fills the color red for the square
        self.vis.setFill('red')
        # draws the object to the window
        self.vis.draw(self.win)


    def undraw(self):
        '''Undraws the object from the window'''
        self.vis.undraw()


class Blue(Person):
    '''Inherits the class Person and creates a person of type "blue" and draws a blue square on to the window given'''
    
    def __init__(self, win, px, py, dx=1, dy=1):
        '''Constructor function'''

        # links with the parent cass assigning the type to blue
        Person.__init__(self, win, 'blue', px, py, dx, dy)
        # draws the object
        self.draw()


    def draw(self):
        '''Draws the object on to the window'''

        # creates the visualized object, which is a square
        self.vis = gr.Rectangle(gr.Point((self.pos[0]-self.width/2)*self.scale, self.win.getHeight()-(self.pos[1]-self.height/2)*self.scale), gr.Point((self.pos[0]+self.width/2)*self.scale, self.win.getHeight() - (self.pos[1] + self.height/2)*self.scale))
        # fills the color blue for the square
        self.vis.setFill('blue')
        # draws the object to the window
        self.vis.draw(self.win)


    def undraw(self):
        '''Undraws the object from the window'''
        self.vis.undraw()


class Line:
    '''Creates a Line object which is shown as a line with the initial point and last point given as an argument and draws the line on to the window'''

    def __init__(self, win, p1, p2):
        '''Constructor function'''

        # assignment of the fields 
        self.win = win
        self.scale = 10
        self.p1 = gr.Point(p1[0]*self.scale, win.getHeight() - p1[1]*self.scale)
        self.p2 = gr.Point(p2[0]*self.scale, win.getHeight() - p2[1]*self.scale)
        # draws the object
        self.draw()


    def draw(self):
        '''Draws the object on to the window'''

        # creates the visualization field and assigns it to the field self.vis
        self.vis = gr.Line(self.p1, self.p2)
        # draws the self.vis on to the window
        self.vis.draw(self.win)


    def undraw(self):
        '''Undraws the object'''
        self.vis.undraw()


class Arrow(Line):
    '''Inherits the Line Class and adds an arrow at the last point'''

    def __init__(self, win, p1, p2):
        '''Constructor function'''

        # links with the super/parent class with points passed in
        super().__init__(win, p1, p2)
        # calls the arrow function to add an arrow to the line
        self.arrow()


    def arrow(self):
        '''Adds an arrow at the last point for the line'''
        self.vis.setArrow('last')


class DataPoint:
    '''Creates a small circular point on to the window'''

    def __init__(self, win, px, py):
        '''Constructor Function'''

        # assignment of fields to the default values
        self.win = win
        self.pos = [px, py]
        self.scale = 10
        # draws the object on to the window
        self.draw()

    
    def draw(self):
        '''Draws the object on to the window'''

        # creates a small circular object and assigns it to the self.vis field
        self.vis = gr.Circle(gr.Point(self.pos[0]*self.scale, self.win.getHeight() - self.pos[1]*self.scale), radius=5)
        # fills the color green to the visual field
        self.vis.setFill('green1')
        # draws the object on to the window
        self.vis.draw(self.win)


    def undraw(self):
        '''Undraws the object from the window'''
        self.vis.undraw()


    def getPosition(self):
        # returns the positon of the object as a tuple
        return tuple(self.pos)


    def setPosition(self, px, py):
        '''Sets the position of the object to the position given'''

        # assigns the old position field value to a local variable
        old_pos = self.pos

        # computes the scaled change both in the x and y direction and assigns it to local variables
        dx = (px - old_pos[0])*self.scale
        dy = (py - old_pos[1])*-self.scale

        # moves the object to the new position
        self.vis.move(dx, dy)

        # updates the position value to the new position values given
        self.pos = [px, py]


class Text:
    '''Craetes a text onto the window given'''

    def __init__(self, win, text = '', px=0, py=0):
        '''Constructor function'''

        # assignment of field values to the default or given values
        self.win = win
        self.pos = [px, py]
        self.scale = 10
        self.text = text
        self.size = 10
        # calls the method draw and draws the object 
        self.draw()


    def draw(self):
        '''Draws the visual object on to the window'''

        # creates the text object and assigns it to the self.vis field
        self.vis = gr.Text(gr.Point(self.scale*self.pos[0], self.win.getHeight()-self.pos[1]*self.scale), text=self.text)
        # draws the text on to the window
        self.vis.draw(self.win)


    def undraw(self):
        '''Undraws the object from the window'''
        self.vis.undraw()


    def getPosition(self):
        '''Returns the position of the object as a tuple'''
        return tuple(self.pos)


    def setPosition(self, px, py):
        '''Sets the position of the object to the position given'''

        # assigns the old position field value to a local variable
        old_pos = self.pos

        # computes the scaled change both in the x and y direction and assigns it to local variables
        dx = (px - old_pos[0])*self.scale
        dy = (py - old_pos[1])*-self.scale

        # moves the object to the new position
        self.vis.move(dx, dy)

        # updates the position value to the new position values given
        self.pos = [px, py]


    def setSize(self, s):
        '''Sets the size of the text'''
        self.size = s
        self.vis.setSize(s)


class Input:
    '''Creates an entry box with a text appearing before the entry box on to the window in the position given'''

    def __init__(self, win, px, py, size = 10, text=''):
        '''Contructor Function'''

        # assignment of the fields to default or assigned values
        self.win = win
        self.pos = [px, py]
        self.text = text
        self.scale = 10
        self.size = size

        # calls the draw method and draws the object
        self.draw()


    def draw(self):
        '''Draws the object on to the window'''

        # creates a list containg a text object and an entry object in their respective positions and assigns it to the self.vis field
        self.vis = [gr.Entry(gr.Point((self.pos[0]+10)*self.scale, self.win.getHeight()-self.pos[1]*self.scale), 22), gr.Text(gr.Point(self.scale*(self.pos[0]-10), self.win.getHeight()-self.pos[1]*self.scale), text=self.text)]
        # sets the size of the text to 15
        self.vis[1].setSize(15)

        for items in self.vis:
            # loops through each item inside the self.vis list and moves them to the new position
            items.draw(self.win)


    def undraw(self):
        '''Undraws each item in the self.vis field'''
        for items in self.vis:
            # loops through the self.vis field and undraws
            items.undraw()


    def getSize(self):
        '''Returns the size of the text appearing before the text object'''
        size = self.size
        return size


    def setSize(self, size):
        '''Returns the size fo the text'''
        self.vis[1].setSize(size)


    def getPositon(self):
        '''Returns the position of the object as a tuple'''
        return tuple(self.pos)


    def setPosiiton(self, px, py):
        '''Sets the position of the object to the new position given'''

        # assigns the old position field value to a local variable
        old_pos = self.pos

        # computes the scaled change both in the x and y direction and assigns it to local variables
        dx = (px - old_pos[0])*self.scale
        dy = (py - old_pos[1])*-self.scale

        for item in self.vis:
            # loops through the self.vis and moves each item to the new position given
            item.move(dx, dy)

        # updates the position value to the new position values given
        self.pos = [px, py]


    def getText(self):
        '''Gets and returns the text enetered inside the entry box'''

        # gets the text entered inside the entry box and assigns it to a local variable
        text = self.vis[0].getText()
        # returns the text
        return text


    def setText(self, string):
        '''Sets the text for the text object appearing before the entry box/not inside the entry box/'''

        self.vis[1].setText(string)


class SubmitButton:
    '''Creates a button with a text inside the rectangular box on to the window in the position given'''

    def __init__(self, win, px, py, onclick='', width = 10, height = 3, button_text = 'Submit', color = 'Blue', size =25):
        '''Constructor Function'''

        # assignment of fields to default or assigned values
        self.win = win
        self.pos = [px, py]
        self.onclick = onclick
        self.width = width
        self.height = height
        self.color = color
        self.button_text = button_text
        self.scale = 10
        self.size = size

        # draws the object by the calling the method draw()
        self.draw()


    def draw(self):
        '''Draws the object on to the window'''

        # creates a list containg a text object and a rectnagular object in their respective positions and assigns it to the self.vis field
        self.vis = [gr.Rectangle(gr.Point((self.pos[0]-self.width/2)*self.scale, self.win.getHeight()-(self.pos[1]-self.height/2)*self.scale), gr.Point((self.pos[0]+self.width/2)*self.scale, self.win.getHeight() - (self.pos[1] + self.height/2)*self.scale)), gr.Text(gr.Point(self.pos[0]*self.scale, self.win.getHeight()-self.pos[1]*self.scale), text=self.button_text)]

        # fills the color of the rectangular box to the self.color field
        self.vis[0].setFill(self.color)
        # sets the size of the text inside the box
        self.vis[1].setSize(self.size)
        # sets the color of the text inside the box
        self.vis[1].setFill('white')

        for items in self.vis:
            # loops through the self.vis list and draws each item on to the window
            items.draw(self.win)


    def undraw(self):
        '''Undraws the object from the window'''

        for items in self.vis:
            # loops through the self.vis list and undraws each item from the window
            items.undraw()


    def getPositon(self):
        '''Returns the position of the object as a tuple'''
        return tuple(self.pos)


    def setPosiiton(self, px, py):
        '''Sets the position of the object to the new position given'''

        # assigns the old position field value to a local variable
        old_pos = self.pos

        # computes the scaled change both in the x and y direction and assigns it to local variables
        dx = (px - old_pos[0])*self.scale
        dy = (py - old_pos[1])*-self.scale

        for items in self.vis:
            # loops through the self.vis and moves each item to the new position given
            items.move(dx, dy)

        # updates the position value to the new position values given
        self.pos = [px, py]


    def setOnClick(self, onclick):
        '''Sets the onclick field to the new value given'''
        self.onclick = onclick


    def getClick(self):
        '''Waits for the user to click the button and runs the self.onlclick value if given'''

        # waits and gets the position of the mouse click inside the window
        clickPoint = self.win.getMouse()

        # converts the position to scale and assigns it to local variables
        x_pos = clickPoint.getX()/self.scale
        y_pos = (self.win.getHeight() - clickPoint.getY())/self.scale

        if x_pos >= self.pos[0]-self.width/2 and x_pos <= self.pos[0]+self.width/2 and y_pos >= self.pos[1]-self.height/2 and y_pos <= self.pos[1]+self.height/2:
            # checks if the click is inside the rectangular box and if so, returns and runs the self.onclick value
            return self.onclick

        else:
            # if the click is not inside the button area then recurses/reruns the method function to get the click.
            self.getClick()



        






       

    




    
