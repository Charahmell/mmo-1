
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate bake time remaining"""
    return EXPECTED_BAKE_TIME - elapsed_bake_time
def preparation_time_in_minutes(number_of_layers):
    """Calculate the prep time if each number of layers takes two minutes.
    param number of layers : int -  the number of layers of lasagna multiplied by two.

    it takes an integer multiplies it by two and returns number of layers 
    """
    number_of_layers *= 2
    return number_of_layers
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total time spent cooking the lasagna
    Args:
    number_of_layers(int)
    elapsed_bake_time(int)
    returns:
    Total time in minutes spent preparing and baking
    """
    time_spent_cooking = preparation_time_in_minutes(number_of_layers)
    return time_spent_cooking + elapsed_bake_time








