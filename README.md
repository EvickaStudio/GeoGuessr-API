# GeoGuessr API

This Python script contains a list of endpoints for the GeoGuessr API. It uses the `requests` library to make HTTP requests to the API and retrieve data.

## Getting Started

To use this script, you'll need to have Python 3 installed on your computer. You can download it from the official website: https://www.python.org/downloads/

You'll also need to install the `requests` library. You can do this by running the following command in your terminal:

`pip install requests`

### Authentication

To access the most endpoint, you'll need to provide a `_ncfa` cookie. You can extract this cookie from your browser by following these steps:

1. Open the GeoGuessr website in your browser and log in to your account.
2. Open the developer tools in your browser.
3. Navigate to the "Network" tab in the developer tools.
4. Refresh the page to capture the network traffic.
5. Look for a request like to the `profiles` endpoint in the network traffic.
6. Click on the request to open it.
7. In the request headers, look for the `_ncfa` cookie and copy its value.
8. Paste the `_ncfa` token into the script where indicated.

## Usage

To use the script, simply run it from the command line:

`python main.py`

This script sends a GET request to the GeoGuessr API using the endpoint you set and prints the response to the console.

## API Endpoints

The following API endpoints are available:

- v3/accounts/delete
- v3/accounts/signin
- v3/apple/signin
- v3/experiments
- v3/facebook/signin
- v3/games
- v3/games/streak
- v3/googleplus/signin
- v3/likes
- v3/profiles
- v3/profiles/maps
- v3/profiles/pin
- v3/profiles/resetpassword
- v3/profiles/setpassword
- v3/scores/maps
- v3/search/user
- v3/social/badges/claim
- v3/social/badges/unclaimed
- v3/social/events/unfinishedgames
- v3/social/friends
- v3/social/friends/received
- v3/social/maps/browse/featured
- v3/social/maps/browse/popular/all
- v3/social/maps/browse/popular/official
- v3/subscriptions
- v3/subscriptions/google
- v3/subscriptions/plans
- v3/version/update
- v4/app/ads/reward
- v4/app/features/android
- v4/app/logs
- v4/app/onboarding/completed
- v4/app/state
- v4/chat/emotes
- v4/feed/friends
- v4/feed/private
- v4/games/infinity
- v4/games/infinity/challenge/new
- v4/games/infinity/challenge/random
- v4/games/infinity/challenges
- v4/games/infinity/guess
- v4/games/infinity/history
- v4/games/infinity/inbox
- v4/games/infinity/location-overview
- v4/games/infinity/next
- v4/games/infinity/outbox
- v4/games/infinity/share
- v4/games/infinity/shared-location
- v4/parties
- v4/pushnotification/register
- v4/search/map

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
