import requests

NOMINATIM_BASE_URL = "https://nominatim.openstreetmap.org/search"

def find_resources():
    """Retrieve general mental health resources."""
    resources = [
        {
            "name": "National Suicide Prevention Lifeline",
            "contact": "1-800-273-8255",
            "description": "24/7 support for people in distress."
        },
        {
            "name": "Substance Abuse and Mental Health Services",
            "contact": "1-800-662-HELP (4357)",
            "description": "Free and confidential treatment referral and information service."
        },
        {
            "name": "Crisis Text Line",
            "contact": "Text HOME to 741741",
            "description": "Text-based support for those in crisis."
        }
    ]

    formatted_resources = "Here are some helpful mental health resources:\n\n"
    for resource in resources:
        formatted_resources += f"**{resource['name']}**\nContact: {resource['contact']}\n{resource['description']}\n\n"

    return formatted_resources


def get_location_based_resources(location):
    """Retrieve location-based mental health resources using Nominatim."""
    try:
        # Search for "mental health services" near the location
        params = {
            'q': f"mental health services near {location}",
            'format': 'json',
            'limit': 3
        }
        response = requests.get(NOMINATIM_BASE_URL, params=params)
        data = response.json()

        if len(data) == 0:
            return f"Sorry, I couldn't find any mental health services near {location}. Please try another location."

        formatted_resources = f"Mental health resources near {location}:\n\n"

        for place in data:
            name = place.get('display_name', 'Unknown')
            lat = place.get('lat', 'N/A')
            lon = place.get('lon', 'N/A')
            formatted_resources += f"**{name}**\nCoordinates: {lat}, {lon}\n\n"

        return formatted_resources

    except Exception as e:
        print(f"Error fetching location-based resources: {e}")
        return "Sorry, there was an error finding mental health resources in your area."
