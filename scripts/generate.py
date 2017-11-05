preamble = r'''
\documentclass{article}

\usepackage{fancyhdr}
\usepackage{lipsum}
\usepackage{ragged2e}
\usepackage{longtable}
\usepackage{graphicx}

%header
\pagestyle{fancy}
\lhead{ACME Robotics}
\chead{\#8367}
\rhead{Week \thesection}

%get rid of section numbering
\makeatletter
% \@seccntformat is the command that adds the number to section titles
% we make it a no-op
\renewcommand{\@seccntformat}[1]{}
\makeatother

%fix table padding
\renewcommand{\arraystretch}{1.5}
'''

weekBegin = r'''
\newpage
\section{Week \thesection}
'''

tableBeginTemplate = r'''
\subsection{title}
\begin{center}
\begin{flushleft}
    \begin{longtable}{ | p{.2\textwidth} | p{.3\textwidth} | p{.4\textwidth} |}
    \hline
    Goal & Description & Outcome \\ \hline
'''

tableRowTemplate = r'''
goal & description & outcome \\ \hline
'''

tableEnd = r'''
\end{longtable}
\end{flushleft} 
\end{center}
'''

goalBeginTemplate = r'''
\subsection{goal}
'''

figureTemplate = r'''
\begin{figure}[h!]
<\includegraphics[width=\linewidth]{path}
\end{figure}
'''

def getTableBegin(title):
    return tableBeginTemplate.replace('title', title)

def getTableRow(goal, description, outcome):
    return tableRowTemplate.replace('goal', goal).replace('description', description).replace('outcome', outcome)

def getGoalBegin(goal):
    return goalBeginTemplate.replace('goal', goal)

def getFigure(path):
    return figureTemplate.replace('path', path)

file = open('../out/test.tex', 'w+')
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
           
