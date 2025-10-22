# D'Hondt method

class Result():
    def __init__(self, fullName: str, committee: str, votes: int):
        self.fullName = fullName
        self.committee = committee
        self.votes = votes

def computeQuotients(commitee_votes, places):
    """
    Compute the quotients limited to the number of places.

    :param commitee_votes: the eligible committees and voites
    :param places: the number of places
    :return: the list of quotients and places
    """
    quotients = []

    for committee, votes in commitee_votes.items():

        for i in range(1, places + 1):
            quotient = (votes / i, committee)
            quotients.append(quotient)

    quotients.sort(reverse=True, key=lambda x: x[0])
    return quotients[:places]

def mapVotesToCommittees(results):
    """
    Maps the committee names into the number of votes.
    Only eligable committees are included.

    :param results: the voting results
    :return: mapping between names and votes
    """
    total_number_of_votes = sum(list(map(lambda x: x.votes, results)))
    votes_threshold = total_number_of_votes * 0.05
    commitee_votes = {}

    for committee in set(map(lambda x: x.committee, results)):
        commitee_results = list(filter(lambda x: x.committee == committee, results))
        commitee_total_result = sum(list(map(lambda x: x.votes, commitee_results)))

        if commitee_total_result >= votes_threshold:
            commitee_votes[committee] = commitee_total_result

    return commitee_votes

def votingResults(results, places):
    """
    Provides the list of elected members.

    :param results: the voting results
    :param places: the number of places
    :return: the list of elected members
    """
    commitee_votes = mapVotesToCommittees(results)
    mandates = {}

    for _, committee in computeQuotients(commitee_votes, places):
        mandates[committee] = mandates.get(committee, 0) + 1

    elected = []

    for committee, count in mandates.items():
        members = [r for r in results if r.committee == committee]
        members.sort(reverse=True, key=lambda x: x.votes)
        elected.extend(m.fullName for m in members[:count])

    return elected

# We have committees B, D and Z, that received 720, 300 and 480 votes.
results = [Result("A.B.", "B", 200),
           Result("G.B.", "B", 120),
           Result("E.B.", "B", 200),
           Result("D.B.", "B", 200),
           Result("D.D.", "D", 150),
           Result("C.D.", "D", 50),
           Result("E.D.", "D", 50),
           Result("X.Z.", "Z", 80),
           Result("Y.Z.", "Z", 200),
           Result("F.Z.", "Z", 200)]
# There are 8 places.
print(votingResults(results, 8))
