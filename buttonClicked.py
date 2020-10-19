Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> #root for layout
>>> #now adding button to this layout
>>> button = ttk.Button(root,text="click me!") # take the layout to add to it
>>> button.pack() # make the button showed on the layout
>>> def buttonClicked(): #method to print text when click button
	print("button is clicked")

	
>>> button.config(command=buttonClicked) # add event to the button
>>> button is clicked
button is clicked
button is clicked
button is clicked
button is clicked
button is clicked
button is clicked
button is clicked
button is clicked

>>> button.invoke() # see the action on the button
button is clicked
'None'
>>> button.state(['disabled']) # see the state of the button
('!disabled',)
>>> button.instate(['disabled'])
True
>>> button.state(['!disabled'])
('disabled',)
>>> button is clicked

>>> button.instate(['disable'])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    button.instate(['disable'])
  File "C:\Program Files\Python39\lib\tkinter\ttk.py", line 576, in instate
    self.tk.call(self._w, "instate", ' '.join(statespec)))
_tkinter.TclError: Invalid state name disable
>>> button.instate(['disabled'])
False
>>> button is clicked
button is clicked
button is clicked
