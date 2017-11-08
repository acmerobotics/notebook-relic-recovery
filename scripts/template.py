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