from forms import ClubSearchForm
from flask import Flask, request, jsonify,flash, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "super secret key"

#-------------------- LANDING PAGES -----------------------#
@app.route('/')
def main():
    return "Welcome to PennClubReview!"

@app.route('/api')
def api():
    return "Welcome to the PennClubReview API!."

#------------------- Task 2: Student Class and Jennifer ------------------#
# Possibly an extension to this quickly would be associate Jennifer's preferences 
# with her Student object
# Password is hashed in accordance to werkzeug.security specifications 
class Student:    
    def __init__(self, name, password, pennkey, schoolYear):
        self.name = name
        self.set_password(password)
        self.pennkey = pennkey
        self.schoolYear = schoolYear
 
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)      

Jennifer = Student("Jennifer", "ilovearun6789", "jennyffy", 1)

#-------------------- Task 3: Jennifer's Preferences ---------------------#
#retArr tracks Jennifer's preferences throughout
preferences =   [
                    { "name": "Penn Labs", "size": 40 },
                    { "name": "Penn Coffee Clubs", "size": 10 },
                    { "name": "Penn Tech Review", "size": 20 },
                    { "name": "Totally Not a Frat", "size": 40 },
                    { "name": "Dining Philosophers", "size": 50 },
                    { "name": "Hack4Impact", "size": 40 }
                ]

retArr = [] 
for i in range(0, len(preferences)):
    retArr.append(preferences[i]["name"])

#-------------------- Tasks 4 & 5: Handling Clubs ------------------------#
# Due to a lack of a Club Database, I've simply gone with all of Jennifer's clubs
# With an actual DB, @var 'list' would parse the DB
# GET returns 'list' of all clubs in JSON format 
# POST takes in two @params clubName, clubSize and appends them to the 'list' of all clubs  
@app.route('/api/clubs', methods = ['GET', 'POST'])
def clubsData():
    list = [
                { "name": "Penn Labs", "size": 40 },
                { "name": "Penn Coffee Clubs", "size": 10 },
                { "name": "Penn Tech Review", "size": 20 },
                { "name": "Totally Not a Frat", "size": 40 },
                { "name": "Dining Philosophers", "size": 50 },
                { "name": "Hack4Impact", "size": 40 }
            ]
    if request.method == 'GET':
        retList = [] 
        for i in range(0, len(list)):
            retList.append(preferences[i]["name"])        
        return jsonify(retList)
    if request.method == 'POST':
        newClubName = request.data['clubName'] 
        newClubSize = request.data['clubSize']
        list.append({"name": newClubName, "size": newClubSize})

#-------------------- Tasks 6 & 7: Handling Clubs ---------------------#
@app.route('/api/rankings', methods = ['GET', 'POST'])
def rankings():
    if request.method == 'GET':
        return jsonify(retArr) 
    # POST method takes in two arguments (clubName, newRank)
    # Club whose rank is to be changed and its new rank     
    if request.method == 'POST':
        changeRankClub = request.data['clubName'] 
        changeRankTo = request.data['newRank']
        retArr.remove(changeRankClub)
        retArr.insert((changerankTo - 1), changeRankClub)
     
#-------------------- Tasks 8: Return User ---------------------#
# Certain lines of this route are limited because I dont have a database of Users.
# I might almost be writing pseudocode at some points in this method
# A line or two might be commented out to avoid compilation errors, Sorry!

@app.route('/api/user/<id>')
def retUser(id):
    #Check for Student ID from Database
    exampleUserDatabase
    if exampleUserDatabase.contains(id):
        requestedUser = Student()
        return jsonify(requestedUser)     


#-------------------- TASK 9: SEARCH FEATURE ---------------------#
@app.route('/api/search', methods=['GET', 'POST'])
def index():
    search = ClubSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
 
    return render_template('index.html', form=search)
 
 
@app.route('/api/search/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    # if search.data['search'] != '': 
    #     qry = db_session.query()
    #     results = qry.all()
 
    if not results:
        flash('No results found!')
        return redirect('/api/search')
    else:
        # display results
        return render_template('results.html', results=results)
#-------------------------------------------------------------------#

if __name__ == '__main__':
    app.run()