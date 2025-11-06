class Car:
     ## this is needed to construct object
    def __init__(self, model, year, color, for_sale):
        
        # attributes for the car class
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

        # methods are actions that object can perform

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"you stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")