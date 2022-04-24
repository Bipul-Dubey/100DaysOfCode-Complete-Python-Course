# args -> positional argument   *positional_argument_name
# kwargs -> keywords argument **keyword_argument_name

class User:
    def __init__(self,name):
        self.name=name
        self.is_login=False


def is_authentication_decorator(function):
    def wrapper(*args):
        if args[0].is_login:
            function(args[0])
    return wrapper


@is_authentication_decorator
def create_blog_post(user):
    print(f"Hey there, {user.name} is login now.")


new_user=User('Bipul')
new_user.is_login=True
create_blog_post(new_user)
