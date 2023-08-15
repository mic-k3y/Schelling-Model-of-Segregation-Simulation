'''
main.py

Michael Yilma(Mickey)
CS 152 B Fall Dec 2022
Final Project(10)

This program is the main file for my final project. It contains pretty much every function needed for the execution of the program.
When executed, it will first show the home scene by calling the function homeScene. And then after taking the necessary inputs from
the user and the user clicks submit the program will call the function initialize which will create a random data set of the population
based on the user's inputs. And after the initialize function is called, it will return a dictionary(hash map) of the population with the 
key being position of the individual values/person/ it refers to and a list containing the avaible empty space a square can move to. And 
then the simulate function will be called which will run the number of times the user wanted(taken from the input values from the home scene)
While doing that, it will also plot a graph showing the overall satisfication/happiness of the overall population. After all the simulations
are done, a button will appear below the graph. The user can click the button to save the data that shows the overall happiness of the population
after each simulation(the data of the graph). When clicked, the program will execute the function saveData, which will create and open a file 
called data.csv and save the percentage data for each simulation, and close the window.
'''

# importing packages
import graphicsPlus as gr
import random
import schelling_objects as sch


def homeScene(window):
    '''Creates the home scene for the program in the window given and returns the inputs given by the user which will later be used as 
    input parameters for the other functions'''

    # creates an empty list to later store the objects created in this function
    home_scene_objs = []

    # creates all the necessary input fields and texts for the scene and assigns them to local variables
    home_text = sch.Text(window, text='Schelling\'s Model of Segregation V1.0', px = 34.5, py=47)
    home_text.setSize(35)
    number_of_simulations= sch.Input(window, px=34.5, py=42, size=27, text='Number of Simulations:')
    red_population_percentage = sch.Input(window, px=34.5, py=37, size=27, text='Red Population Percentage in decimals:        ')
    blue_population_count = sch.Text(window, px=34.5, py=32, text='**Blue Popuation is 1 minus the Red population percentage')
    blue_population_count.setSize(15)
    free_space_percentage = sch.Input(window, px=34.5, py=27, size=27, text='Free Space Percentage in decimals: ')
    red_intolerance_toward_blue = sch.Input(window, px=34.5, py= 22, size=27, text='Red Intolerance towards Blue: ')
    blue_intolerance_toward_red = sch.Input(window, px=34.5, py= 17, size=27, text='Blue Intolerance towards Red: ')
    # creates the submit button 
    submit_button = sch.SubmitButton(window, px=34.5, py=10, button_text='Submit')

    # appends all the objects to the list home_scene_objs
    home_scene_objs.append(home_text)
    home_scene_objs.append(number_of_simulations)
    home_scene_objs.append(red_population_percentage)
    home_scene_objs.append(blue_population_count)
    home_scene_objs.append(free_space_percentage)
    home_scene_objs.append(red_intolerance_toward_blue)
    home_scene_objs.append(blue_intolerance_toward_red)
    home_scene_objs.append(submit_button)

    # waits for the user to click the submit button
    submit_button.getClick()

    # initialization of dictionary later used to store the values entered by the user
    entry_inputs = {}

    # Assigns the inputs to to their respective keys in the dictionary created
    entry_inputs['Number of Simulations'] = int(number_of_simulations.getText())
    entry_inputs['Red Population Percentage'] = float(red_population_percentage.getText())
    entry_inputs['Blue Population Percentage'] = (1 - float(red_population_percentage.getText())).__round__(4)
    entry_inputs['Free Space Percentage'] = float(free_space_percentage.getText())
    entry_inputs['Red Intolerance toward Blue'] = float(red_intolerance_toward_blue.getText())
    entry_inputs['Blue Intolerance toward Red'] = float(blue_intolerance_toward_red.getText())

    for obj in home_scene_objs:
        # iterates through each object in the list home_scene_objs and undraws them from the window
        obj.undraw()
 
    return entry_inputs


def initialize(window, input_parameters):
    '''Randomly generates data based on the user's inputs and returns the dictionary containing the 
    population with the keys being the position of the individuals and a list containing a empty space positions the squares can move to
    And also plots a graph to show the overall satisfication/happiness of the population'''

    # initiailize the dictionary and the list to be returned later on
    data_pos = {}
    empty_spaces = []

    # assign the input parameters values to local variables
    num_of_sim = input_parameters['Number of Simulations']
    blue_pop_percentage = input_parameters['Blue Population Percentage']
    red_pop_percentage = input_parameters['Red Population Percentage']
    free_space = input_parameters['Free Space Percentage']
    red_intolerance_toward_blue = input_parameters['Red Intolerance toward Blue']
    blue_intolerance_toward_red = input_parameters['Blue Intolerance toward Red']

    # Creates texts down the window to show what the user input values were for each entry box
    num_sim_text = sch.Text(window, text=f'Number of Simulations: {num_of_sim}', px=16, py=15)
    blue_pop_text = sch.Text(window, text=f'Blue Population Percentage: {blue_pop_percentage}', px=16, py=13)
    red_pop_text = sch.Text(window, text=f'Red Population Percentage: {red_pop_percentage}', px=16, py=11)
    free_space_perc_text = sch.Text(window, text=f'Free Space Percentage: {free_space}', px=16, py=9)
    red_intolerance = sch.Text(window, text=f'Red Intolerance toward Blue: {red_intolerance_toward_blue}', px=16, py=7)
    blue_intolerance = sch.Text(window, text=f'Blue Intolerance toward Red: {blue_intolerance_toward_red}', px=16, py=5)

    # creates a line boundary between the graph and the simulation space
    vertical_bounary = sch.Line(window, [33, 19], [33, 51])
    # creates a line boundary between the simulation space and the texts below the simulation space
    horizontal_bounary = sch.Line(window, [0, 19], [33, 19])

    # creates an arrow lines(both horizontal and vertical) for the graph
    vertical_arrow = sch.Arrow(window, [37, 22], [37, 49.5])
    horizontal_arrow = sch.Arrow(window, [37, 22], [66.5, 22])

    # writes the text for to show what the axis for the graph represent
    simulations_text = sch.Text(window, text='Number of Simulations', px = 51, py = 19)
    overall_happiness_text = sch.Text(window, text='Population Happiness Percentage', px = 45, py = 50.5)

    for i in range(4):
        # loops four times to draw ticks for the verical line  axis for the graph

        # creates a small horizontal line similar to a tick on the vertical line axis
        vertical_axis_tick = sch.Line(window, [36.5, 22+((i+1)/4)*26], [37.5, 22+((i+1)/4)*26])
        # writes what the number is for that tick, in this case 0.25, 0.5, 0.75, 1 
        tick_text = sch.Text(window, text=str((i+1)/4), px=35, py=22+((i+1)/4)*26)


    for i in range(1, 33):
        # loops 32 times
        for j in range(1, 33):
            # loops 32 times, totaling around 1024 loops when both loops combined, meaning this will create a 32 x 32 simulation space

            if random.random() <= 1-free_space:
                # checks if the probability to create a square instead of jumping the space 

                if random.random() <= red_pop_percentage:
                    # if the random number is less the red_pop_percentage, then it will create a red square, or a person with type red 
                    createPerson = sch.Red(window, px = i, py = j+19, dx= 1, dy = 1)

                    # append the person to the data_pos dictionary with the key being its current position in the simulation space(one digit number)
                    data_pos[32*(i-1)+j] = [createPerson]

                else:
                    # or else that means, it will create a person with type blue 
                    createPerson = sch.Blue(window, px = i, py = j+19, dx= 1, dy = 1)

                    # append the person to the data_pos dictionary with the key being its current position in the simulation space(one digit number)
                    data_pos[32*(i-1)+j] = [createPerson]

            else:
                # if the probability of free space then it will assign a list Containg None as the first value 
                # the second and the third values(boolean values) being the compatibilty of that empty space for type red and type blue respectively
                data_pos[32*(i-1)+j] = [None, 'red: {}', 'blue: {}']

                # appends that the value of the position to the empty spaces list
                empty_spaces.append([i, j])


    return (data_pos, empty_spaces)


def checkHappiness(person, data_pos, input_parameters):
    '''Checks the happiness/satisication of the person(or of a person of type at an empty_space) and returns a boolean value'''

    # assigns the parameter values to local variables 
    red_intolerance_toward_blue = input_parameters['Red Intolerance toward Blue']
    blue_intolerance_toward_red = input_parameters['Blue Intolerance toward Red']

    if person[0] != None:
        # if the person passed in is an actual person, not an empty space

        # initialize the sum and actual neighbour_number variables
        actual_neighbour_number = 0
        # sum is the number of neighbours of the same type(race) with the person
        sum = 0

        # looks for the position/key value/ of the person and assigns it to a local variable pos
        pos = [i for i in data_pos if data_pos[i] == person][0]

        # takes the list containing the neighbours of the person and assigns it to a local variable
        neighbours = getNeighbours(person, data_pos)

        # gets the type of person and assigns it to a local variable 
        type_of_person = person[0].getType()

        for neighbour in neighbours:
            # for each neighbour
            if neighbour[0] != None:
                # checks if the neighbour is a person, not an empty space

                # if so, increments the number of neighbours by 1
                actual_neighbour_number +=1

                if type_of_person == neighbour[0].getType():
                    # if the neghbou is of the same type of the person, increments sum by 1
                    sum+=1


        if actual_neighbour_number > 0:
            # if the number of neighbours is greater than 0, calculates the happiness ratio/satisfication ratio of the person
            happiness_ratio = sum/actual_neighbour_number

        else:
            # if no neigbours, returns 'No Neigbours'
            return "No Neighbours"

        if type_of_person == 'red' and happiness_ratio > red_intolerance_toward_blue:
            # if the person if red and the happiness ratio/satisfication ratio of the person is greater than the intolerance toward Blue 

            # then assigns the happiness field of the person to True
            data_pos[pos][0].setHappiness(True)  
            # and returns True
            return True

        if type_of_person == 'blue' and happiness_ratio > blue_intolerance_toward_red:
            # if the person if red and the happiness ratio/satisfication ratio of the person is greater than the intolerance toward Blue 
            
            # then assigns the happiness field of the person to True
            data_pos[pos][0].setHappiness(True)  
            # and returns True
            return True

        # returns False otherwise 
        return False

    else:
        # if the person passed in as an argument is not person object but an empty space, then

        # takes the list containing the neighbours of the person and assigns it to a local variable
        neighbours = getNeighbours(person, data_pos)

        # initialization of some variables 
        blue_neighbours = 0 
        red_neighbours = 0
        actual_neighbour_number = 0

        for neighbour in neighbours:
            # iterates through each neighbour

            if neighbour[0] != None:
                # checks if it's person, not an empty space

                # if so, increments neighbour count by 1
                actual_neighbour_number +=1

                if neighbour[0].getType() == 'red':
                    # if the neighbour is of the type red, increments the red_neighbours count by 1
                    red_neighbours += 1

                if neighbour[0].getType() == 'blue':
                    # if the neighbour is of the type blue, increments the blue_neighbours count by 1
                    blue_neighbours += 1

        if actual_neighbour_number > 0:
            # if there are neighbours, or the cneighbour cunt iss greater than 0,

            # calculates the satisfication ratio for each type and assign them to their respective local variables 
            happiness_ratio_for_red = red_neighbours/actual_neighbour_number
            happiness_ratio_for_blue = blue_neighbours/actual_neighbour_number

        else:
            # if there are no neigbours, then the space is open for both blue and red, so the compatibility for both red and blue is True
            return [None, 'red: True', 'blue: True']

        # or else returns based on the compatibility boolean values passed in the formated strings
        return [None, f'red: {happiness_ratio_for_red>red_intolerance_toward_blue}', f'blue: {happiness_ratio_for_blue>blue_intolerance_toward_red}']


def getNeighbours(person, data_pos):
    '''Gets the Neighbours of the person(or empty space) passed in as an argument and returns a list containing all neighbours'''

    # looks for the position/key value/ of the person/empty space and assigns it to a local variable pos
    pos = [i for i in data_pos if data_pos[i] == person][0]

    if pos == 1:
        # if the person, or empty space, is on the lower left corner, then its neighbours are the following 
        neighbours = [data_pos[pos+1],
                    data_pos[pos+32], data_pos[pos+31]]

    elif pos == 32:
        # else if the person, or empty space, is on the upper left corner, then its neighbours are the following 
        neighbours = [data_pos[pos-1], 
                    data_pos[pos+32], data_pos[pos+31]]
                    
    elif pos == 993:
        # else if the person, or empty space, is on the lower right corner, then its neighbours are the following 

        neighbours = [data_pos[pos-32], data_pos[pos-31], 
                    data_pos[pos+1]]

    elif pos == 1024:
        # else if the person, or empty space, is on the upper right corner, then its neighbours are the following 
        neighbours = [data_pos[pos-32], data_pos[pos-31],
                        data_pos[pos-1]]

    elif pos  % 32 == 0:
        # else if the person, or empty space, is on the first row, then its neighbours are the following 

         neighbours = [data_pos[pos-32], data_pos[pos-31], 
                        data_pos[pos-1], 
                    data_pos[pos+32], data_pos[pos+31]]

    elif pos % 32 == 1:
        # else if the person, or empty space, is on the last row, then its neighbours are the following 

        neighbours = [data_pos[pos-32], data_pos[pos-31], 
                    data_pos[pos+1],
                    data_pos[pos+32], data_pos[pos+31]]

    elif pos < 32:
        # else if the person, or empty space, is on the first column, then its neighbours are the following 

        neighbours = [data_pos[pos-1], data_pos[pos+1],
                    data_pos[pos+32], data_pos[pos+33], data_pos[pos+31]]

    elif pos > 992:
        # else if the person, or empty space, is on the last column, then its neighbours are the following 

        neighbours = [data_pos[pos-32], data_pos[pos-31], data_pos[pos-33], 
                        data_pos[pos-1], data_pos[pos+1]]

    else:
        # else then its neigbours are the following
        neighbours = [data_pos[pos-32], data_pos[pos-31], data_pos[pos-33], 
                        data_pos[pos-1], data_pos[pos+1],
                    data_pos[pos+33], data_pos[pos+31], data_pos[pos+33]]

    # returns the list containing the neighbours
    return neighbours


def lookForSpaces(data_pos, empty_spaces, input_parameters):
    '''Returns the compatiable empty spaces for both red and blue based on the parameters'''

    # initialize the blue and red happy spaces list
    blue_happy_spaces = []
    red_happy_spaces = []

    for empty_space in empty_spaces:
        # iterates through each empty space positon in the empty_spaces list

        # gets the value in the data_pos dictionary corresponding to the empty space
        none_value = data_pos[32*(empty_space[0]-1) + empty_space[1]]

        # checks the happiness of that space and updates value of in the dictionary(updates the compatibilty boolean values)
        data_pos[32*(empty_space[0]-1) + empty_space[1]] = checkHappiness(none_value, data_pos, input_parameters)

        if data_pos[32*(empty_space[0]-1) + empty_space[1]][1] == 'red: True':
            # checks if the compatibility for a perseon of type red is True, if so appends that empty space to red_happy_space
            red_happy_spaces.append(empty_space)

        if data_pos[32*(empty_space[0]-1) + empty_space[1]][2] == 'blue: True':
            # checks if the compatibility for a perseon of type blue is True, if so appends that empty space to blue_happy_space
            blue_happy_spaces.append(empty_space)

    # returns the red_happy_spaces and blue_happy_spaces lists
    return (red_happy_spaces, blue_happy_spaces)


def simulateOnce(data_pos, empty_spaces, input_parameters):
    '''Simulates the simulation space once and return the overall happiness percentage of the population after the simulation'''

    for person in data_pos.values():
        # loops through each object in the data set
        if person[0] != None:
            # checks if the that object is a person not an empty space

            # checks the happiness of that person and assigns it to a local variable
            happy = checkHappiness(person, data_pos, input_parameters)

            if not happy:
                # if the person is not happy

                # new space is initialized
                new_space = []

                # searches for possible empty spaces the person can move to for both red and blue people and assign those positions(list) to local variables
                (red_happy_spaces, blue_happy_spaces) = lookForSpaces(data_pos, empty_spaces, input_parameters)
                
                if person[0].getType() == 'blue':
                    # if the person is of type blue, then the person would move to blue possible spaces 

                    if blue_happy_spaces != []:
                        # checks if blue happy spaces is not empty and makes a random choice out of all possible spaces compatible for the person
                        # and assign it to new space
                        new_space = random.choice(blue_happy_spaces)

                        # sets the happiness of the person to True
                        person[0].setHappiness(True)

                elif person[0].getType() == 'red':
                    # if the person is of type red, then the person would move to red possible spaces 
                    if red_happy_spaces != []:
                        # checks if red happy spaces is not empty and makes a random choice out of all possible spaces compatible for the person
                        # and assign it to new space
                        new_space = random.choice(red_happy_spaces)

                        # sets the happiness of the person to True
                        person[0].setHappiness(True)

                if new_space == []:
                    # if the new space is still not updated, and the person is still not happy, new space will updated to a random empty space
                    new_space = random.choice(empty_spaces)

                # looks for the position/key value/ of the person and assigns it to a local variable pos
                pos = [i for i in data_pos if data_pos[i] == person][0]

                # appends the space the current position of the person(the position which will empty afterward) to empty spaces
                empty_spaces.append([person[0].getPosition()[0], person[0].getPosition()[1]-19])

                # new position will changed to key value for the dictionary data_pos
                new_pos = 32 * (new_space[0] - 1) + new_space[1]

                # the old key value(the old position) will know have an empty space object(which is a list having None and the compatibility for red and blue spaces boolean values)
                data_pos[pos] = [None, 'red: {}', 'blue: {}']

                # the key value(the new position which was an empty space) will now have that person as a value
                data_pos[new_pos] = person

                # the person's position is set to the new posisition
                person[0].setPosition(new_space[0], new_space[1]+19)

                # since the new position which was empty before is now filled, it is removed from the empty_spaces list
                empty_spaces.remove(new_space)

                
    # initialize the variable overall happy and population number
    overallHappy = 0
    population_number = 0

    for person in data_pos.values():
        # loops through each object in the data set
        if person[0] != None:
            # checks if the that object is a person not an empty space

            # checks the happiness of that person
            happy = checkHappiness(person, data_pos, input_parameters)

            # increments the population number by 1
            population_number += 1

            if happy == True:     
                # if the person is happy, then increments the overallHappy by 1
                overallHappy +=1

    # returns the overallHappy to population_number ratio
    return overallHappy/population_number


def simulate(window, data_pos, empty_spaces, input_parameters):
    '''Simulates the simulation space based on the parameters given'''

    # initialize the variable overall happy and population number
    overallHappy = 0 
    population_number = 0 

    # creates a list for the population happiness percetages
    pop_happiness_percentage = []

    # takes the input of the user from the input_parameters and assigns it to a local variable
    num_of_sim = input_parameters['Number of Simulations']

    for person in data_pos.values():
        # loops through each object in the data set
        if person[0] != None:
            # checks if the that object is a person not an empty space

            # checks the happiness of that person
            happy = checkHappiness(person, data_pos, input_parameters)

            # increments the population number by 1
            population_number += 1

            if happy == True:     
                # if the person is happy,increments the overallHappy by 1
                overallHappy +=1

    # creates a point for the first dataPoint on the graph, the point that shows the initial population happiness percentage
    last_point = [37, 22+(overallHappy/population_number)*26]

    # appends that value to the population happiness percentage values list
    pop_happiness_percentage.append(overallHappy/population_number)

    # creates a dataPoint object(green circular point) at that point on the graph
    datapoint = sch.DataPoint(window, last_point[0], last_point[1])

    for i in range(1, num_of_sim+1):
        # loops the number of times the user want to simulate(based on the input by the user initially)

        # simulates once and takes the over all happiness percentage for that simulation and assigns it a local variable
        population_happiness = simulateOnce(data_pos, empty_spaces, input_parameters)

        # appends that value to the population happiness percentage values list
        pop_happiness_percentage.append(population_happiness)

        # creates a dataPoint object(green circular point) at respective point on the graph
        datapoint = sch.DataPoint(window, 37+(i/num_of_sim)*28, 22+population_happiness*26)

        # takes the last pont and assigns it to a local variable
        p1 = last_point
        # takes the current point and assigns it to another variable
        p2 = [37+(i/num_of_sim)*28, 22+population_happiness*26]

        # creates a line between those two points on the graph
        line = sch.Line(window, p1, p2)

        # the currrent point will serve as a last point for the next simulation so I assign the current point to last_point 
        last_point = p2

        if i % 4 == 0 or i == num_of_sim:
            # for every 4th or the last simulation, there will be a horizontal axis tick just like the vertical axis tick

            # creates the tick, small vertical line at that point
            horizontal_axis_tick = sch.Line(window, [37+(i/num_of_sim)*28, 21.5], [37+(i/num_of_sim)*28, 22.5])
            # a text showing which simulation it is for
            tick_text = sch.Text(window, text=str(i), px=37+(i/num_of_sim)*28, py=20.5)
    
    return pop_happiness_percentage


def saveData(pop_happiness_percentage):
    '''Creates a file and saves the happiness percentage data of each simulation, which is obtained from the parameter, to that file'''

    # opens a file in write mode and asigns it to a local variable
    fp = open('data.csv', 'w')
    # writes the header of the .csv file
    fp.write('Simulation,Population Happiness Percentage\n')

    for i in range(len(pop_happiness_percentage)):
        # loops the length of the list parameter times and writes the data to the file
        fp.write(f'{i},{pop_happiness_percentage[i]}\n')

    # closes the file
    fp.close()


def main():
    '''Main Function; Creates a window where a user can enter the values for the Schelling's Model of Segregation and watch the simulation and save the data generated at the end'''

    # creates the window and assigns it to a local variable
    win = gr.GraphWin('Schelling\'s Model', 690, 520)

    # calls the homeScene function and assigns the result(the inputs by the user) to a local variable 
    home_scene_result_inputs = homeScene(win)

    # calls the initialize function and assigns the results to local variables
    (data_pos, empty_spaces) = initialize(win, home_scene_result_inputs)

    # calls the simulate function and simulates the simulation space and updates the graph based on the inputs from the user and the initialize function results
    # and assigns the results to a local variable
    pop_happiness_percentage = simulate(win, data_pos, empty_spaces, home_scene_result_inputs)

    # creates a button once the simulation is done and set the onclick field of the button to saveData function
    download_pop_happiness_percentages_button = sch.SubmitButton(win, button_text='Save Happiness Percentages', px=52, py = 10, onclick=saveData(pop_happiness_percentage) ,width=20, height=4, color='green', size=11)
    # waits for the users click on the button
    download_pop_happiness_percentages_button.getClick()

    # closes the window once done saving the data
    win.close()


if __name__ == "__main__":

    main()