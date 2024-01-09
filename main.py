import tkinter as tk
from tkinter import ttk
from trip_planner1 import TripPlanner

class TripPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("50 Shades Xplore!!!")
        # Set background color for the root window
        self.root.configure(bg='#CC99CC')
        self.heading=ttk.Label(root,text="Welcome to 50 Shades Xplore!!!\nWhere Your Adventure Awaits...",background="#CC99CC",foreground='#660066',font=('Times New Roman',27))
        self.heading.grid(row=0,column=3)

        # Example: Set foreground color for an entry widget
        self.destination_entry = ttk.Entry(root, foreground='#CC99CC')
        # Example: Set background and foreground color for a button
        style = ttk.Style()
        style.configure("TButton", background='#CC99CC', foreground='black')
        self.hotelcheck_button = ttk.Button(root, text="Check hotels", command=self.check_hotel, style="TButton")
        # Example: Set background and foreground color for a text widget
        self.results_text = tk.Text(root, height=200, width=500, state='normal', background='black', foreground='black')

        self.destination_label = ttk.Label(root, text="Destination:",background="#CC99CC",font=('Times New Roman',14))
        self.destination_entry = ttk.Entry(root)

        self.hotel_label = ttk.Label(root, text="Type of hotel(3/4/5 star):",background="#CC99CC",font=('Times New Roman',14))
        self.hotel_entry = ttk.Entry(root)

        self.people_label = ttk.Label(root, text="Total number of people:",background="#CC99CC",font=('Times New Roman',14))
        self.people_entry = ttk.Entry(root)

        self.children_label = ttk.Label(root, text="Number of Children:",background="#CC99CC",font=('Times New Roman',14))
        self.children_entry = ttk.Entry(root)

        self.budget_label = ttk.Label(root, text="Budget for trip:",background="#CC99CC",font=('Times New Roman',14))
        self.budget_entry = ttk.Entry(root)

        self.days_label = ttk.Label(root, text="No. of days:",background="#CC99CC",font=('Times New Roman',14))
        self.days_entry = ttk.Entry(root)

        self.hotelname_label = ttk.Label(root, text="Select the hotel:",background="#CC99CC",font=('Times New Roman',14))
        self.hotelname_entry = ttk.Entry(root)

        self.hotelcheck_button = ttk.Button(root, text="Check hotels", command=self.check_hotel,width=20)

        self.results_label = ttk.Label(root, text="Hotels under budget:",font=('Times New Roman',14),background='#CC99CC')
        self.results_text = tk.Text(root, height=10, width=50, state='disabled')

        self.Itinerary_button = ttk.Button(root, text="Plan Trip", command=self.plan_trip,width=20)

        self.results1_label = ttk.Label(root, text="Generated Itinerary:",font=('Times New Roman',14),background='#CC99CC')
        self.results1_text = tk.Text(root, height=10, width=50, state='disabled')

        self.print_button = ttk.Button(root, text="Print Itinerary", command=self.print_trip,width=20)

        self.destination_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.destination_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.people_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.people_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.children_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.children_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        self.hotel_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.hotel_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")
        self.days_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.days_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")
        self.budget_label.grid(row=6, column=0, padx=10, pady=10, sticky="e")
        self.budget_entry.grid(row=6, column=1, padx=10, pady=10, sticky="w")
        self.hotelcheck_button.grid(row=7, column=0, columnspan=2, pady=1)
        self.results_label.grid(row=8, column=0, columnspan=2, pady=1)
        self.results_text.grid(row=9, column=0, columnspan=2, pady=5,padx=50)
        self.Itinerary_button.grid(row=5, column=11, columnspan=2, pady=10)
        self.results1_label.grid(row=6, column=11, columnspan=2, pady=(15, 1))  # Adjusted position
        self.results1_text.grid(row=7, column=11, columnspan=2, pady=(5, 10))  # Adjusted position
        self.print_button.grid(row=9, column=11, columnspan=2, pady=(15, 10))


        self.hotelname_label.grid(row=3, column=11, padx=5, pady=5, sticky="e")
        self.hotelname_entry.grid(row=3, column=12, padx=5, pady=5, sticky="w")

    def check_hotel(self):
        destination = self.destination_entry.get()
        budget = float(self.budget_entry.get())
        hotel=self.hotel_entry.get()
        people=self.people_entry.get()
        print("p=", people)
        days=self.days_entry.get()
        children=self.children_entry.get()

        # Call the TripPlanner class to generate itinerary
        trip_planner = TripPlanner(destination, hotel)
        itinerary = trip_planner.generate_hotel( destination, people, days, budget)

        # Display the results
        self.results_text.config(state='normal')
        self.results_text.delete('1.0', tk.END)
        self.results_text.insert(tk.END, itinerary)
        self.results_text.config(state='disabled')

    def plan_trip(self):
        destination = self.destination_entry.get()
        budget = float(self.budget_entry.get())
        star=self.hotel_entry.get()
        people=self.people_entry.get()
        hotel=self.hotelname_entry.get()
        print("p=", people)
        days=self.days_entry.get()
        children=self.children_entry.get()

        # Call the TripPlanner class to generate itinerary
        trip_planner = TripPlanner(destination, star)
        itinerary = trip_planner.generate_plan(people, children, budget, days, hotel)

        # Display the results
        self.results1_text.config(state='normal')
        self.results1_text.delete('1.0', tk.END)
        self.results1_text.insert(tk.END, itinerary)
        self.results1_text.config(state='disabled')

    def print_trip(self):
        destination = self.destination_entry.get()
        budget = float(self.budget_entry.get())
        star=self.hotel_entry.get()
        people=self.people_entry.get()
        hotel=self.hotelname_entry.get()
        print("p=", people)
        days=self.days_entry.get()
        children=self.children_entry.get()
        itinerary="\t\t\t\t\t\tWelcome to 50 Shades Xplore!!!!\n\nYour trip Itinerary is: \n\n"

        # Call the TripPlanner class to generate itinerary
        trip_planner = TripPlanner(destination, star)
        itinerary += trip_planner.generate_plan(people, children, budget, days, hotel)

        # Specify the file path
        file_path = "Itinerary.txt"

        # Open the file in write mode ('w' for writing)
        with open(file_path, 'w') as file:
            # Write the output string to the file
            file.write(itinerary)

        print(f"Output string has been written to {file_path}")



if __name__ == "__main__":
    root = tk.Tk()
    app = TripPlannerApp(root)
    root.mainloop()
