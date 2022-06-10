from decimal import Decimal

# deault precision of decimal package is 28, which is more than enough for our target precision for output (6 d.p.)

def simulate(dice_n: int, side_n: int) -> dict[int,Decimal]|str:
    """Calculates the possibilities of every outcome of a given dice set by simulation. It is assumed that all dice are 
    prefectly fair and have same faces. Return a dictionary of outcomes and possibilitie or an error string when the 
    total number of possible instances is over 1000.

    Args:
        dice_n (int): the number of dice.
        side_n (int): the number of face of each dice.

    Returns:
        dict[int,Decimal]|str: dict with dice outcome as key and its possibility as value. If the total number of
        possible instances is over 1000, an error message as string is returned instead.
    """

    case_count = side_n**dice_n
    if case_count > 1000:
        return "Sorry, the simulation is run on server-side so I have limited the maximum number of results to 1000 in \
    order to prevent overloading. Please use a smaller combination of input."

    min_face = 1
    max_face = side_n
    # create a dictionary of possible outcomes : number of instances
    outcome_range = range(min_face*dice_n, max_face*dice_n+1)
    outcome_instance_dict = dict.fromkeys(outcome_range, 0)
    
    # create a set of dice with min face
    dice_tray = [min_face] * dice_n
    
    # increment the last dice by 1 each time, until all dice are at max face
    while not all(dice == max_face for dice in dice_tray):
        dice_tray[-1] += 1
        
        # if any die exceeds its max face, turn it back to min face
        for position, die in enumerate(dice_tray):
            if die > max_face:
                die = min_face
                #increment the die in the front
                dice_tray[position-1] += 1
                
        # calculate the sum of dice and add count to outcome_instance_dict
        outcome = sum(dice_tray)
        outcome_instance_dict[outcome] += 1
    
    # calculate the possibility of occurrence of an instance  
    inst_prob = Decimal(1)/case_count
    output = {outcome: round(count * inst_prob, 6) for outcome, count in outcome_instance_dict.items()}
    return output