# Reusable Kubeflow Components for ppc64le
Reusable [Kubeflow](https://www.kubeflow.org) components for ppc64le (IBM Power processor architecture).


### Building Components
Each subfolder of this repository includes a Kubeflow component. Each component is generally structured as recommended by [Kubeflow's "Building Components" guide](https://www.kubeflow.org/docs/components/pipelines/sdk/component-development/). That is, each component comes with:
- a `build_image.sh` file that can be run to build a container image and to push it to a container registry and
- a `component.yaml` file that specifies the component’s interface and implementation.
