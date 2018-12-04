import math

from kivy.uix.layout import Layout
from kivy.properties import (
    NumericProperty,
    VariableListProperty,
    OptionProperty,
)

class CircleLayout(Layout):
    orientation = OptionProperty('clock', options=('clock', 'reverse_clock'))
    radius = NumericProperty(0)
    first_widget_pos = NumericProperty(0)


    def __init__(self, **kwargs):
        """ Circle layout initialization, binding needed on properties """
        super(CircleLayout, self).__init__(**kwargs)
        update  = self._trigger_layout
        fbind = self.fbind
        fbind('orientation', update)
        fbind('radius', update)
        fbind('first_widget_pos', update)
        fbind('children', update)
        fbind('parent', update)
        fbind('size', update)
        fbind('pos', update)

    def on_children(self, _, children):
        self._trigger_layout()

    def do_layout(self, *largs):
        len_children = len(self.children)
        if len_children == 0:
            return
        first_pos = float(self.first_widget_pos)
        if first_pos < 0 or first_pos > 360:
            return

        first_pos = first_pos / 180.0 * math.pi
        orientation = self.orientation
        if orientation == 'reverse_clock':
            offset_angle = 2.0 * math.pi / float(len_children)
        else:
            offset_angle = -2.0 * math.pi / float(len_children)

        for index, child in enumerate(reversed(self.children)):
            child.pos = [
                self.center[index] + (xy * self.radius)
                for index, xy in enumerate((
                    math.cos(offset_angle * index),
                    math.sin(offset_angle * index)
                ))
            ]



    def add_widget(self, widget, index=0):
        widget.bind(pos_hint=self._trigger_layout)
        return super(CircleLayout, self).add_widget(widget, index) 

    def remove_widget(self, widget):
        widget.bind(pos_hint=self._trigger_layout)
        return super(CircleLayout, self).remove_widget(widget)
