import falcon
from time import sleep


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class NEOResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        query_items = req.params['args'].split('%')
        command = " ".join(query_items)
        print(command)

        f = open('com.txt', 'w')
        f.write(command)
        f.close()
        sleep(2)
        f = open('out.txt', 'r')
        output = f.read()
        f.close()

        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = output

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
nrs = NEOResource()

# things will handle all requests to the '/things' URL path
app.add_route('/NEO', nrs)