from enum import Enum
from typing import Any, Optional

from flet.core.constrained_control import ConstrainedControl
from flet.core.control import OptionalNumber

class FletGlossyContainer(ConstrainedControl):
    """
    A glossy container.
    """

    def __init__(
        self,
        #
        # Control
        #
        opacity: OptionalNumber = None,
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        data: Any = None,
        #
        # ConstrainedControl
        #
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        #
        # FletGlossy specific
        #
        value: Optional[str] = "Glossy Container Text",
        width: Optional[float] = 200.0,
        height: Optional[float] = 200.0,
        border_radius: Optional[float] = 12.0,
        font_size: Optional[float] = 20.0,
        font_weight: Optional[str] = "w100",
        color: Optional[str] = "#FFFFFF"
    ):
        ConstrainedControl.__init__(
            self,
            tooltip=tooltip,
            opacity=opacity,
            visible=visible,
            data=data,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
        )

        self.value = value
        self.width = width
        self.height = height
        self.border_radius = border_radius
        self.font_size = font_size
        self.font_weight = font_weight
        self.color = color

    def _get_control_name(self):
        return "flet_glossy"

    # value
    @property
    def value(self):
        """
        Text to be shown on the glossy container.
        """
        return self._get_attr("value")

    @value.setter
    def value(self, value):
        self._set_attr("value", value)

    # width
    @property
    def width(self):
        """
        Width of the glassy container.
        """
        return self._get_attr("width")

    @width.setter
    def width(self, width):
        self._set_attr("width", width)

    # height
    @property
    def height(self):
        """
        Text to be shown on the glossy container.
        """
        return self._get_attr("height")

    @height.setter
    def height(self, height):
        self._set_attr("height", height)

    # border radius
    @property
    def border_radius(self):
        """
        Border radius of the glossy container.
        """
        return self._get_attr("border_radius")

    @border_radius.setter
    def border_radius(self, border_radius):
        self._set_attr("border_radius", border_radius)
        
    # font size
    @property
    def font_size(self):
        """
        Font size of the text on the glossy container.
        """
        return self._get_attr("font_size")

    @font_size.setter
    def font_size(self, font_size):
        self._set_attr("font_size", font_size)
        
    # font weight
    @property
    def font_weight(self):
        """
        Font weight of the text on the glossy container.
        """
        return self._get_attr("font_weight")

    @font_weight.setter
    def font_weight(self, font_weight):
        self._set_attr("font_weight", font_weight)
        
    # color
    @property
    def color(self):
        """
        Color of the text on the glossy container.
        """
        return self._get_attr("color")

    @color.setter
    def color(self, color):
        self._set_attr("color", color)
        