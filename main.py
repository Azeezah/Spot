from screenshot import takeScreenshot

def triggerLogin():
    '''Trigger Auth0 and collect email address.'''
    pass

def reportDogSighting(userid):
    '''Reports dog sighting to server.'''
    pass

def displayDogs(dogs):
    '''
    Send dogs to electron for display.
    This can be asynchronous if we can remove the display dogs from the screenshot.
    '''
    pass

def getFriendDogsSightings():
    '''Requests list of friends' dog sightings from flask server.'''
    pass

def detectDog(imgFilename):
    pass

if __name__ == '__main__':
    userid = triggerLogin()
    while True:
        if detectDog(takeScreenshot()):
            reportDogSighting(userid)
        dogs_of_friends = getFriendDogsSightings()
        displayDogs(dogs_of_friends)
