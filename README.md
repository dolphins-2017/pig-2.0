## Game's component:  


#### Data: 
- Using class Player:
	name
	total_score
	current_score
	status: playing/holding
- `player_list = []`
- Update object's data every turn  


#### Commands:
- input score_cap at the begin
- `r` roll
- `b` bank
- cheats


## Game conditions:  
- _Pig_: one dice is 1 -> reset current score, ends turn
- _Snake-eyes_: both dices are 1s -> reset total score, ends turn
- _DOUBLE_: same values on dices -> forced to choose roll
- _Winning_: Reach the score_cap

## Display:
- Print the values in player object

## Mechanism:
- Using random package from python
```python
import random
for i in range(2):
	x = random.randrange(x)
```
