import requests

# GeoGuessr API
# [!] All Endpoints extracted from Android app version 2.8.2
#   API Endpoints:
#       v3/accounts/delete
#       v3/accounts/signin
#       v3/apple/signin
#       v3/experiments
#       v3/facebook/signin
#       v3/games
#       v3/games/streak
#       v3/googleplus/signin
#       v3/likes
#       v3/profiles
#       v3/profiles/maps
#       v3/profiles/pin
#       v3/profiles/resetpassword
#       v3/profiles/setpassword
#       v3/scores/maps
#       v3/search/user
#       v3/social/badges/claim
#       v3/social/badges/unclaimed
#       v3/social/events/unfinishedgames
#       v3/social/friends
#       v3/social/friends/received
#       v3/social/maps/browse/featured
#       v3/social/maps/browse/popular/all
#       v3/social/maps/browse/popular/official
#       v3/subscriptions
#       v3/subscriptions/google
#       v3/subscriptions/plans
#       v3/version/update
#       v4/app/ads/reward
#       v4/app/features/android
#       v4/app/logs
#       v4/app/onboarding/completed
#       v4/app/state
#       v4/chat/emotes
#       v4/feed/friends
#       v4/feed/private
#       v4/games/infinity
#       v4/games/infinity/challenge/new
#       v4/games/infinity/challenge/random
#       v4/games/infinity/challenges
#       v4/games/infinity/guess
#       v4/games/infinity/history
#       v4/games/infinity/inbox
#       v4/games/infinity/location-overview
#       v4/games/infinity/next
#       v4/games/infinity/outbox
#       v4/games/infinity/share
#       v4/games/infinity/shared-location
#       v4/parties
#       v4/pushnotification/register
#       v4/search/map

BASE_URL = "https://www.geoguessr.com/api/v3/"  # Base URL for all endpoints
_ncfa_TOKEN = ""  # Insert your _ncfa token here

# Create a session object and set the _ncfa cookie
session = requests.Session()
session.cookies.set("_ncfa", _ncfa_TOKEN, domain="www.geoguessr.com")

# Send a GET request to the profiles endpoint
profiles = session.get(f"{BASE_URL}profiles")

# Check if the request was successful
if profiles.status_code == 200:
    # Print the response as text
    print(profiles.text)
else:
    # Print an error message
    print(f"Error: {profiles.status_code}")
