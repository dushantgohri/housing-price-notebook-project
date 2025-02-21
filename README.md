# Jupyter Notebook Project for Housing Price Prediction

This project aims to predict housing prices using regression techniques. It involves fetching data from Snowflake, performing exploratory data analysis (EDA), applying multiple regression models, selecting the best model, and deploying it to AWS SageMaker. The predictions will also be uploaded back to Snowflake.

## Project Structure

- **data/**: Contains the datasets used for training and testing.
  - `train.csv`: Training dataset.
  - `test.csv`: Testing dataset.
  
- **notebooks/**: Jupyter notebooks for various stages of the project.
  - `eda.ipynb`: Exploratory Data Analysis.
  - `regression_models.ipynb`: Application of regression models.
  - `model_selection.ipynb`: Model evaluation and selection.
  - `deployment.ipynb`: Deployment steps for AWS SageMaker.

- **scripts/**: Python scripts for data fetching and model deployment.
  - `fetch_data.py`: Fetches data from Snowflake.
  - `upload_predictions.py`: Uploads predictions back to Snowflake.
  - `sagemaker_deploy.py`: Deploys the model to AWS SageMaker.

- **requirements.txt**: Lists the required Python packages for the project.

- **.gitignore**: Specifies files and directories to be ignored by Git.

- **README.md**: Documentation for the project.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd jupyter-notebook-project
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Fetch the data from Snowflake by running `scripts/fetch_data.py`.

4. Open the Jupyter notebooks in the `notebooks/` directory to perform EDA, apply regression models, and select the best model.

## Git Instructions

- **Branching**: Create a new branch for your feature or bug fix.
  ```
  git checkout -b feature-branch-name
  ```

- **Staging Changes**: Stage your changes before committing.
  ```
  git add <file-name>
  ```

- **Committing Changes**: Commit your changes with a descriptive message.
  ```
  git commit -m "Description of changes"
  ```

- **Merging**: Merge your feature branch back into the main branch.
  ```
  git checkout main
  git merge feature-branch-name
  ```

- **Rollback**: If you need to undo a commit, you can reset to the previous commit.
  ```
  git reset --hard HEAD~1
  ```

- **Pushing Changes**: Push your changes to the remote repository.
  ```
  git push origin main
  ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.