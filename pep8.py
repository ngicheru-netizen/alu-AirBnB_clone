"""Simple PEP 8-compliant property listing example."""


class Property:
    """Represent a property available for booking."""

    def __init__(self, title, city, price_per_night):
        """Initialize a property listing."""
        self.title = title
        self.city = city
        self.price_per_night = price_per_night

    def summary(self):
        """Return a short description of the property."""
        return f"{self.title} in {self.city}: " \
            f"${self.price_per_night:.2f} per night"


def affordable_properties(properties, maximum_price):
    """Return properties at or below the maximum nightly price."""
    return [
        property_listing
        for property_listing in properties
        if property_listing.price_per_night <= maximum_price
    ]


def main():
    """Display affordable property listings."""
    properties = [
        Property("Cozy studio", "Nairobi", 35.00),
        Property("City apartment", "Mombasa", 60.00),
        Property("Garden cottage", "Nakuru", 45.00),
    ]

    for property_listing in affordable_properties(properties, 50.00):
        print(property_listing.summary())


if __name__ == "__main__":
    main()
