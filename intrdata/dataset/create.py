from kivy.app import App
from kivy.uix.button import Button
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty

import random
import pandas as pd
import argparse

W_WIDTH = 500.0
W_HEIGHT = 500.0
from kivy.core.window import Window
Window.clearcolor = (0.5, 0.5,0.5, 0.5)
Window.size = (W_WIDTH, W_HEIGHT)
DF = None

class ClassButton(Button):
    classId = NumericProperty(1)


class RootWidget(FloatLayout):
    numClasses = NumericProperty(1)

    def classSwitch(self,toClass):
        Dataset.CURRENT_CLASS = toClass

    def toDataFrame(self,points):
        x1 = [x[0] for x in points]
        x2 = [x[1] for x in points]
        y = [x[2] for x in points]
        df= pd.DataFrame({"x1": x1, "x2":x2 , "y":y})
        Dataset.DF = df
        App.get_running_app().stop()

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)

        # let's add a Widget to this layout

        self.buttons = []
        for c in range(self.numClasses):
            b = ClassButton(text=f'Class-{c}' ,classId=c, size_hint=(.1, .1),pos_hint={"x":0 , "y":0.8-c*0.1})
            self.buttons.append(b)
            b.bind(on_press=lambda x: self.classSwitch(x.classId))
            self.add_widget(b)

        b_to_df = Button(text=f'To DataFrame' ,size_hint=(.1, .1),pos_hint={"x":0 , "y":0.9})
        b_to_df.bind(on_press=lambda x: self.toDataFrame(Dataset.POINTS_COLLECTED))

        self.add_widget(b_to_df)

        self.add_widget(MousePos(numClasses=self.numClasses))

class MousePos(Widget):
    numClasses = NumericProperty(1)

    def __init__(self, **kwargs):
        super(MousePos, self).__init__(**kwargs)
        self.colors = [(random.random(),random.random(),random.random(),0.5) for i in range(self.numClasses)]

    def on_touch_down(self, touch):
        touch.apply_transform_2d(self.to_window)
        #print('The touch is at position', touch.pos)
        x,y = touch.pos
        x /= W_WIDTH
        y /= W_HEIGHT

        if x > 0.1:
            with self.canvas.after:
                Color(*self.colors[Dataset.CURRENT_CLASS] , mode='rgba')
                self.rect = Rectangle(pos=(touch.x,touch.y), size=(10,10))
                Dataset.POINTS_COLLECTED.append((touch.x,touch.y,Dataset.CURRENT_CLASS))

class Dataset(App):
    CURRENT_CLASS = 0
    POINTS_COLLECTED = []
    num_classes = NumericProperty(1)

    def build(self):
        print(self.num_classes)
        return RootWidget(numClasses=int(self.num_classes))


def inputDataset(num_classes):
    Dataset(num_classes=num_classes).run()
    return Dataset.DF

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num-classes" , default=2 , help="Number of Classes")
    args = parser.parse_args()

    df = inputDataset(args.num_classes)
    print(df.head())
