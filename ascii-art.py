
class Canvas():
    """A canvas for adding shapes."""

    def __init__(self):
        """Initialize a canvas object."""
        self.shapes = []


    def render(self):
        """Print a canvas and its shapes."""

        # Create the canvas as a nested list.
        canvas = []
        for x in range(0, 10):
            canvas.append([None for i in range(0,10)])

        # Update canvas list with the canvas object's shapes.
        for shape in self.shapes:
            for x in range(shape.start_x, shape.end_x + 1):
                for y in range(shape.start_y, shape.end_y + 1):
                    canvas[x][y] = shape.fill_char

        # Print canvas.
        print(" 0123456789")
        
        for y in range(0, 10):
            string_to_print = str(y)
            
            for x in range(0, 10):
                if canvas[x][y] == None:
                    string_to_print += " "
                else:
                    string_to_print += canvas[x][y]

            print(string_to_print)


    def add_shape(self, shape):
        """Add a shape to a canvas."""
        self.shapes.append(shape)


    def clear(self):
        """Remove shapes from a canvas."""
        self.shapes = []



class Rectangle():
    """A rectangle object."""

    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        """Instantiate a rectangle object."""

        legal_values = set(range(0,10))
        corners = {start_x, start_y, end_x, end_y}

        if not corners.issubset(legal_values):
            raise ValueError("Start and end values must be within 0-9.")

        if len(fill_char) != 1:
            raise ValueError("Please select only 1 fill character.")

        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.fill_char = fill_char


    def change_fill(self, fill_char):
        """Change the fill character of a rectangle."""
        if len(fill_char) != 1:
            raise ValueError("Please select only 1 fill character.")

        self.fill_char = fill_char


    def translate(self, axis, num):
        """Move a rectangle's location on the canvas."""

        if axis == "x":
            if self.start_x + num < 0 or self.end_x + num > 9:
                raise ValueError("Please select a smaller translation value.") 
            else:
                self.start_x += num
                self.end_x += num

        elif axis == "y":
            if self.start_y + num < 0 or self.end_y + num > 9:
                raise ValueError("Please select a smaller translation value.")
            else:
                self.start_y += num
                self.end_y += num

        else:
            raise ValueError("Please select a valid axis: 'x' or 'y'")

