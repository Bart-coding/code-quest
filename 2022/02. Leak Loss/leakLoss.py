def leakLoss(input: str) -> int:
    poolVolume, rateOfFill, rateOfLeak = (int(x) for x in input.split(" "))
    return round(poolVolume * rateOfLeak / (rateOfFill - rateOfLeak))