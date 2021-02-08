## Introduction

Writing unit tests is a common practice in industry to ensure software quality. Usually meeting a certain criterea of test coverage serve as a segway to the product release. Despite all efforts, the software remains error prone. Empirical studies [1][2][3] at different scale and under different settings have found a no, weak or moderate correlation between coverage and test case. These studies examined all types of bugs that were found in the systems. A part of literature focusses on subset of bugs such as easy to fix one-line bugs, mostly in the context of program repair. However, There is a gap in study related to the effectiveness of test suites for such bugs. Previously there was no large dataset available to conduct such studies. The recent studies in automatic program fixing have produced large classified [4] and unclassified [5] datasets of one-line bugs.

In this study, we aim to fill the gap by studying the relation of unit testing and small one line bugs.


1- Lucas Gren and Vard Antinyan (On the Relation Between Unit Testing and Code Quality)
2- Antinyan et all (Mythical Unit Test Coverage)
3- Laura Inozemtseva and Reid Holmes (Coverage Is Not Strongly Correlated
with Test Suite Effectiveness)
4- Rafael-Michael Karampatsis, Charles Sutton (How Often Do Single-Statement Bugs Occur?
The ManySStuBs4J Dataset)
5- Zimin Chen, Steve Kommrusch, Michele Tufano, Louis-Noël Pouchet, Denys Poshyvanyk and Martin Monperrus (SEQUENCER: Sequence-to-Sequence Learning for End-to-End Program Repair)
