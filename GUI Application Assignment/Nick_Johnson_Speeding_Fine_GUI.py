"""
Assignment: Speeding Fine GUI
Class: DEV 128
Date: 03/12/2024
Author: Nick Johnson
Description: Program to provide a GUI for speeding fines
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Nick_Johnson_Speeding_Fine import SpeedingFineCalculator


# Class for the Presentation layer
class SpeedingFineFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")

        # Business tier class
        self.speedingFineCalculator = SpeedingFineCalculator()

        # Save the parent so we can call destroy on the parent window
        self.parent = parent

        # Define variables for text entry fields
        self.speedLimit = tk.DoubleVar()
        self.clockedSpeed = tk.DoubleVar()
        self.speedingFine = tk.DoubleVar()
        self.initComponents()

    def initComponents(self):
        self.pack()
        self.initMainFrame()
        self.initButtonsFrame()

    def initMainFrame(self):
        # Add implementation:
        # Create a new Frame object and use grid method to add it to the parent frame (self).
        # Create and place the 6 labels and 3 text entry boxes.
        # Connect the DoubleVar attributes declared in the constructor to the text entry boxes.
        frame = ttk.Frame(self, padding=10)
        frame.grid()
        ttk.Label(frame, text="Minimum Fine: $50").grid(column=0, row=0, sticky="w")
        ttk.Label(frame, text="Penalty per MPH over limit: $5").grid(
            column=0, row=1, sticky="w"
        )
        ttk.Label(frame, text="Penalty for 50 MPH over the limit: $200").grid(
            column=0, row=2, sticky="w"
        )

        ttk.Label(frame, text="Speed Limit:").grid(column=0, row=3, sticky="w")
        ttk.Entry(frame, width=25, textvariable=self.speedLimit).grid(
            column=1, row=3, sticky="w"
        )

        ttk.Label(frame, text="Clocked Speed").grid(column=0, row=4, sticky="w")
        ttk.Entry(frame, width=25, textvariable=self.clockedSpeed).grid(
            column=1, row=4, sticky="w"
        )

        ttk.Label(frame, text="Speeding Fine").grid(column=0, row=5, sticky="w")
        ttk.Entry(
            frame, width=25, textvariable=self.speedingFine, state="readonly"
        ).grid(column=1, row=5, sticky="w")

        self.initButtonsFrame()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def initButtonsFrame(self):
        # Add implementation:
        # Creates a new Frame object and use grid method to add it to the parent frame (self).
        # Create and place three buttons to this frame using grid method.
        # Add the corresponding event-handlers to the buttons.
        button_frame = ttk.Frame(self)
        button_frame.grid(column=0, row=6, columnspan=3, sticky="w")

        ttk.Button(button_frame, text="Calculate", command=self.calculateFine).grid(
            column=0, row=0, padx=5
        )

        ttk.Button(button_frame, text="Clear", command=self.clear).grid(
            column=1, row=0, padx=5
        )

        ttk.Button(button_frame, text="Exit", command=self.exit).grid(
            column=2, row=0, padx=5
        )

    def calculateFine(self):
        # Add implementation
        # Event-handler for the button.
        # Read the values of Entry boxes corresponding to the speeding limit and clocked speed.
        # call the calculateSpeedingFine method on self.speedingFineCalculator object to calculate the fine,
        # populate the text entry box with the fine.
        if float(self.speedLimit.get()) < 0 or float(self.clockedSpeed.get()) < 0:
            messagebox.showerror("Error", "Please enter valid positive numbers")
            self.clear()
        self.speedingFineCalculator.speedingLimit = float(self.speedLimit.get())
        self.speedingFine.set(
            self.speedingFineCalculator.calculateSpeedingFine(
                float(self.clockedSpeed.get())
            )
        )

    def clear(self):
        # Add implementation: clear all the text entry boxes
        self.speedLimit.set(0.0)
        self.clockedSpeed.set(0.0)
        self.speedingFine.set(0.0)

    def exit(self):
        self.parent.destroy()


def main():
    root = tk.Tk()
    root.title("Speeding Fine Calculator of Funnyville")
    root.geometry("600x250")
    SpeedingFineFrame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
