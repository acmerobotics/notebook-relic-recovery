from template import *
import os

def getTableBegin(title):
    return tableBeginTemplate.replace('title', title)

def getTableRow(goal, description, outcome):
    return tableRowTemplate.replace('goal', goal).replace('description', description).replace('outcome', outcome)

def getGoalBegin(goal):
    return goalBeginTemplate.replace('goal', goal)

def getFigure(path):
    return figureTemplate.replace('path', path)

'''
file = open('./out/test.tex', 'w+')
file.write(preamble)
file.write(r'\begin{document}')
file.write(weekBegin)
file.write(getTableBegin('Software Goals'))
file.write(getTableRow('test', 'test test test', 'test test test test'))
file.write(getTableRow('test', 'test test test', 'test test test test'))
file.write(tableEnd)
file.write(getGoalBegin('Software Goal 1'))
file.write(r'\lipsum')
file.write(r'\end{document}')
'''

tex = open('./out/notebook.tex', 'w+')
tex.write(preamble)
tex.write(r'\begin{document}')

weeks = os.listdir("./temp")
for week in weeks:
    tex.write(weekBegin)
    teams = os.listdir('./temp/' + week)
    writing = []
    for team in teams:
        if '.csv' not in team: continue
        name = 'Software'
        if 'b' in team: name = 'Business'
        elif 'h' in team: name = 'Hardware'
        writing.append([name, []])        

        file = open('./temp/' + week + '/' + team)
        file = file.read()
        file = file.replace('%', r'\%')
        file = file.split('\n')
        lines = []
        for line in file:
            if not line.startswith('\t'): lines.append(line.split('\t'))

        for i in range(3, len(lines)):
            writing[-1][1].append(lines[i])

    for team in writing:
        tex.write(getTableBegin(team[0] + ' Goals'))
        for entry in team[1]:
            if len(entry) > 2: tex.write(getTableRow(entry[0], entry[1], entry[2]))
        tex.write(tableEnd)

    for team in writing:
        for i in range(0, len(team[1])):
            if len(team[1][i]) < 3: continue
            tex.write(getGoalBegin(team[0] + ' ' + str(i) + ': ' + team[1][i][0]))
            tex.write(team[1][i][3])

tex.write(r'\end{document}')
tex.close
