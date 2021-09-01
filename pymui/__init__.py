import pyact as pa

MaterialUI = require ('@material-ui/core')
MaterialUI_lab = require ('@material-ui/lab')

class Wrapper:
    def __init__ (self, Wrappee, args):
        self.Wrappee = Wrappee
        self.args = args

    def el (self):
        return pa.createElement (self.Wrappee, *self.args)

AppBar = lambda *args: Wrapper (MaterialUI.AppBar, args)
Box = lambda *args: Wrapper (MaterialUI.Box, args)
Button = lambda *args: Wrapper (MaterialUI.Button, args)
Card = lambda *args: Wrapper (MaterialUI.Card, args)
Grid = lambda *args: Wrapper (MaterialUI.Grid, args)
Paper = lambda *args: Wrapper (MaterialUI.Paper, args)
Slider = lambda *args: Wrapper (MaterialUI.Slider, args)
Tab = lambda *args: Wrapper (MaterialUI.Tab, args)
Tabs = lambda *args: Wrapper (MaterialUI.Tabs, args)
TextField = lambda *args: Wrapper (MaterialUI.TextField, args)

TabContext = lambda *args: Wrapper (MaterialUI_lab.TabContext, args)
TabList = lambda *args: Wrapper (MaterialUI_lab.TabList, args)
TabPanel = lambda *args: Wrapper (MaterialUI_lab.TabPanel, args)

Canvas = lambda *args: Wrapper ('canvas', args)

class String:
    def __init__ (self, Wrappee):
        self.Wrappee = Wrappee

    def el (self):
        return self.Wrappee
