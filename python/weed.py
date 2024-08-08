class ItemTracker:
    def __init__(self):
        self.total_cash = 0
        self.total_bags = 0
        self.total_stolen = 0
        self.num_inputs = 0

    def add_items(self, cash, bags, stolen):

        self.total_cash += cash
        self.total_bags += bags
        self.total_stolen += stolen
        self.num_inputs += 1

    def display_totals_and_averages(self):
        if self.num_inputs == 0:
            avg_cash = avg_bags = avg_stolen = 0
        else:
            avg_cash = self.total_cash / self.num_inputs
            avg_bags = self.total_bags / self.num_inputs
            avg_stolen = self.total_stolen / self.num_inputs

        print(f"\nTotal Cash: {self.total_cash}")
        print(f"Total bags: {self.total_bags}")
        print(f"Total stolen: {self.total_stolen}\n")
        print(f"Number of Inputs: {self.num_inputs}\n")
        print(f"Average Cash: {avg_cash:.2f}")
        print(f"Average bags: {avg_bags:.2f}")
        print(f"Average stolen: {avg_stolen:.2f}\n\n")

def main():
    tracker = ItemTracker()
    while True:
        try:
            cash = float(input("Enter the amount of Cash: "))
            bags = int(input("Enter the number of bags: "))
            stolen = int(input("Enter the number of stolen: "))
            tracker.add_items(cash, bags, stolen)
            tracker.display_totals_and_averages()
        except ValueError:
            print("Invalid input, please enter numeric values.")

if __name__ == "__main__":
    main()
