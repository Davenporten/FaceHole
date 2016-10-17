This is a hack solution which isn't very stable. 

It uses selenium to open a browser, navigates to the about page, clicks on needed buttons, and injects your public key.

The problems with this solution are 
- that if there is even just one change to any of the tags that are used it will break
- a browser must be open to use it (I haven't looked into if Selenium can open a browser in the background)
- you need to put needed information for login, etc, manually
- the public key must be perfectly formatted in the source code for fb to save it

There are probably other problems, but those are the major ones. The ideal, which is what I'm going for in the GraphSolution folder is to be able to somehow save a public key to fb in a stable way that won't require opening a browser and will be stable regardless of any changes fb might make to their site. 
