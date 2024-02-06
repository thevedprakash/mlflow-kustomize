# MLflow Deployment with Kustomize

This repository contains the Kubernetes configurations for deploying the MLflow platform, which is designed for managing the complete machine learning lifecycle. By leveraging Kustomize, these configurations facilitate adaptable deployments across various environments, notably development and production.

## Repository Structure

The repository is structured into `base` and `overlays` directories:

- **Base**: Houses the foundational Kubernetes YAML configurations applicable across all environments.
- **Overlays**: Comprises environment-specific configurations, segmented into `development` and `production` subdirectories.

### Base Directory

The `base` directory encompasses:

- `kustomization.yaml`: A Kustomize manifest linking to other resources.
- `mlflow-deployment.yaml`: The Kubernetes Deployment manifest for MLflow.
- Other necessary manifests (services, volumes, etc.).

### Overlays Configuration

Within the `overlays` directory:

- **Development**: Contains Kustomize and patch files for a development setting. `mlflow-patch.yaml` in this directory overrides configurations for development purposes.
- **Production**: Mirroring the development directory, it holds files for the production environment.

## Usage

To deploy MLflow in a specific environment, execute the following:

1. **Root Navigation**: Position yourself in the repository's root directory.

2. **Apply Kustomize Configuration**: Deploy MLflow in the desired environment:

   - Development:
     ```bash
     kubectl apply -k overlays/development/
     ```
   - Production:
     ```bash
     kubectl apply -k overlays/production/
     ```

This command will deploy MLflow according to the chosen environment's configurations.

## Customization

For bespoke deployments, you can modify the base configuration files or introduce new patches in the respective `overlays` environment directories.

## Conclusion

This approach provides a streamlined and flexible method for deploying MLflow in different Kubernetes environments, ensuring core consistency while accommodating environment-specific customizations.
