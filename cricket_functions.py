p1 = {'name': 'Virat Kohli', 'role': 'bat', 'runs': 112, '4': 10, '6': 0, 'balls': 119, 'field': 0}
p2 = {'name': 'du Plessis', 'role': 'bat', 'runs': 120, '4': 11, '6': 2, 'balls': 112, 'field': 0}
p3 = {'name': 'Bhuvneshwar Kumar', 'role': 'bowl', 'wkts': 1, 'overs': 10, 'runs': 71, 'field': 1}
p4 = {'name': 'Yuzvendra Chahal', 'role': 'bowl', 'wkts': 2, 'overs': 10, 'runs': 45, 'field': 0}
p5 = {'name': 'Kuldeep Yadav', 'role': 'bowl', 'wkts': 3, 'overs': 10, 'runs': 34, 'field': 0}

# batting_points Function:

def batting_function(dict):
    runs = dict.get("runs")
    balls_faced = dict.get("balls")
    strike_rate = int((runs / balls_faced) * 100)
    fours = dict.get("4")
    sixes = dict.get("6")
    batting_points = 0
    if runs >= 50:
        batting_points += 5
    if runs >= 100:
        batting_points += 10
    if strike_rate in range(80, 101):
        batting_points += 2
    if strike_rate > 100:
        batting_points += 4
    if fours > 0:
        batting_points += fours * 1
    if sixes > 0:
        batting_points += sixes * 2
    batting_points += runs // 2
    print("Finally {} got {} points in batting".format(dict.get("name"), batting_points))
    return batting_points


# bowling_points Function:

def bowling_function(dict):
    wickets_taken = dict.get("wkts")
    overs_bowled = dict.get("overs")
    runs_given = dict.get("runs")
    economy_rate = runs_given // overs_bowled
    bowling_points = 0
    bowling_points += wickets_taken * 10
    if wickets_taken == 3:
        bowling_points += 5
    if wickets_taken >= 5:
        bowling_points += 10
    if 3.5 < economy_rate < 4.5:
        bowling_points += 4
    elif 2 < economy_rate < 3.5:
        bowling_points += 7
    elif economy_rate < 2:
        bowling_points += 10
    print("Finally {} got {} points in bowling".format(dict.get("name"), bowling_points))
    return bowling_points


def fielding_function(dict):
    no_of_fields = dict.get("field")
    fielding_points = 0
    fielding_points += no_of_fields * 10
    print("Finally {} got {} points in fielding".format(dict.get("name"), fielding_points))
    return fielding_points
