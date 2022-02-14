# use Tkinter for python2, tkinter for python3
import Tkinter as tk

# build main window
Win = tk.Tk()

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

# let Tkinter start running the application
Win.mainloop()
