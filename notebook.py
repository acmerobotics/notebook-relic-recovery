#!python2

import os
import template
import openpyxl
import datetime


def append_line(s1, s2):
    return s1 + '\n' + s2

def findOccurences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def parse_response(response, path):
    while '<' in response:
        start = response.find('<') + 1
        end = response.find('>')
        image = response[start:end]


        name = image.split('.')[0]

        figure = ''
        if ',' in image:
            file = image.split(',')[0].replace('_', '-')
            caption = image.split(',')[1]
            figure = template.figureTemplate.replace('path', path + file).replace('name', name).replace('captionr', caption)
        figure = figure + r'Figure \ref{fig:' + name + r'}'

        response = response[:start-1] + figure + response[end+1:]

    marks = findOccurences(response, '#')
    while '#' in response:
        start = findOccurences(response, '#')[0] + 1
        end = findOccurences(response, '#')[1]
        equation = response[start:end]
        print equation
        name = ''
        result = ''
        if ',' in equation:
            name = equation.split(',')[0]
            result = template.eqTemplate.replace('value', equation.split(',')[1]).replace('name', name)
        else:
            name = equation
        print name

        result = result + r'Equation \ref{eq:' + name + '}'

        response = response[:start - 1] + result + response[end + 1:]

    return response

def getDate(week):
    return (datetime.date(2017, 10, 28) + datetime.timedelta(days=6)).strftime('%d %B %Y')

tex = open('./out/notebook.tex', 'w+')
tex.write(template.preamble)
tex.write(r'\begin{document}')
tex.write(r'\tableofcontents')
tex.write(r'\newpage')

dir = os.listdir('./in')
numWeeks = len(dir)

for i in range(numWeeks):
    goalsText = ''
    responseText = ''
    print 'week ', i + 1
    weekDir = dir[i]
    tex.write(template.weekBegin)
    tex.write(r'\subsection*{' + getDate(i) + r'}')
    weekList = os.listdir('./in/' + weekDir+ '/')
    if 'schedule.pdf' in weekList:
        tex.write(template.scheduleTemplate.replace('file', '../in/' + weekDir + '/' + 'schedule.pdf'))
    for file in weekList:
        if 'xlsx' not in file: continue
        first = file.lower()[0]
        team = 'Business'
        if first == 's': team = 'Software'
        elif first == 'h': team = 'Hardware'

        goalsText = append_line(goalsText, r'\subsection{' + team + r' Goals}')

        wb = openpyxl.load_workbook(filename='./in/' + weekDir + '/' + file);
        ws = wb.active

        goalNum = 1
        goal = ws['A' + str(goalNum + 3)].value
        while goal:
            goal = team[0] + str(goalNum) + ': ' + goal
            descip = ws['B' + str(goalNum + 3)].value
            response = ws['D' + str(goalNum + 3)].value

            goalsText = append_line(goalsText, r'\paragraph{' + goal + '} ' + descip)

            response = parse_response(response, '../in/' + weekDir + '/')

            responseText = append_line(responseText, template.goalBeginTemplate.replace('goal', goal))
            responseText = append_line(responseText, response)

            goalNum += 1
            goal = ws['A' + str(goalNum + 3)].value

    tex.write(goalsText)
    tex.write(r'  \newpage  ' + '\n')
    tex.write(responseText)

tex.write(r'\end{document}')
tex.close()
