import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

from flask import Flask, request, render_template
 
def modelTrain():
	df = pd.read_excel('dataset.xlsx')

	# preprocessing
	# print(df.keys())
	category_col = ['area', 'climatic_condition', 'agriculture_products',
	       'popular_cuisines', 'land_cost', 'total_population', 'gender',
	       'ratio_of_working_professional', 'kids_ratio', 'ideal_place',
	       'cuisines', 'no_of_customers_5years', 'peak_hours_occupancy']
	labelEncoder = preprocessing.LabelEncoder()
	 
	# mapping_dict = {}
	for col in category_col:
	    df[col] = labelEncoder.fit_transform(df[col])
	 
	    le_name_mapping = dict(zip(labelEncoder.classes_, labelEncoder.transform(labelEncoder.classes_)))
	#     mapping_dict[col]=le_name_mapping
	# print(mapping_dict)

	# print(df.head())
	X = df.values[:, 0:9]
	Y = df.values[:, 9]

	# training
	X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.1, random_state = 20)
	 
	dt_clf_gini = DecisionTreeClassifier(criterion = "gini",
	                                     random_state = 20,
	                                     max_depth = 5,
	                                     min_samples_leaf = 5)
	# testing
	dt_clf_gini.fit(X_train, y_train)
	y_pred_gini = dt_clf_gini.predict(X_test)
	print(y_pred_gini)
	return dt_clf_gini


def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 9)
    loaded_model=modelTrain()
    print(to_predict)
    result = loaded_model.predict(to_predict)
    return result[0]

app=Flask(__name__, template_folder='../templates')

# render form
@app.route('/')
def index():
	return render_template("index.html")

# api to calculate result
@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)                 
        return render_template("result.html", prediction = result)

app.run()