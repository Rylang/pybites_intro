MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    """Print name is allowed / not allowed to drive based on MIN_DRIVING_AGE"""
    if age >= MIN_DRIVING_AGE:
        print("{} is allowed to drive".format(name))
    else:
        print("{} is not allowed to drive".format(name))
