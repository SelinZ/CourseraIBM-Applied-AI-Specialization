#Method Decorators

"""Let’s say we have a python code where we want all the output to be in JSON format. It doesn’t make sense to include code for these in each of the 
methods as it makes the lines of code redundant. In such cases, we can handle this with a decorator."""

def jsonify_decorator(function):
    def modifyOutput():
        return {"output":function()}
    return modifyOutput
@jsonify_decorator
def hello():
    return 'hello world'
@jsonify_decorator
def add():
    num1 = input("Enter a number - ")
    num2 = input("Enter another number - ")
    return int(num1)+int(num2)
print(hello())
print(add())

#Route Decorators
"""You may have observed when you visit any domain you have the root and then have other end-points you can access. See the examples below.
We can handle multiple routes with a single function by just stacking additional route decorators above the method which should be invoked when the route is called. 
The following is a valid example of serving the same “Hello World!” message for 3 separate routes:
"""
@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return "Hello World!"


"""The route decorator can also be more specific. For example, to get the details of a user whose userId is U0001, you may go to
http://mydomain.com/userdetails/U0001. It doesn’t make sense to define a different route for each user you may be dealing with. In such cases, we define the route like this."""

@app.route("/userdetails/<userid>")
def getUserDetails(userid):
    return "User Details for  "+userid