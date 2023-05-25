class TravelDestinationRecommender:
    def __init__(self):
        self.destination_data = {
            "beach": ["Maldives", "Hawaii", "Bali"],
            "mountain": ["Switzerland", "Nepal", "Canada"],
            "city": ["Paris", "New York", "Tokyo"],
            # Add more destination categories and their corresponding locations
        }

    def recommend_destination(self, preferences):
        recommended_destinations = []

        for preference in preferences:
            if preference in self.destination_data:
                recommended_destinations.extend(self.destination_data[preference])

        return recommended_destinations

# Example usage
destination_recommender = TravelDestinationRecommender()

preferences = ["beach", "city"]
recommended_destinations = destination_recommender.recommend_destination(preferences)

print("Recommended Destinations:")
for destination in recommended_destinations:
    print("-", destination)
