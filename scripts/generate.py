from template import *
import os
import datetime

def getTableBegin(title):
    return tableBeginTemplate.replace('title', title)

def getTableRow(goal, description, outcome):
    return tableRowTemplate.replace('goal', goal).replace('description', description).replace('outcome', outcome)

def getGoalBegin(goal):
    return goalBeginTemplate.replace('goal', goal)

def getFigure(path, name):
    return figureTemplate.replace('path', path).replace('name', name).replace('captionr', caption)

def getEq(value, name):
    return eqTemplate.replace('value', value).replace('name', name)


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
tex.write(r'\tableofcontents')
tex.write(r'\newpage')

weeks = os.listdir("./temp")
for week in weeks:
    tex.write(weekBegin)
    teams = os.listdir('./temp/' + week)
    writing = []
    firstTeam = True
    for team in teams:
        if 'schedule.pdf' in team:
            tex.write(scheduleTemplate.replace('file', '../temp/' + week + '/' + 'schedule.pdf'))
        if '.csv' not in team: continue
        name = 'Software'
        if 'b' in team: name = 'Business'
        elif 'h' in team: name = 'Hardware'
        writing.append([name, []])        

        file = open('./temp/' + week + '/' + team)
        file = file.read()
        file = file.replace('%', r'\%')
        #file = file.replace('$', r'\$')
        file = file.split('\n')

        if firstTeam:
            firstTeam = False
            startDate = file[0].split('\t')[1]
            numbers = startDate.split('/')
            startDate = datetime.date(2017, int(numbers[0]), int(numbers[1]))
            enddate = startDate + datetime.timedelta(days=6)
            tex.write(startDate.strftime('%d %B %Y'))
        
        lines = []
        for line in file:
            if not line.startswith('\t'): lines.append(line.split('\t'))

        for i in range(3, len(lines)):
            if len(lines[i]) > 3:
                if len(lines[i][3]) > 10:
                    writing[-1][1].append(lines[i])


                    
    done = []
    for team in writing:
        counter = 1
        if team[0] in done: continue
        done.append(team[0])
        tex.write(r'\subsection{' + str(team[0]) + r' Goals}')
        for entry in team[1]:
            if len(entry) > 2:
                entry[0] = '{} {}: {}'.format(team[0][0], counter, entry[0])
                counter += 1
                tex.write(r'\paragraph{' + entry[0] + '}' + entry[1])

    tex.write(r'\newpage')
                          

    done = []
    for team in writing:
        if team[0] in done: continue
        done.append(team[0])
        for i in range(0, len(team[1])):
            if len(team[1][i]) < 3: continue
            title = team[1][i][0]
            body = team[1][i][3]
            body = body.split('<')
            for i in range(1, len(body)):
                filename = body[i].split('>')[0]
                caption = ''
                if ',' in filename:
                    caption = filename.split(',')[1]
                    #print caption
                    filename = filename.split(',')[0]
                body[i] = body[i].split('>')[1]
                body[i] = r'Figure \ref{fig:' + filename.split('.')[0] + r'}' + body[i]
                body[i] = getFigure('../temp/{}/{}'.format(week, filename, caption), filename.split('.')[0]) + '\n' + body[i]
            body = ' '.join(body)

            while '#' in body:
                sections = body.split('#', 2)
                if ',' in sections[1]:
                    sections [1] = getEq(sections[1].split(',')[1], sections[1].split(',')[0])
                else:
                    sections [1] = r'Equation \ref{eq:' + sections[1] + '}'
                body = ''.join(sections)

            tex.write(getGoalBegin(title))
            tex.write(body)
                
tex.write(r'\end{document}')
tex.close()
