import kfp
from kfp import components
import os

EXAMPLES = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(EXAMPLES)
EVIDENTLY = os.path.join(ROOT, 'evidently')
DATA_QUALITY = os.path.join(EVIDENTLY, 'data-quality-report')
HTML_VIEW = os.path.join(ROOT, 'html-viewer')

download_data_op = components.load_component_from_file(os.path.join(EXAMPLES, 'download_breast_cancer_data.yaml'))
train_test_split_op = components.load_component_from_file('train_test_split.yaml')
run_gradient_boost_op = components.load_component_from_file('run_gradient_boost.yaml')
data_quality_op = components.load_component_from_file(os.path.join(DATA_QUALITY, 'component.yaml'))
html_view_op = components.load_component_from_file(os.path.join(HTML_VIEW, 'component.yaml'))


@kfp.dsl.pipeline(name='test-pipeline')
def test_pipeline():
    data = download_data_op().output
    
    report = data_quality_op(
        cur=data
    ).output
    
    html_view_op(
        html=report
    )
    
    prepared_data = train_test_split_op(data)
    print(prepared_data)
    
    run_gradient_boost_op(
        data=prepared_data.outputs,
    )
    
    
if __name__ == '__main__':
    kfp_endpoint=None
    kfp.compiler.Compiler().compile(test_pipeline, 'testPipeline.yaml')