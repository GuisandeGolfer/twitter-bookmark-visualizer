from twitter.account import Account
from twitter.search import search

username, password = "@guisande4", "Diegito23!"

account = Account(username, password)

account.tweet("test tweet from twitter-api-client 123")

'''
    https://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html#web-application-flow

    This is where I can use requests with the Twitter Oauth2 requirements
    found in the Developer portal.

    use fast_api credential section of FCC youtube video
    to help use environment variables so secrets and URI are
    kept hidden.

'''
