from circle import Circle
from rectangle import Rectangle
from shape import Shape
import matplotlib.pyplot as plt
from matplotlib.patches import Circle as matp_circle, Rectangle as matp_rectangle


class Shape2dPlotter:
    """Plots 2D shapes (Circle, Rectangle) using Matplotlib.

    Validates that added objects are Shape instances.
    Supports adding multiple shapes and drawing them
    with consistent axis limits and grid.
    """

    def __init__(self, shapes: list[Shape] | None = None):

        if shapes is None:
            self.shapes = []
        else:
            self.shapes = shapes

        fig, ax = plt.subplots()
        self.fig = fig
        self.ax = ax

    def add_shapes(self, shape):

        if isinstance(shape, Shape):

            self.shapes.append(shape)

        else:
            raise TypeError("shape is not a subclass to Shape")

    def draw_all(self):

        for shape in self.shapes:
            if isinstance(shape, Circle):
                circle_patch = matp_circle((shape.x, shape.y), shape.radius, fill=False)
                self.ax.add_patch(circle_patch)
            if isinstance(shape, Rectangle):
                rectangle_patch = matp_rectangle(
                    (shape.x, shape.y), shape.width, shape.height, fill=False
                )
                self.ax.add_patch(rectangle_patch)

        # Set axis limits and proportions for the plot
        self.ax.set_xlim(-5, 20)
        self.ax.set_ylim(-5, 20)

        # keeps circles and rectangles correctly scaled
        self.ax.set_aspect("equal")

        # Add a light dashed grid for better readability
        self.ax.grid(True)
        self.ax.grid(color="gray", linestyle="--", linewidth=0.5)
        plt.show()
