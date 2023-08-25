from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler

def logistic_classification(train_data, features, target):
    """
    - Trained logistic regression model
    """
    
    # Convert feature columns to a single vector column
    assembler = VectorAssembler(inputCols=features, outputCol="features")
    train_data = assembler.transform(train_data)
    
    # Initialize and train the logistic regression model
    lr = LogisticRegression(featuresCol="features", labelCol=target)
    model = lr.fit(train_data)
    
    return model
