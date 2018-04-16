preamble = r'''
\documentclass{article}

\usepackage{fancyhdr}
\usepackage{lipsum}
\usepackage{ragged2e}
\usepackage{longtable}
\usepackage{graphicx}
\usepackage{caption}
\usepackage{geometry}
\usepackage{amsmath}
\usepackage{rotating}

\usepackage{listings}
\usepackage{color}

\definecolor{dkgreen}{rgb}{0,0.6,0}
\definecolor{gray}{rgb}{0.5,0.5,0.5}
\definecolor{mauve}{rgb}{0.58,0,0.82}

\lstset{frame=tb,
  language=Java,
  aboveskip=3mm,
  belowskip=3mm,
  showstringspaces=false,
  columns=flexible,
  basicstyle={\small\ttfamily},
  numbers=none,
  numberstyle=\tiny\color{gray},
  keywordstyle=\color{blue},
  commentstyle=\color{dkgreen},
  stringstyle=\color{mauve},
  breaklines=true,
  breakatwhitespace=true,
  tabsize=4
}

\setcounter{secnumdepth}{0}

%\newgeometry{vmargin={20mm}, hmargin={12mm,17mm}}

%\makeatletter
%\renewcommand{\thefigure}{\thesection .\@arabic\c@figure}
%\makeatother
\usepackage{chngcntr}
\counterwithin{figure}{section}

\renewcommand*{\thepage}{C\arabic{page}}

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

figureTemplate = r'''\begin{figure} \centering
\includegraphics[width=10cm,height=10cm,keepaspectratio]{path}
\caption{captionr}
\label{fig:name}
\end{figure}'''

eqTemplate = r'\begin{equation} value \label{eq:name} \end{equation}'

scheduleTemplate = r'''
\begin{sidewaysfigure}
\includegraphics[width=\textheight]{file}
\end{sidewaysfigure}
'''
