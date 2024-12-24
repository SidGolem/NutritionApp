import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Food_Values import foodValues

#Food Codes
pb = (10, 10, 10, 10, 10, 10, 10, 10)
PROTEIN = 56
CARBS = 130
FIBER = 34
CALCIUM = 1000
IRON = 8
MAGNESIUM = 400
PHOSPHORUS = 700
SODIUM = 2300
ZINC = 11
VA = 900
VE = 15
VD = 600
VC = 90
foodRow = 1
class NutritionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Nutrition App")
        self.root.geometry("600x400")
        
        # Create notebook for different tabs
        notebook = ttk.Notebook(root)
        notebook.pack(fill='both', expand=True)

        #Create notebook tabs
        calculator_frame = ttk.Frame(notebook)
        notebook.add(calculator_frame, text='Calculator')
        self.calculator_init(calculator_frame)
        foodValTab = ttk.Frame(notebook)
        notebook.add(foodValTab, text = 'Food Codes')

        #Create Buttons
        

        

        
        # # Pack Layout Demo
        # pack_frame = ttk.Frame(notebook)
        # notebook.add(pack_frame, text='Pack Layout')
        # self.pack_demo(pack_frame)
        
        # # Grid Layout Demo
        # grid_frame = ttk.Frame(notebook)
        # notebook.add(grid_frame, text='Grid Layout')
        # self.grid_demo(grid_frame)
        
        # # Place Layout Demo
        # place_frame = ttk.Frame(notebook)
        # notebook.add(place_frame, text='Place Layout')
        # self.place_demo(place_frame)
        
    def calculator_init(self, parent):
        #Initializes all default displays on calculator tab
        # Example of a label spanning multiple columns
        #tk.Label(parent, text="Spans 2 columns", bg='lightgray').grid(row=2, column=0, columnspan=2, sticky='ew', padx=5, pady=5)
        tk.Label(parent, text="Nutrient", bg='lightgray').grid(row=0, column=0, padx=5, pady=5)
        tk.Label(parent, text="Daily Amount", bg='lightgray').grid(row=0, column=1, padx=5, pady=5)
        tk.Label(parent, text="Running Amount", bg='lightgray').grid(row=0, column=2, padx=5, pady=5)
        tk.Label(parent, text="Food", bg='lightgray').grid(row=0, column=5, padx=5, pady=5)
        tk.Label(parent, text="Servings", bg='lightgray').grid(row=0, column=6, padx=5, pady=5)
        tk.Label(parent, text="Protein", bg='lightyellow').grid(row=1, column=0, padx=5, pady=5)
        tk.Label(parent, text=str(PROTEIN), bg='lightgreen').grid(row=1, column=1, padx=5, pady=5)
        tk.Label(parent, text="Carbs", bg='lightyellow').grid(row=2, column=0, padx=5, pady=5)
        tk.Label(parent, text=str(CARBS), bg='lightgreen').grid(row=2, column=1, padx=5, pady=5)
        tk.Label(parent, text="Fiber", bg='lightblue').grid(row=3, column=0, padx=5, pady=5)
        tk.Label(parent, text=str(FIBER), bg='lightgreen').grid(row=3, column=1, padx=5, pady=5)
        tk.Label(parent, text="Calcium", bg='lightblue').grid(row=4, column=0, padx=5, pady=5)
        tk.Label(parent, text=str(CALCIUM) + "mg", bg='lightgreen').grid(row=4, column=1, padx=5, pady=5)
        tk.Label(parent, text="Iron", bg='lightblue').grid(row=5, column=0, padx=5, pady=5)
        tk.Label(parent, text=str(IRON), bg='lightgreen').grid(row=5, column=1, padx=5, pady=5)
        tk.Label(parent, text="Magnesium", bg='lightblue').grid(row=6, column=0, padx=5, pady=5)
        tk.Label(parent, text=str(MAGNESIUM), bg='lightgreen').grid(row=6, column=1, padx=5, pady=5)
        tk.Label(parent, text="Phosphorus", bg='lightblue').grid(row=7, column=0, padx=5, pady=5)
        tk.Label(parent, text=str(PHOSPHORUS), bg='lightgreen').grid(row=7, column=1, padx=5, pady=5)
        tk.Label(parent, text="Sodium", bg='lightblue').grid(row=8, column=0, padx=5, pady=5)
        tk.Label(parent, text=str(SODIUM) + "mg", bg='lightgreen').grid(row=8, column=1, padx=5, pady=5)

        
        #Running nutrition values
        protein = 0
        carbs = 0
        fiber = 0
        calcium = 0
        iron = 0
        magnesium = 0
        phosphorus = 0
        sodium = 0
        #Running nutrition labels
        self.protein_label = tk.Label(parent, text=str(protein), bg='lightpink').grid(row=1, column=2, padx=5, pady=5)
        self.carbs_label = tk.Label(parent, text=str(carbs), bg='lightpink').grid(row=2, column=2, padx=5, pady=5)
        self.fiber_label = tk.Label(parent, text=str(fiber), bg='lightpink').grid(row=3, column=2, padx=5, pady=5)
        self.calcium_label = tk.Label(parent, text=str(calcium), bg='lightpink').grid(row=4, column=2, padx=5, pady=5)
        self.iron_label = tk.Label(parent, text=str(iron), bg='lightpink').grid(row=5, column=2, padx=5, pady=5)  
        self.magnesium_label = tk.Label(parent, text=str(magnesium), bg='lightpink').grid(row=6, column=2, padx=5, pady=5)
        self.phosphorus_label = tk.Label(parent, text=str(phosphorus), bg='lightpink').grid(row=7, column=2, padx=5, pady=5)
        self.sodium_label = tk.Label(parent, text=str(sodium), bg='lightpink').grid(row=8, column=2, padx=5, pady=5)

        #food entry fields
        self.foodTypeEntry = tk.Entry(parent, width = 20)
        self.foodTypeEntry.grid(row=18, column=5, padx=5, pady=5)
        self.foodServEntry = tk.Entry(parent, width = 5)
        self.foodServEntry.grid(row=18, column=6, padx=5, pady=5)
        
        #Enter Button
        self.foodRow = 1
        self.button = tk.Button(parent, text="Enter", command=lambda: self.add_food(parent)).grid(row=18, column=7, padx=5, pady=5)
    
        
    def add_food(self, parent): 
        print("addfood called")
        #adds a food item to the right of the screen in the row below the previous food
        #adds nutrients from the entry to the running values

        #Parse user input for food codes
        #This compares the user input to the names in the foodvalues list locted in Food_Values.py
        #If a match is reached, the food is added as a label to the display, 
        #Otherwise, it gives the message ("Food Unrecognized")
        foodE = self.foodTypeEntry.get()
        for element in foodValues:
            print("addfood for-loop entered")
            if foodE and foodValues[foodE]:
                print("entry and dictionary match")
                tk.Label(parent, text = foodE, bg='lightpink').grid(row=self.foodRow, column=5, padx=5, pady=5)
                tk.Label(parent, text=self.foodServEntry.get(), bg='lightpink').grid(row=self.foodRow, column=6, padx=5, pady=5)
                self.foodRow += 1
                print(str(self.foodRow))
                break
            
        #def clearAll:
            #clears calculator tab, clearing food entries and running nutrition values
        
        #def updateRunning(self, parent):
        #Updates labels to reflect current running nutrition variables
        


    def pack_demo(self, parent):
         #Pack arranges widgets in blocks
        tk.Label(parent, text="Top", bg='lightblue').pack(side='top', fill='x')
        tk.Label(parent, text="Left", bg='lightgreen').pack(side='left', fill='y')
        tk.Label(parent, text="Right", bg='lightpink').pack(side='right', fill='y')
        tk.Label(parent, text="Bottom", bg='lightyellow').pack(side='bottom', fill='x')

    def grid_demo(self, parent):
        # Grid arranges widgets in rows and columns
        tk.Label(parent, text="Row 0, Col 0", bg='lightblue').grid(row=0, column=0, padx=5, pady=5)
        tk.Label(parent, text="Row 0, Col 1", bg='lightgreen').grid(row=0, column=1, padx=5, pady=5)
        tk.Label(parent, text="Row 1, Col 0", bg='lightpink').grid(row=1, column=0, padx=5, pady=5)
        tk.Label(parent, text="Row 1, Col 1", bg='lightyellow').grid(row=1, column=1, padx=5, pady=5)
        
        # Span multiple columns
        tk.Label(parent, text="Spans 2 columns", bg='lightgray').grid(row=2, column=0, columnspan=2, sticky='ew', padx=5, pady=5)

    def place_demo(self, parent):
        # Place allows precise positioning using coordinates or relative positions
        tk.Label(parent, text="Absolute Position", bg='lightblue').place(x=50, y=50)
        tk.Label(parent, text="Relative Position", bg='lightgreen').place(relx=0.5, rely=0.5, anchor='center')
        tk.Label(parent, text="Bottom Right", bg='lightpink').place(relx=1.0, rely=1.0, anchor='se')

if __name__ == "__main__":
    root = tk.Tk()
    app = NutritionApp(root)
    root.mainloop()