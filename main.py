from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import (
    DataIngestionConfig, 
    TrainingPipelineConfig, 
    DataValidationConfig, 
    DataTransformationConfig, 
    ModelTrainerConfig
)

import sys

if __name__ == '__main__':

    try:
        training_pipeline_config = TrainingPipelineConfig()

        """
        Data Ingestion
        """

        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
 
        logging.info("Initiate Data Ingestion")

        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        print(data_ingestion_artifact)

        logging.info("Data Ingestion completed")

        """
        Data Validation
        """

        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(data_ingestion_artifact, data_validation_config)

        logging.info("Initiate Data Validation")

        data_validation_artifact = data_validation.initiate_data_validation()

        logging.info("Data Validation completed")

        print(data_validation_artifact)

        """
        Data Transformation
        """

        data_transformation_config = DataTransformationConfig(training_pipeline_config)
        data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)

        logging.info("Initiate Data Transformation")

        data_transformation_artifact = data_transformation.initiate_data_transformation()

        logging.info("Data Transformation completed")

        print(data_transformation_artifact)

        """
        Model Trainer
        """

        model_trainer_config = ModelTrainerConfig(training_pipeline_config)
        model_trainer = ModelTrainer(model_trainer_config, data_transformation_artifact)

        logging.info("Initiate the Model Trainer")

        model_trainer_artifact = model_trainer.initiate_model_trainer()

        logging.info("Model Training completed")

    except Exception as e:
        raise NetworkSecurityException(e, sys)

