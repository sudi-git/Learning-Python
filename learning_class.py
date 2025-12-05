class Vehicle:
    def __init__(self, name="", kind="car", color="", value=100.00):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (
            self.name,
            self.color,
            self.kind,
            self.value,
        )
        return desc_str


# Creating two car objects
car1 = Vehicle("Fer", "convertible", "red", 60000.00)
car2 = Vehicle("Jump", "van", "blue", 10000.00)

# Printing descriptions
print(car1.description())
print(car2.description())
