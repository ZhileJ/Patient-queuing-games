## README
The project implements the algorithm computing the utility for each queue in patient queueing games given by Jason Gaitonde and Éva Tardos in [The Price of Anarchy of Strategic Queuing Systems](https://dl.acm.org/doi/10.1145/3587250).

### Dependence

* Python >= 3.7

* Numpy 1.21.6 (?)
* Pandas 1.3.5(?)

### Run testcase

```
python queuing_game.py test.csv
```



### Add your system and strategy

In ./graphs, add .csv file where row titles are lambda values, column titles are mu values, and the matrix is strategy. Make sure lambdas and mus are between 0 and 1, and strategy are some probabilities. Check test.csv, test1.csv, and test2.csv for more details.
