import math

from kivy.uix.layout import Layout
from kivy.properties import (
    NumericProperty,
    VariableListProperty,
    OptionProperty,
)

class CircleLayout(Layout):
    orientation = OptionProperty('clock', options=('clock', 'reverse_clock'))
    center = VariableListProperty([0, 0])
    radius = NumericProperty(0)
    first_widget_pos = NumericProperty(0)

    def __init__(self, **kwargs):
        """ Circle layout initialization, binding needed on properties """
        super(CircleLayout, self).__init__(**kwargs)
        update  = self._trigger_layout
        fbind('orientation', update)
        fbind('center', update)
        fbind('radius', update)
        fbind('first_widget_pos', update)
        fbind('children', update)
        fbind('parent', update)
        fbind('size', update)
        fbind('pos', update)

    def do_layout(self):
        len_children = len(self.children)
        if len_children == 0:
            return
        first_pos = float(self.first_widget_pos)
        if first_pos < 0 or first_pos > 360:
            return

        first_pos = first_pos / 180.0 * math.pi
        offset = 2.0 * math.pi / len_children
        orientation = self.orientation


    def add_widget(self, widget, index=0):
        pass

    def remove_widget(self, widget):
        pass
