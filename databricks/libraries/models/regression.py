from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler

def linear_regression(train_data, features, target):
    """
    - Trained linear regression model
    """
    
    # Convert feature columns to a single vector column
    assembler = VectorAssembler(inputCols=features, outputCol="features")
    train_data = assembler.transform(train_data)
    
    # Initialize and train the linear regression model
    lr = LinearRegression(featuresCol="features", labelCol=target)
    model = lr.fit(train_data)
    
    return model
