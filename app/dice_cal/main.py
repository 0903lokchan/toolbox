from decimal import Decimal

# deault precision of decimal package is 28, which is more than enough for our target precision for output (6 d.p.)
class TooManyCombinationsError(ValueError):
    """Exception raised for when the total number of possible combination of dice outcomes exceeded limit.

    Attributes:
        combination_n (int): The number of possible combinations from user input
        message (str): Error message
    """
    
    def __init__(self, combination_n: int, message: str="Number of possible cmobinations exceeded 10000", *args: object) -> None:
        self.combination_n = combination_n
        self.message = message
        super().__init__(self.message, *args)
        
    def __str__(self) -> str:
        return f"{self.combination_n} -> {self.message}"

def simulate(dice_n: int, side_n: int) -> dict[int,Decimal]:
    """Calculates the possibilities of every outcome of a given dice set by simulation. It is assumed that all dice are 
    prefectly fair and have same faces. Return a dictionary of outcomes and possibilitie or an error string when the 
    total number of possible instances is over 1000.

    Args:
        dice_n (int): the number of dice.
        side_n (int): the number of face of each dice.

    Returns:
        dict[int,Decimal]|str: dict with dice outcome as key and its possibility in percentage as value. If the total 
        number of possible instances is over 1000, an error message as string is returned instead.
    """

    case_count = side_n**dice_n
    if case_count > 10000:
        raise TooManyCombinationsError(case_count)

    min_face = 1
    max_face = side_n
    # create a dictionary of possible outcomes : number of instances
    outcome_range = range(min_face*dice_n, max_face*dice_n+1)
    outcome_instance_dict = dict.fromkeys(outcome_range, 0)
    
    # create a set of dice with min face
    dice_tray = [min_face] * dice_n
    
    # keep incrementing the dice until all combinations are iterated over
    while True:
        # if any die exceeds its max face, turn it back to min face
        for position, die in enumerate(dice_tray):
            if die > max_face:
                dice_tray[position] = min_face
                #increment the next die by 1
                dice_tray[position+1] += 1
                
        # calculate the sum of dice and add count to outcome_instance_dict
        outcome = sum(dice_tray)
        outcome_instance_dict[outcome] += 1
        
        # if all dice are at max face, break out from the loop
        if all(dice == max_face for dice in dice_tray):
            break
        # else increment the first dice by 1
        dice_tray[0] += 1
    
    # calculate the possibility of occurrence of an instance  
    inst_prob = Decimal(1)/case_count
    output = {outcome: round(count * inst_prob * 100, 6) for outcome, count in outcome_instance_dict.items()}
    return output

