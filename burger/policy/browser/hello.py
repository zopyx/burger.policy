from Products.Five.browser import BrowserView

class HelloView(BrowserView):

    def helper(self):
        return [ dict(key='a', value=1),
                 dict(key='b', value=2),
                 dict(key='c', value=3)]
