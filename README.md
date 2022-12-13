"# ABC-Report" 

clone repository<br>
run: python scripts/script.js

CRUD Operations:<br>
@app.route('/')  --  homepage <br>
@app.route('/data')  --  api to get all data from dataset<br>
@app.route('/form')  --  api to collect data and apply ML model<br>
@app.route('/result')  -- api to post result after applying ML<br>
@app.route('/any-other-url')  --  api to handle HTTPException<br>
<br>
Yet to do:<br>
@app.route('/data/<string:word1>/<string:word2>', methods = ['DELETE'])  -- api to delete data from dataset<br>
@app.route('/reports')  -- api to generate reports ( present in ppt )
