"# ABC-Report" 

clone repository
run: python scripts/script.js


CRUD Operations:

@app.route('/')  --  homepage
@app.route('/data')  --  api to get all data from dataset
@app.route('/form')  --  api to collect data and apply ML model
@app.route('/result')  -- api to post result after applying ML
@app.route('/any-other-url')  --  api to handle HTTPException

Yet to do:
@app.route('/data/<string:word1>/<string:word2>', methods = ['DELETE'])  -- api to delete data from dataset
@app.route('/reports')  -- api to generate reports ( present in ppt )
