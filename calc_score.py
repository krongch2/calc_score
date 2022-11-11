# comment
def read_structure(fn):
    with open(fn) as f:
        text = f.read()
    structure = []
    for nuct in text:
        structure.append(nuct)
    return structure

def read_reactivity(fn):
    with open(fn) as f:
        text = f.read()
    lines = text.split('\n')
    result = []
    for line in lines:
        if not line == '':
            result.append(float(line))
    return result

def get_subset(reacts, start, end):
    '''
    get items from [start, end] inclusive
    '''
    react = reacts[start - 1:end]
    return react

def test_reactivity():
    reacts = [5, 9, 3, 8, 4, 6, 7, 9, 9, 4]
    start = 3
    end = 5
    print(get_subset(reacts, start, end))

def calc_score_pct(subset, structure):
    '''
    returns score in percentage
    '''
    score = 0
    n = len(subset)
    for idx in range(n):
        react = subset[idx]
        nuct = structure[idx]
        if nuct == 'X' and react < 0.50:
            score += 1
        elif nuct == '.' and react > 0.25:
            score += 1
    return score/n*100

if __name__ == '__main__':
    # input
    reacts = read_reactivity('reacts_1-7.txt')
    start = 24
    end = 307
    structure = read_structure('structure.txt')

    subset = get_subset(reacts, start, end)
    score_pct = calc_score_pct(subset, structure)
    print(score_pct)


