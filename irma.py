import turtle
import csv
import time

def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()

    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.gif")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)


    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def setCategory(speed, t):
    ''' Determine the category rating of the hurricane, given
        the wind speed in MPH.  Modify the pen settings of the
        turtle t to be appropriate for drawing that category.
        Return the category, or 0 for non-hurricane strength wind'''


    """ all the categorys of hurricanes and their respective wind speeds """
    category1 = 74
    category2 = 96
    category3 = 111
    category4 = 130
    category5 = 157

    if speed < category1:
        t.width(1)
        t.pencolor('white')
        return 0
    elif speed < category2:
        t.width(2)
        t.pencolor('blue')
        return 1
    elif speed < category3:
        t.width(4)
        t.pencolor('green')
        return 2
    elif speed < category4:
        t.width(6)
        t.pencolor('yellow')
        return 3
    elif speed < category5:
        t.width(8)
        t.pencolor('orange')
        return 4
    else:
        t.width(10)
        t.pencolor('red')
        return 5


def irma():
    """Animates the path of hurricane Irma
    """
    # Do not change this line
    # t is the turtle, and you will not need the other variables
    (t, wn, map_bg_img) = irma_setup()

    hurricaneFile = "data/irma.csv"
    # The line below is a little magical. It opens the file,
    # with awareness of any errors that might occur.
    with open(hurricaneFile, 'r') as csvfile:
        # This line gives you an "iterator" you can use to get each line
        # in the file.
        pointreader = csv.reader(csvfile)
        next(pointreader)
        t.width()
        t.penup()

        # You'll need to add some code here, before the loop
        # One thing you'll need to figure out how to do is to
        # skip the first line of the file (which is the header).
        # You might use a boolean variable, or you can
        # look into Python's built-in next function
        #(https://docs.python.org/3/library/functions.html#next)
        # pointreader is an iterator

        for row in pointreader:
            # row is a list representing each line in the csv file
            # Each comma separated element is in its own index position
            # This code just prints out the date and time elements of each
            # row in the file.
            # Make sure you understand what is happening here.
            # Then, you'll need to change this code
            lat = float(row[2])
            lon = float(row[3])
            wind = float(row[4])
            t.setpos(lon, lat)
            t.pendown()
            cat = setCategory(wind, t)
            if cat >= 1:
                t.write(str(cat), font=("Arial", 10, "normal"))
            print("Date:", row[0], "Time:", row[1])



    # Hack to make sure a reference to the background image stays around
    # Do not remove or change this line
    return map_bg_img


# Feel free to add "helper" functions here


if __name__ == "__main__":
    bg=irma()
    time.sleep(10)
