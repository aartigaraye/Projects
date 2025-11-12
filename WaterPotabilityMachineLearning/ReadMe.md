# Introduction 

Water is the most important source of life to sustain many living things. All living things on earth depend on water to grow and sustain life. In order to use this water in everyday life, it is significant to have access to clean water without contamination. Water pollution can be defined in terms of its quality which is determined by various features like pH, turbidity, electrical conductivity dissolved, etc. This project aims to presents a prediction of water potability deploying different classification models employing machine learning algorithms. We will be using logistic regression, LDA, QDA, elastic net, a random forrest, and SVM. Different classification methods encourage us to compare several classification methods that can be used. Machine learning is well-suited for this type of classification task. Traditional rule-based systems often depend on fixed thresholds for each parameter (e.g., "pH must be between 6.5 and 8.5"), but these boundaries may fail to capture the complex, non-linear relationships between water features and potability. 

| Term                                | Quick Definition                                         | Why It Matters for Health                                                  |
| ----------------------------------- | -------------------------------------------------------- | -------------------------------------------------------------------------- |
| **pH**                              | Measure of acidity/basicity (scale 0–14).                | Extreme pH can corrode pipes and leach heavy metals.                       |
| **Turbidity**                       | Cloudiness caused by suspended particles (NTU).          | High turbidity can shield pathogens and reduce disinfection effectiveness. |
| **Hardness**                        | Concentration of calcium & magnesium (mg CaCO₃/L).       | Aesthetic concern; very high values promote scale formation.               |
| **Total Dissolved Solids (Solids)** | Mass of inorganic salts & small organic molecules (ppm). | Elevated TDS can alter taste and indicate other contaminants.              |
| **Chloramines**                     | Disinfectant formed from chlorine + ammonia (mg/L).      | Necessary for disinfection but toxic at high doses.                        |
| **Sulfate**                         | Dissolved sulfate ions (mg/L).                           | > 250 mg/L imparts bitter taste and laxative effect.                       |
| **Conductivity**                    | Ability of water to conduct electricity (µS/cm).         | Proxy for total ion concentration.                                         |
| **Organic Carbon**                  | Carbon from natural organic matter (mg C/L).             | Reacts with chlorine to form harmful disinfection by-products.             |
| **Trihalomethanes (THMs)**          | Chlorination by-products (µg/L).                         | Long-term exposure linked to cancer risk.                                  |

The primary goal of this project is to develop and compare predictive models that can flag unsafe water using readily obtainable measurements. Concretely, we will:

1. Pre-process the dataset of $\approx 3000$ samples: impute missing values, standardize predictors, and stratify into training and testing subsets.

2. Train each of the six algorithms using cross-validation to ensure fair evaluation (hyper-parameter tuning where applicable).

3. Assess model performance with accuracy, ROC-AUC, and confusion matrices on an unseen test set.

4. Interpret variable importance to identify which chemical features drive potability decisions.

5. Deliver a concise recommendation of the best-performing, most practical model for potential deployment in routine water-quality screening.

# Data Citation

I have obtained the dataset from one of the recommended data sources provided by Prof. Coburn. It's the water potability data from [Kaggle](https://www.kaggle.com/datasets/developerghost/water-potability/data). A formal citation is included in the References section. 

# Data Directories

The data directories have been chnaged and they are now in different folders, you might have to manipulate the paths to make sure everything is working
