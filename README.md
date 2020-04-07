# NanoTrivia 

# Full Stack Trivia API  Frontend

## Getting Setup

> _tip_: this frontend is designed to work with [Flask-based Backend](../backend). It is recommended you stand up the backend first, test using Postman or curl, update the endpoints in the frontend, and then the frontend should integrate smoothly.

### Installing Dependencies

#### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

>_tip_: **npm i** is shorthand for **npm install**

## Required Tasks

## Running Your Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use ```npm start```. You can change the script in the ```package.json``` file. 

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br>

```bash
npm start
```

## Request Formatting

The frontend should be fairly straightforward and disgestible. You'll primarily work within the ```components``` folder in order to edit the endpoints utilized by the components. While working on your backend request handling and response formatting, you can reference the frontend to view how it parses the responses. 

After you complete your endpoints, ensure you return to and update the frontend to make request and handle responses appropriately: 
- Correct endpoints
- Update response body handling 

## Optional: Styling

In addition, you may want to customize and style the frontend by editing the CSS in the ```stylesheets``` folder. 

## Optional: Game Play Mechanics

Currently, when a user plays the game they play up to five questions of the chosen category. If there are fewer than five questions in a category, the game will end when there are no more questions in that category. 

You can optionally update this game play to increase the number of questions or whatever other game mechanics you decide. Make sure to specify the new mechanics of the game in the README of the repo you submit so the reviewers are aware that the behavior is correct. 

## Getting Started with Back-end

###Dependencies

#### Python 3.7

You have to check the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

It will be better if use the Virtual Env [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### Dependencies
Then run this
```bash
pip install -r requirements.txt
```
This will install the required dependencies
##### We are using

- [Flask](http://flask.pocoo.org/)

- [SQLAlchemy](https://www.sqlalchemy.org/)

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#)

## Don't forget to setup the Db :)
```bash
psql trivia < trivia.psql
```

## I don't have to tell you, the server :)

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development`

Setting the `FLASK_APP` variable to `flaskr`



```
## APIs 
GET '/questions'
POST '/questions'
DELETE '/questions/{question_id}'
GET '/categories'
GET '/categories/{category_id}/questions'
POST '/search'
POST '/quizzes'
```

**GET '/categories'
- Returns:
{'1' : "Sport",
'2' : "Art"
}

**GET '/categories/{category_id}/questions'
-questions to a given category
Returns :
{
current_category: "Geography",
questions: [
    {
        answer: "Pla Pla :)",
        category: "1",
        difficulty: 1,
        id: 1,
        question: "Who is the the .... of ... "
    }
  ],
total_questions: 1
}
**GET '/questions'
- Get All Questions in the DB
- Returns
{
  "categories": [
    "Science"
  ], 
  "current_category": "", 
  "questions": [
    {
        answer: "Pla Pla :)",
        category: "1",
        difficulty: 1,
        id: 1,
        question: "Who is the the .... of ... "
    }
  ], 
  "total_questions": 3
}
**POST '/questions'
- Create a new question 
- Returns
{
        answer: "Pla Pla :)",
        category: "1",
        difficulty: 1,
        id: 1,
        question: "Who is the the .... of ... "
}

**DELETE '/questions/{question_id}'
- Delete question by a given id
- Returns
{
  "message": "Question Deleted"
} 
**POST '/search'
Serch for a question
- Sample Payload
{
  "searchTerm": "Pla Pla"
}
- Sample Response
{
  "current_category": "", 
  "questions": [
 {
        answer: "Pla Pla :)",
        category: "1",
        difficulty: 1,
        id: 1,
        question: "Who is the the .... of ... "
}
  ], 
  "total_questions": 1
}
**POST '/quizzes'
- Quiz previous asked quesiton
- Returns
{
  "previous_questions":[31],
  "quiz_category":{
    type: "Art", id: "1"
  }
}
- Returns
{
  "previous_questions": [], 
  "question": {
    "answer": "Yeah ", 
    "category": "1", 
    "difficulty": 10, 
    "id": 1, 
    "question": "Pla pla pla "
  }, 
  "quizCategory": {
    "id": "1", 
    "type": "Art"
  }, 
  "success": true
}
```
## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
## Author
Shawki Sukkar