
# Scikit-learn's Design Principle

Scikit-Learn has a simple and consistent API that makes it easy to use and understand. Below are the key design principles behind it:


<br> <!-- ================================================= -->


## 1. Consistency
All objects follow a standard interface, which makes learning and using different tools in Scikit-Learn easier.



<br> <!-- ================================================= -->




## 2. Estimators
Any object that learns from data is called an *estimator*.
- Use the `.fit()` method to train an estimator.
- In supervised learning, pass both `X` (features) and `y` (labels) to `.fit(X, y)`.
- Hyperparameters (like `strategy='mean'` in `SimpleImputer`) are set when creating the object.

**Example:**
```python
imputer = SimpleImputer(strategy="median")
imputer.fit(data)

```

<br> <!-- ================================================= -->



## 3. Transformers

Some estimators can also transform data. These are called *transformers*.

* Use `.transform()` to apply the transformation after fitting.
* Use `.fit_transform()` to do both in one step.

**Example:**

```python
X_transformed = imputer.fit_transform(data)

```

<br> <!-- ================================================= -->



## 4. Predictors

Models that can make predictions are *predictors*.

* Use `.predict()` to make predictions on new data.
* Use `.score()` to evaluate performance (e.g., accuracy or $R^2$).

**Example:**

```python
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
score = model.score(X_test, y_test)

```

<br> <!-- ================================================= -->



## 5. Inspection

* Hyperparameters can be accessed directly: `model.param_name`
* Learned parameters are stored with an underscore: `model.coef_`, `imputer.statistics_`


<br> <!-- ================================================= -->



## 6. No Extra Classes

* Inputs and outputs are basic structures like NumPy arrays or Pandas DataFrames.
* No need to learn custom data types.


<br> <!-- ================================================= -->



## 7. Composition

You can combine steps into a *Pipeline*, chaining transformers and a final predictor.

**Example:**

```python
pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("model", LinearRegression())
])
pipeline.fit(X, y)

```

<br> <!-- ================================================= -->



## 8. Sensible Defaults

Most tools in Scikit-Learn work well with default settings, so you can get started quickly.

---
---

<br> <!-- ================================================== -->



### Note on DataFrames

Even if you input a Pandas DataFrame, the output of transformers like `transform()` will be a NumPy array. You can convert it back like this:

```python
X = imputer.transform(housing_num)
housing_tr = pd.DataFrame(X, columns=housing_num.columns, index=housing_num.index)

```
