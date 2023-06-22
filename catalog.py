import kfp
import os

COMPONENT_CATALOG_FOLDER = os.path.dirname(os.path.abspath(__file__))


def load_component(path):
    component_file = os.path.join(
        COMPONENT_CATALOG_FOLDER,
        path,
        "component.yaml"
    )
    return kfp.components.load_component_from_file(component_file)


load_dataset_comp = load_component("data-collection/load-huggingface-dataset")
load_dataframe_via_trino_comp = load_component("data-collection/load-dataframe-via-trino")
create_dataset_quality_report = load_component("monitoring/create-data-quality-report-with-evidently")
monitor_training_comp = load_component("model-building/monitor-training")
train_model_comp = load_component("model-building/train-model-job")
plot_confusion_matrix_comp = load_component("model-building/plot-confusion-matrix")
plot_confusion_matrix_predictions_comp = load_component("model-building/plot-confusion-matrix-from-predictions")
convert_model_to_onnx_comp = load_component("model-building/convert-to-onnx")
upload_model_comp = load_component("model-building/upload-model")
deploy_model_with_kserve_comp = load_component("model-deployment/deploy-model-with-kserve")
convert_speech_to_text_comp = load_component("data-transformation/convert-speech-to-text")
