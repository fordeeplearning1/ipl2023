from pprint import pprint
import prompt_toolkit
from PyInquirer import prompt, Separator
from examples import custom_style_2
import random
import pandas as pd
import h2o

questions = [
    {
        'type': 'checkbox',
        'qmark': '😃',
        'message': 'Select any two teams',
        'name': 'Teams',
        'choices': [
            Separator('= Teams ='),
            {'name': 'Rajasthan Royals'},
            {'name': 'Royal Challengers Bangalore'},
            {'name': 'Sunrisers Hyderabad'},
            {'name': 'Delhi Capitals'},
            {'name': 'Chennai Super Kings'},
            {'name': 'Gujarat Titans'},
            {'name': 'Lucknow Super Giants'},
            {'name': 'Kolkata Knight Riders'},
            {'name': 'Punjab Kings'},
            {'name': 'Mumbai Indians'},
            {'name': 'Pune Warriors'},
            ],
        'validate': lambda answer: 'You must choose any two teams' if len(answer) != 2 else True
    }
]

answers = prompt(questions, style=custom_style_2)
pprint(answers)

# Model output for winning team
Team1, Team2 = answers['Teams'][0], answers['Teams'][1]
test = pd.DataFrame(columns=['Team1', 'Team2'])
predictors = ['Team1', 'Team2']
test.loc[0] = [Team1, Team2]
model_path = 'StackedEnsemble_AllModels_1_AutoML_1_20230411_190059'
h2o.init()
best_model = h2o.load_model(model_path)

prediction = best_model.predict(h2o.H2OFrame(test[predictors]))
print('\nProbable match winner: ', prediction[0, 0], '\n')

# making a random prediction using Binomial distribution (Toss Prediction)
rand_op = random.randint(1, 2)
if rand_op == 1:
    winner = Team1
else:
    winner = Team2

print('Probable toss winner: ', winner, '\n')
