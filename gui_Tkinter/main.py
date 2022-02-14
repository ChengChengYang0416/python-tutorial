# use Tkinter for python2, tkinter for python3
import Tkinter as tk
import ButtonFcn.ButtonFcn as ButtonFcn

# build main window
Win = tk.Tk()

#------------------- basic setting -------------------#
# set title
Win.title( "Tkinter-tutorial" )

# set geometry of window ( width x height )
Win.geometry( "400x300" )
Win.minsize( width = 400, height = 300 )
Win.maxsize( width = 800, height = 600 )
Win.resizable( True, True )

# color, transparency, pin on top
Win.config( background = "#C0C0C0" )
Win.attributes( "-alpha", 0.65 )
Win.attributes( "-topmost", True )
#------------------- end of basic setting -------------------#

#------------------- button example -------------------#
# basic button with pixel size
Pixel = tk.PhotoImage( width = 1, height = 1 )
Btn = tk.Button( text = "Button", image = Pixel, background = "#FFFFFF", width = 40, height = 10, compound = "c" )
Btn.pack()

# insert image to button and show the text simultaneously
Img = tk.PhotoImage( file = "Button.png" )
ImgResize = Img.subsample( 20, 20 )
BtnImage = tk.Button( text = "Click me !", image = ImgResize, compound = "left", command = ButtonFcn.PrintHello )
BtnImage.pack()
#------------------- end of button example -------------------#

# let Tkinter start running the application
Win.mainloop()
