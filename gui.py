# Gui with three tabs
# 1 - Simulate and display results with graphs
# 2 - simulate probabilities in regions
# 3 - back home algorith for exact probability
import matplotlib

import randomWalk as randomWalk
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np

# Initialize customtkinter
ctk.set_appearance_mode("System")  # System, Light, Dark
ctk.set_default_color_theme("blue")  # Blue, Dark-blue, Green

def askProbabilities(d):
    probabilities = []
    return probabilities

class DoubleFrameTab:
    def __init__(self, parentFrame):
        self.parentFrame = parentFrame
        # Top Frame for inputs on top and output on bottom
        self.topFrame = ctk.CTkFrame(self.parentFrame)
        self.topFrame.pack(fill="both", expand=True)
        # Bottom Frame for graphical outputs
        self.bottomFrame = ctk.CTkFrame(self.parentFrame)
        self.bottomFrame.pack(fill="both", expand=True)


class SimulationTab(DoubleFrameTab):
    def __init__(self, parentFrame):
        super().__init__(parentFrame)
        # Create input frame
        self.inputFrame = ctk.CTkFrame(self.topFrame)
        self.inputFrame.grid(row=0, column=0, sticky="nsew")
        # Create output frame
        self.outputFrame = ctk.CTkFrame(self.topFrame)
        self.outputFrame.grid(row=0, column=1, sticky="nsew")
        # Configure to fill up the space
        self.topFrame.columnconfigure(1, weight=1)
        self.topFrame.columnconfigure(0, weight=1)
        self.topFrame.rowconfigure(0, weight=1)
        self.topFrame.rowconfigure(1, weight=1)
        # Title
        self.labelInput = ctk.CTkLabel(self.inputFrame, text="Inputs")
        self.labelInput.grid(row=0, column=0, sticky="nw")
        self.labelOutputs = ctk.CTkLabel(self.outputFrame, text="Outputs")
        self.labelOutputs.grid(row=0, column=0, sticky="nw")
        # Label and entry for "# of directions"
        self.labelDirections = ctk.CTkLabel(self.inputFrame, text="Directions")
        self.labelDirections.grid(row=1, column=0, sticky="w", pady=5, padx=10)
        self.entryDirections = ctk.CTkEntry(self.inputFrame, placeholder_text=0)
        self.entryDirections.grid(row=1, column=1, sticky="w", padx=10)
        # Label and entry for "steps"
        self.labelSteps = ctk.CTkLabel(self.inputFrame, text="Steps")
        self.labelSteps.grid(row=2, column=0, sticky="w", pady=5, padx=10)
        self.entrySteps = ctk.CTkEntry(self.inputFrame)
        self.entrySteps.grid(row=2, column=1, sticky="w", padx=10)
        # Button
        self.buttonInput = ctk.CTkButton(self.inputFrame, text="Execute",
                                         command=self.executeSim)
        self.buttonInput.grid(row=0, column=1, sticky="w", padx=10, pady=5)

        # Checkbox for "Eq. probabilities"
        self.eqProbCheckbox = ctk.CTkCheckBox(self.inputFrame,
                                              text="Eq. probabilities",
                                              command=self.on_eq_prob_checked)
        self.eqProbCheckbox.grid(row=3, column=0, columnspan=2, sticky="w", pady=5, padx=10)

        # Checkbox for "Custom probabilities"
        self.customProbCheckbox = ctk.CTkCheckBox(self.inputFrame,
                                                  text="Custom probabilities",
                                                  command=self.on_custom_prob_checked)
        self.customProbCheckbox.grid(row=4, column=0, columnspan=2, sticky="w", pady=5, padx=10)

        # Configure inputFrame to handle resizing
        self.inputFrame.columnconfigure(1, weight=1)

        # Output Frame Components
        # Label and entry for "Final x"
        self.labelFinalX = ctk.CTkLabel(self.outputFrame, text="Final x")
        self.labelFinalX.grid(row=1, column=0, sticky="w", pady=5, padx=10)
        self.entryFinalX = ctk.CTkEntry(self.outputFrame)
        self.entryFinalX.grid(row=1, column=1, sticky="w", padx=10)

        # Label and entry for "Final y"
        self.labelFinalY = ctk.CTkLabel(self.outputFrame, text="Final y")
        self.labelFinalY.grid(row=2, column=0, sticky="w", pady=5, padx=10)
        self.entryFinalY = ctk.CTkEntry(self.outputFrame)
        self.entryFinalY.grid(row=2, column=1, sticky="w", padx=10)

        # Label and entry for "Distance"
        self.labelDistance = ctk.CTkLabel(self.outputFrame, text="Distance")
        self.labelDistance.grid(row=3, column=0, sticky="w", pady=5, padx=10)
        self.entryDistance = ctk.CTkEntry(self.outputFrame)
        self.entryDistance.grid(row=3, column=1, sticky="w", padx=10)

        # Configure outputFrame to handle resizing
        self.outputFrame.columnconfigure(1, weight=1)
        self.leftGraphFrame = ctk.CTkFrame(self.bottomFrame)
        self.leftGraphFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.rightGraphFrame = ctk.CTkFrame(self.bottomFrame)
        self.rightGraphFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # Configure bottomFrame to allocate space to both graph frames
        self.bottomFrame.columnconfigure(0, weight=1)
        self.bottomFrame.columnconfigure(1, weight=1)
        self.bottomFrame.rowconfigure(0, weight=1)

        # Example matplotlib figures for demonstration
        # Left Graph (Placeholder plot)
        # fig_left = plt.Figure(figsize=(5, 4), dpi=100)
        # ax_left = fig_left.add_subplot(111)
        # ax_left.plot([0, 1, 2, 3], [0, 1, 4, 9])  # Example data
        # self.canvasLeft = FigureCanvasTkAgg(fig_left, master=self.leftGraphFrame)
        # self.canvasLeft.draw()
        # self.canvasLeft.get_tk_widget().pack(fill="both", expand=True)

        # Right Graph (Placeholder plot)
        # fig_right = plt.Figure(figsize=(5, 4), dpi=100)
        # ax_right = fig_right.add_subplot(111)
        # ax_right.plot([0, 1, 2, 3], [0, -1, -4, -9])  # Example data
        # self.canvasRight = FigureCanvasTkAgg(fig_right, master=self.rightGraphFrame)
        # self.canvasRight.draw()
        # self.canvasRight.get_tk_widget().pack(fill="both", expand=True)


    def executeSim(self):
        # Get inputs
        directions = int(self.entryDirections.get())
        steps = int(self.entrySteps.get())
        if self.customProbCheckbox.get():
            probabilities = askProbabilities()
        else:
            probabilities = 1/directions.shape[0]*np.ones((directions,1))
        # Create instance
        randomWalker = randomWalk.RandomWalk(directions, probabilities)
        walk = randomWalker.walk(steps)
        # Set outputs
        self.entryFinalX.delete(0, tk.END)
        self.entryFinalY.delete(0, tk.END)
        self.entryFinalX.insert(0, np.round(walk[-1,0],4))
        self.entryFinalY.insert(0, np.round(walk[-1,1],4))
        self.entryDistance.delete(0, tk.END)
        self.entryDistance.insert(0, np.round(np.sqrt(np.sum(walk[-1,:]**2)),4))
        # Update plots
        for i in self.leftGraphFrame.winfo_children():
            i.pack_forget()
        fig1 = randomWalker.plot(walk, 0, facecolor="#424242", axis_color='w')
        self.canvasLeft = FigureCanvasTkAgg(fig1, master=self.leftGraphFrame)
        self.canvasLeft.draw()
        self.canvasLeft.get_tk_widget().pack(fill="both", expand=True)
        for i in self.rightGraphFrame.winfo_children():
            i.pack_forget()
        fig2 = randomWalk.heatmap(walk, 50, facecolor="#424242", axis_color='w')
        self.canvasRight = FigureCanvasTkAgg(fig2, master=self.rightGraphFrame)
        self.canvasRight.draw()
        self.canvasRight.get_tk_widget().pack(fill="both", expand=True)
        plt.close()

    def on_eq_prob_checked(self):
        """Callback when Eq. probabilities checkbox is checked."""
        if self.eqProbCheckbox.get() == 1:  # If Eq. probabilities is checked
            self.customProbCheckbox.deselect()  # Deselect Custom probabilities

    def on_custom_prob_checked(self):
        """Callback when Custom probabilities checkbox is checked."""
        if self.customProbCheckbox.get() == 1:  # If Custom probabilities is checked
            self.eqProbCheckbox.deselect()  # Deselect Eq. probabilities







class SimulateProbabilities(DoubleFrameTab):
    def __init__(self, parentFrame):
        super().__init__(parentFrame)


class SideTabApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure the main window
        self.title("Random Walk")
        self.geometry("800x500")
        self.tabs = ["Simulate", "Regions", "Algorithm"]
        # Sidebar frame (left side tabs)
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")
        # Main content area
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.pack(side="right", fill="both", expand=True)
        # Add tab buttons to the sidebar
        self.create_tabs()
        # Display content for the first tab by default
        self.show_tab_content(self.tabs[0])

    def create_tabs(self):
        # Add a button for each tab in the sidebar
        for tab_name in self.tabs:
            button = ctk.CTkButton(self.sidebar, text=tab_name,
                                   command=lambda t=tab_name: self.show_tab_content(t))
            button.pack(pady=10, padx=10, fill="x")

    def show_tab_content(self, tab_name):
        # Clear existing content in the content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        # Create Tab
        self.createTab(tab_name)

    def createTab(self, tab_name):
        if tab_name == self.tabs[0]:
            SimulationTab(self.content_frame)
        elif tab_name == self.tabs[1]:
            SimulateProbabilities(self.content_frame)
        elif tab_name == self.tabs[2]:
            pass
        return


if __name__ == "__main__":
    app = SideTabApp()
    app.mainloop()
