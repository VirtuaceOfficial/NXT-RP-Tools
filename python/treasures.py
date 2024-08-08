class ItemTracker:
    def __init__(self):
        self.total_cash = 0
        self.total_rings = 0
        self.total_watches = 0
        self.num_inputs = 0

    def add_items(self, cash, rings, watches):
        self.total_cash += cash
        self.total_rings += rings
        self.total_watches += watches
        self.num_inputs += 1

    def display_totals_and_averages(self):
        if self.num_inputs == 0:
            avg_cash = avg_rings = avg_watches = 0
        else:
            avg_cash = self.total_cash / self.num_inputs
            avg_rings = self.total_rings / self.num_inputs
            avg_watches = self.total_watches / self.num_inputs

        print(f"\nTotal Cash: {self.total_cash}")
        print(f"Total Rings: {self.total_rings}")
        print(f"Total Watches: {self.total_watches}\n")
        print(f"Number of Inputs: {self.num_inputs}\n")
        print(f"Average Cash: {avg_cash:.2f}")
        print(f"Average Rings: {avg_rings:.2f}")
        print(f"Average Watches: {avg_watches:.2f}\n\n")

def main():
    tracker = ItemTracker()
    while True:
        try:
            cash = float(input("Enter the amount of Cash: "))
            rings = int(input("Enter the number of Rings: "))
            watches = int(input("Enter the number of Watches: "))
            tracker.add_items(cash, rings, watches)
            tracker.display_totals_and_averages()
        except ValueError:
            print("Invalid input, please enter numeric values.")

if __name__ == "__main__":
    main()
