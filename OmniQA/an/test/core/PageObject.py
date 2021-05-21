class PageObject(object):
    webdriver = None

    def __init__(self, webdriver, config):
        self.webdriver = webdriver
        self.config = config

        #self._validate_page(self.webdriver)

    # Abstract method
    def _validate_page(self, webdriver):
        """
        Run checks to validate that current page is the correct target page.
        """
        raise Exception("The _validate_page() method must be implemented in the PageObject based class")

class InvalidPageError(Exception):
    """
    Thrown when incorrect page is instantiated.
    """