# Reusable Kubeflow Components for ppc64le
Reusable [Kubeflow](https://www.kubeflow.org) components for ppc64le (IBM Power processor architecture).

## Using Components

### Kubeflow Pipelines Python SDK
```
import kfp
import kfp.dsl as dsl
from kfp import components

example_comp = components.load_component_from_url('https://raw.githubusercontent.com/lehrig/kubeflow-ppc64le-components/main/examples/hello-world/component.yaml')

@dsl.pipeline(
    name='My first pipeline',
    description='A hello world pipeline.'
)
def hello_world_pipeline():
    task = example_comp(
        name="hello world!"
    )
```

### Elyra
See: https://elyra.readthedocs.io/en/latest/user_guide/pipeline-components.html#managing-pipeline-components

## Creating Components
Each subfolder of this repository includes a Kubeflow component. Each component is generally structured as recommended by [Kubeflow's "Building Components" guide](https://www.kubeflow.org/docs/components/pipelines/sdk/component-development/). That is, each component comes with:
- a `component.yaml` file that specifies the component’s interface and implementation and
- (optionally) a `build_image.sh` file that can be run to build a component-specific container image and to push it to a container registry.

### Base Images
The `base-images` folder includes only build scripts for images that some components might depend on. There's no `component.yaml` for base images themselves.

### Building Component-Specific Container Images
Some components may require component-specific container images, which have to be build first. In this case, proceed as follows.
```
git clone https://github.com/lehrig/kubeflow-ppc64le-components
cd kubeflow-ppc64le-components
```

Afterwards, `cd` into the component in question and run:
```
docker login ***YOUR TARGETED IMAGE REGISTRY***
./build_image.sh
```
