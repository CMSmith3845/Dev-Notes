message = "a"

# this variable is a global variable, since it is outside of the function, so we can access it anywhere from within this
# file, this file is it's scope, global variables stay in memory longer than local, and so you should not use them that
# often if able to.


def greet(name):
    message = 'a'

# This variable is within a function, that is its scope, it works the same for any parameters inside the function, these
# types of variables are local to fuction, which means we can have a different fuction that uses the same variable but
# won't affect the one is the first function, like this.


def send_email(name):  # the name in this function is different than the one up top
    message = "b"  # the variable in this function is different than the one up top

# for local variable python will only store them in memory until the function is finished executing and then if they
# are not referenced anywhere else they get thrown out.


# this will create an error because of the scope of message being inside the function up top
print(message)
