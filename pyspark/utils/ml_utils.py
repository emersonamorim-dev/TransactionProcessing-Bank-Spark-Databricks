from pyspark.ml import PipelineModel
from pyspark.ml.evaluation import RegressionEvaluator, BinaryClassificationEvaluator, MulticlassClassificationEvaluator
from pyspark.sql import DataFrame

def build_pipeline(stages: list) -> Pipeline:
    """Build a MLlib pipeline."""
    return Pipeline(stages=stages)

def train_pipeline(pipeline: Pipeline, training_data: DataFrame) -> PipelineModel:
    """Train a model using a pipeline."""
    return pipeline.fit(training_data)

def evaluate_model(model: PipelineModel, test_data: DataFrame, metric_name: str = "rmse", evaluator_type: str = "regression") -> float:
    """Evaluate the performance of a model."""
    if evaluator_type == "regression":
        evaluator = RegressionEvaluator(metricName=metric_name)
    elif evaluator_type == "binary_classification":
        evaluator = BinaryClassificationEvaluator(metricName=metric_name)
    elif evaluator_type == "multiclass_classification":
        evaluator = MulticlassClassificationEvaluator(metricName=metric_name)
    else:
        raise ValueError(f"Unknown evaluator type: {evaluator_type}")
    
    predictions = model.transform(test_data)
    return evaluator.evaluate(predictions)

def save_model(model: PipelineModel, path: str) -> None:
    """Save a trained model."""
    model.write().overwrite().save(path)

def load_model(path: str) -> PipelineModel:
    """Load a trained model."""
    return PipelineModel.load(path)

def transform_data(model: PipelineModel, data: DataFrame) -> DataFrame:
    """Use a model or pipeline to transform a dataset."""
    return model.transform(data)

