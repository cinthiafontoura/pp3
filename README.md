# Rock Paper Scissors Game

Rock Paper Scissors is a Python terminal game which runs in the Code Institute mock terminal on Heroku.

Users play against the computer to get the best of 3 rounds on this adaptation of a classic game usually played by two people using their hands and no tools. The idea is to choose shapes with an outstretched hand represented by numbers, where each shape will have a certain degree of power and lead to an outcome.

Live game at [Rock Paper Scissors Game](https://pp3-rock-paper-scissors.herokuapp.com/).

![final-layout-responsive](https://user-images.githubusercontent.com/80278757/174295260-28da9e88-52f8-4840-a6a2-2b5ce4277d1f.png)


## Table of Contents

- [Description](#rock-paper-scissors-game)
- [How to play](#how-to-play)
- [Features](#features)
- [Testing](#testing)
- [User Experience](#user-experience)
- [Deployment](#deployment)
- [Credits](#credits)


## How To Play

The player enters their name and chooses their move to start the first round.

Rock beats scissors, scissors beats paper, and paper wins against the rock.

[&#11178; Back to the Table of Contents](#table-of-contents)


## Features

- The introduction to the game and rules is given.
- The user is asking to enter a name.

![introduction](https://user-images.githubusercontent.com/80278757/174295802-a8c63746-8967-4db9-8e64-617c513f298c.png)

- The user was not allowed to leave empty numbers or alphanumeric for the name input. And feedback is provided case it occurs.

![name-validation](https://user-images.githubusercontent.com/80278757/174296125-0046b9bc-2e16-45fb-8c5a-e0a7d147e371.png)

- Random generation of computer and user choice is printed with the round number and the score.

![round](https://user-images.githubusercontent.com/80278757/174295799-97dd9ec9-84e4-4ba0-953d-619ccf9cda0e.png)

- After the third round, the game results pop on the screen 

![result](https://user-images.githubusercontent.com/80278757/174295796-2bb16292-8cac-41f5-b392-8a2f973d621e.png)

- The new score is added to a worksheet using a Google API.
- The latest six results are printed on the screen.

![latest-scores](https://user-images.githubusercontent.com/80278757/174295804-1f0c8233-b3f3-4d9b-8b02-f427a40f6411.png)

- The user can enter the numbers 1, 2 or 3 as the instructions ask, and the program will provide feedback if they type something different.

![choice-validation](https://user-images.githubusercontent.com/80278757/174296122-694dd2b7-f5c8-4bc4-86a9-397e215f7673.png)

### Future Features

- Change the order of the latest scores to a decrescent order.

[&#11178; Back to the Table of Contents](#table-of-contents)


## Testing

- No errors or warns are returned when passed through the PEP8 linter.
- All valid inputs are managed by not accepting strings when numbers are requested or numbers or empty information when strings are expected.
- Tested in my local terminal and The Code Institute Heroku terminal.

### Bugs

#### Solved bugs

- When the Code Institute terminal was returned a gspreed not determined error, I fixed running the <code>pip3 freeze > requirements.txt</code>.

#### Remaining Bugs 

- No bugs remaining.

[&#11178; Back to the Table of Contents](#table-of-contents)


## User Experience

- I had put the button on the bottom of the terminal and made it more extensive, and changed the button value to "PLAY GAME", but when I tested with users, they got confused with the new layout and tried to click PLAY GAME instead hit enter in the keyboard to enter the inputs. To solve this, I return the original location, size, and value and keep the pink style.
- The user always presses 3 instead of 0 to play, so I change the input choices to 1, 2, and 3 so the user does not get confusing and does not need to go to the other side of the keyboard when choosing moves. It is also more logical to count from one than zero for most players.
- Even with the ASCII art at the end showing if the player wins, loses or draws, they feel a need for more feedback confirming this.
- For those that want to play again, the instruction is given when the game ends.

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
- Support of documentation on [Python docs](https://docs.python.org/3/library/)
- W3Schools [Python Tutorial](https://www.w3schools.com/python/default.asp)
- Love Sandwiches [code](https://github.com/cinthiafontoura/love-sandwiches)
- Google Sheets and Google APIs.

[&#11178; Back to the Table of Contents](#table-of-contents)
