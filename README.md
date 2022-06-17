# Rock Paper Scissors Game

Rock Paper Scissors is a Python terminal game which runs in the Code Institute mock terminal on Heroku.

Users play against the computer to get the best of 3 rounds on this adaptation of a classic game usually played by two people using their hands and no tools. The idea is to choose shapes with an outstretched hand represented by numbers, where each shape will have a certain degree of power and lead to an outcome.

Live game at [Rock Paper Scissors Game](https://pp3-rock-paper-scissors.herokuapp.com/).

![final-layout-responsive](https://user-images.githubusercontent.com/80278757/174295260-28da9e88-52f8-4840-a6a2-2b5ce4277d1f.png)


## Table of Contents

- [Description](#rock-paper-scissors-game)
- [How to play](#how-to-play)
- [Features](#features)
- [Bugs](#bugs)
- [User Experience](#user-experience)
- [Deployment](#deployment)
- [Credits](#credits)


## How To Play

The player enters their name and chooses their move to start the first round.

Rock beats scissors, scissors beats paper, and paper wins against the rock.

[&#11178; Back to the Table of Contents](#table-of-contents)


## Features

![introduction](https://user-images.githubusercontent.com/80278757/174295802-a8c63746-8967-4db9-8e64-617c513f298c.png)
![round](https://user-images.githubusercontent.com/80278757/174295799-97dd9ec9-84e4-4ba0-953d-619ccf9cda0e.png)
![result](https://user-images.githubusercontent.com/80278757/174295796-2bb16292-8cac-41f5-b392-8a2f973d621e.png)
![latest-scores](https://user-images.githubusercontent.com/80278757/174295804-1f0c8233-b3f3-4d9b-8b02-f427a40f6411.png)

[&#11178; Back to the Table of Contents](#table-of-contents)


## Validation

![choice-validation](https://user-images.githubusercontent.com/80278757/174296122-694dd2b7-f5c8-4bc4-86a9-397e215f7673.png)
![name-validation](https://user-images.githubusercontent.com/80278757/174296125-0046b9bc-2e16-45fb-8c5a-e0a7d147e371.png)
![pep8](https://user-images.githubusercontent.com/80278757/174296127-476d7d4e-d71e-43ea-9fa9-eebcbfcbfea0.png)

[&#11178; Back to the Table of Contents](#table-of-contents)


## Bugs 

No bugs unsolved!

[&#11178; Back to the Table of Contents](#table-of-contents)


## User Experience

![final-layout](https://user-images.githubusercontent.com/80278757/174296283-b88924ca-54d1-44c3-9cc6-3c6dae85580c.png)

[&#11178; Back to the Table of Contents](#table-of-contents)


## Deployment

- Create a repository using the [Code Institute template](https://github.com/cinthiafontoura/python-essentials-template) for Python command-line project.
- Run the **command pip3 freeze > requirements.txt** to ensure the gspreed will work on the deployed app.
- Go to [Heroku webpage](https://www.heroku.com/) and **log in**/**sign up**.
- At the dashboard, click the **New** button -> **Create new app**.
- Add an app name, choose the region, and click the **Create app** button.
- On the **Settings** tab -> **Config Vars** section -> **Reveal Config Vars** add the KEY and VALUE needed.
- Bellow on the **Buildpacks** section -> **Add buildpack** button to add Python and Node.js to the list.
- On the **Deploy** tab -> **Deployment method** section, choose GitHub.
- Search for a repository to connect to on the **Connect to GitHub** section and click **Connect**.
- Choose a branch and click on **Deploy Branch** on the **Manual deploy** section to finish the deployment.
- After a few seconds, open the deployed app by clicking on the **View** button.

Live website at [Rock Paper Scissors Game](https://pp3-rock-paper-scissors.herokuapp.com/)

[&#11178; Back to the Table of Contents](#table-of-contents)


## Credits

- Project created using the [Code Institute template](https://github.com/cinthiafontoura/python-essentials-template) for Python command-line project.
- Description text and rules from [World Rock Paper Scissors Association](https://wrpsa.com/) website.
- ASCII art from [ASCII Art Archive](https://www.asciiart.eu) and [patorjk](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20).
- Clear screen code from [Stack Overflow](https://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python)

[&#11178; Back to the Table of Contents](#table-of-contents)
