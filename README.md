# Rock Paper Scissors Game

![full-layout](https://user-images.githubusercontent.com/80278757/173707581-190bdfc4-2a38-4eab-a8c0-0b822f9cb41b.png)

## Table of Contents

- [Description](#rock-paper-scissors-game)
- [Features](#features)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)

## Features
![playing](https://user-images.githubusercontent.com/80278757/173707616-60528de5-6881-40b7-a8d8-86ba14dd9d0e.png)
![validation-leter](https://user-images.githubusercontent.com/80278757/173707619-068327e3-7b19-49c2-a1e9-0c921ae0938d.png)
![validation-number](https://user-images.githubusercontent.com/80278757/173707620-d96c7efc-5fcd-449c-8403-ac7e34d2ec48.png)
![result](https://user-images.githubusercontent.com/80278757/173707957-5cd90c8f-79d6-48f5-a27a-7414cb1d2268.png)

## Bugs

No bugs unsolved!

## Deployment

- Create a repository using the [Code Institute template](https://github.com/cinthiafontoura/python-essentials-template) for Python command-line project.
- Go to [Heroku webpage](https://www.heroku.com/) and **log in**/**sign up**.
- At the dashboard click on the **New** button -> **Create new app**.
- Add a app name, choose the region, and click on **Create app** button.
- On the **Settings** tab -> **Config Vars** section -> **Reveal Config Vars** add the KEY and VALUE nedded.
- Bellow on the **Buildpacks** section -> **Add buildpack** button to add Python and Node.js to the list.
- On the **Deploy** tab -> **Deployment method** section, choose GitHub.
- Search for a repository to connect to on **Connect to GitHub** section and click **Conect**.
- Choose a branch and click on **Deploy Branch** on **Manual deploy** section to finilyse the deployment.
- After a few seconds, open the deployed app by clicking on **View** button.

Live website at [Rock Paper Scissors Game](https://pp3-rock-paper-scissors.herokuapp.com/)

## Credits

- Project created using the [Code Institute template](https://github.com/cinthiafontoura/python-essentials-template) for Python command-line project.
- Description text and rules from [World Rock Paper Scissors Association](https://wrpsa.com/) website.
- ASCII art from [ASCII Art Archive](https://www.asciiart.eu) and [patorjk](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20).
- Clear screen code from [Stack Overflow](https://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python)


<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Cinthia Fontoura,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!
