#!/bin/python

from manimlib.imports import *
import numpy as np

class Solution(Scene):

    def gen_vector(self, vector):
        point1 = np.array([vector[0][0]-2.5,vector[0][1]-2.5,0])
        point2 = np.array([vector[1][0]-2.5,vector[1][1]-2.5,0])
        line = Line(point1, point2, color=PURPLE, stroke_width=10.0)
        self.play(ShowCreation(line))
        return line


    def construct(self):

        # Defining the grid that we will work on.

        grid_background = Square(side_length=6, color=BLUE, fill_opacity=0.7)
        grid_foreground = []
        for i in range(1,7):
            grid_row = []
            for j in range(1,7):
                grid_row.append(Square(side_length=1, color=DARK_BLUE).shift(np.array([j-3.5,i-3.5,0])))
            grid_foreground.append(grid_row)

        # Define the counters that we will use to mark spaces

        counters = []
        for i in range(1,7):
            counter_column = []
            for j in range(1,7):
                counter_column.append(Circle(radius=0.4, color=GREEN, fill_opacity=0.7).shift(np.array([i-3.5,j-3.5,0])))
            counters.append(counter_column)

        # Define the explanation text
        text_strings = [
                "We can write all lengths as coordinates",
                "Taking into account pythagorean triples",
                "We can now place our markers as shown below",
                "Now let's exhaustively search all combinations",
                "We can keep track of vectors used by crossing them out",
                "Finally, we can see that there are no lengths used twice"
                ]
        text_objects = []
        for string in text_strings:
            text_objects.append(TextMobject(string).next_to(grid_background, UP))

        # Define the vectors used
        vector_text = [
                "(1,0)",
                "(2,0)",
                "(3,0)",
                "(4,0)",
                "(1,1)",
                "(2,1)",
                "(3,1)",
                "(4,1)",
                "(5,1)",
                "(2,2)",
                "(3,2)",
                "(4,2)",
                "(5,2)",
                "(3,3)",
                "(4,3) = (5,0)",
                "(5,3)",
                "(4,4)",
                "(5,4)",
                "(5,5)"
                ]
        vector_objects = []
        for i,text in enumerate(vector_text):
            if i == 0:
                vector_objects.append(TextMobject(text).next_to(grid_background, LEFT).shift(np.array([-1,3,0])))
            elif i == 9:
                vector_objects.append(TextMobject(text).next_to(grid_background, RIGHT).shift(np.array([1,3,0])))
            else:
                vector_objects.append(TextMobject(text).next_to(vector_objects[-1], DOWN))

        # Define crossouts for vector texts

        vector_crosses = []
        for i,text in enumerate(vector_text):
            vector_crosses.append(Line(vector_objects[i].get_edge_center(LEFT) + np.array([-0.2,0,0]), vector_objects[i].get_edge_center(RIGHT) + np.array([0.2,0,0]), color=RED))





        #Draw the grid

        self.play(DrawBorderThenFill(grid_background))
        fade_in_objects = []
        for row in grid_foreground:
            for tile in row:
                fade_in_objects.append(FadeIn(tile))
        self.play(*fade_in_objects)
#        self.play(DrawBorderThenFill(counters[1][0]))
#        for v in vector_objects:
#            self.play(Write(v))
#        for l in vector_crosses:
#            self.play(ShowCreation(l))
        self.play(Write(text_objects[0]))
        vector_write_objects = []
        for v in vector_objects:
            vector_write_objects.append(Write(v))
        self.wait(2)
        self.play(*vector_write_objects)
        self.play(Transform(text_objects[0], text_objects[1]))
        self.wait(2)
        self.play(Transform(text_objects[0], text_objects[2]))
        counter_animations = []
        counter_animations.append(DrawBorderThenFill(counters[5][5]))
        counter_animations.append(DrawBorderThenFill(counters[2][5]))
        counter_animations.append(DrawBorderThenFill(counters[5][3]))
        counter_animations.append(DrawBorderThenFill(counters[3][1]))
        counter_animations.append(DrawBorderThenFill(counters[1][0]))
        counter_animations.append(DrawBorderThenFill(counters[0][0]))
        self.play(*counter_animations)
        self.wait(2)
        self.play(Transform(text_objects[0], text_objects[3]))
        self.wait(1)
        line = self.gen_vector([[5,5],[2,5]])
        self.wait(1)
        self.play(Transform(text_objects[0], text_objects[4]))
        self.wait(1)
        self.play(ShowCreation(vector_crosses[2]))
        self.play(FadeOut(line))
        self.wait(2)
        line = self.gen_vector([[5,5],[5,3]])
        self.wait(1)
        self.play(ShowCreation(vector_crosses[1]))
        self.play(FadeOut(line))
        self.wait(1)
        line = self.gen_vector([[5,5],[3,1]])
        self.wait(1)
        self.play(ShowCreation(vector_crosses[11]))
        self.play(FadeOut(line))
        self.wait(1)
        line = self.gen_vector([[5,5],[1,0]])
        self.wait(1)
        self.play(ShowCreation(vector_crosses[17]))
        self.play(FadeOut(line))
        self.wait(1)
        line = self.gen_vector([[5,5],[0,0]])
        self.wait(1)
        self.play(ShowCreation(vector_crosses[18]))
        self.play(FadeOut(line))
        self.wait(1)
        line = self.gen_vector([[2,5],[5,3]])
        self.wait(1)
        self.play(ShowCreation(vector_crosses[10]))
        self.play(FadeOut(line))
        self.wait(1)
        line = self.gen_vector([[2,5],[3,1]])
        self.wait(1)
        self.play(ShowCreation(vector_crosses[7]))
        self.play(FadeOut(line))
        self.wait(1)
        line = self.gen_vector([[2,5],[1,0]])
        self.wait(1)
        self.play(ShowCreation(vector_crosses[8]))
        self.play(FadeOut(line))
        self.wait(1)
        line = self.gen_vector([[2,5],[0,0]])
        self.wait(1)
        self.play(ShowCreation(vector_crosses[12]))
        self.play(FadeOut(line))
        self.wait(1)
        line = self.gen_vector([[5,3],[3,1]])
        self.wait(1)
        self.play(ShowCreation(vector_crosses[9]))
        self.play(FadeOut(line))
        self.wait(1)
        line = self.gen_vector([[5,3],[1,0]])
        self.wait(1)
        self.play(ShowCreation(vector_crosses[14]))
        self.play(FadeOut(line))
        self.wait(1)
        line = self.gen_vector([[5,3],[0,0]])
        self.wait(1)
        self.play(ShowCreation(vector_crosses[15]))
        self.play(FadeOut(line))
        self.wait(1)
        line = self.gen_vector([[3,1],[1,0]])
        self.wait(1)
        self.play(ShowCreation(vector_crosses[5]))
        self.play(FadeOut(line))
        self.wait(1)
        line = self.gen_vector([[3,1],[0,0]])
        self.wait(1)
        self.play(ShowCreation(vector_crosses[6]))
        self.play(FadeOut(line))
        self.wait(1)
        line = self.gen_vector([[1,0],[0,0]])
        self.wait(1)
        self.play(ShowCreation(vector_crosses[0]))
        self.play(FadeOut(line))
        self.wait(1)
        self.play(Transform(text_objects[0], text_objects[5]))
        self.wait(3)
