def total(galleons, sickles, knuts):
    return (galleons *17 + sickles)*29 +knuts

coins={"galleons":100, "sickles": 50, "knuts": 25}

print(total(**coins), "knuts")
# ** unpacks coins into galleons=100, sickles=50, knuts=25
# these fit as arguments of total function