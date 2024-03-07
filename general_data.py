import os

PROJECT_PATH = os.getcwd()
DATA_PATH_ABS = os.path.join(PROJECT_PATH, "static", "data")
ASSETS_PATH_ABS = os.path.join(PROJECT_PATH, "static", "assets")
PAPER_PATH_ABS = os.path.join(ASSETS_PATH_ABS, "papers")

ASSETS_PATH = os.path.join(" ", "static", "assets")
PAPER_PATH = os.path.join(ASSETS_PATH, "papers")

collab_moschi = dict(
    name="Moschi Riccardo",
    link="https://www.linkedin.com/in/riccardo-moschi-716506220/"
)

collab_levoci = dict(
    name="Le Voci Ismaele Nachit",
    link="https://www.linkedin.com/in/ismaele-le-voci/"
)

collab_loddo = dict(
    name="Loddo Luca",
    link="https://www.linkedin.com/in/luca-loddo-63752323a/"
)

collab_rondena = dict(
    name="Rondena Matteo",
    link="https://www.linkedin.com/in/matteo-rondena-3791412b9/"
)

collab_muko = dict(
    name="Mucko Luka",
    link="https://www.linkedin.com/in/luka-mucko-066130164/"
)

collab_razvan = dict(
    name="Razvan Potcuveanu",
    link="https://www.linkedin.com/in/razvan-florin/"
)

trnet = dict(
    id="trnet",
    name="Transportation Network Analysis",
    short_desc="Analysis of the structure and vulnerabilities of the Transportation Network: Deutsche Bahn",
    related_exam="Data Analytics",
    year="2024",
    page_link="/works/trnet",
    dash_link="https://dash-da-trnet-26fc8d9cdb9c.herokuapp.com/",
    git_repo_link="https://github.com/LucaPoli59/Da_TrNet",
    collaborators=None,
    paper_it_path=os.path.join(PAPER_PATH, "trnet_it.pdf"),
    paper_en_path=os.path.join(PAPER_PATH, "trnet_en.pdf"),
    long_desc="This report presents a detailed analysis of the German railway network, focusing on the GTFS dataset "
              "of Deuthesche Bahn (BN). Through data conversion into DataFrame and subsequent graphical "
              "representation, the structure and connectivity of the graph were examined. Various centrality metrics "
              "were used to assess node importance and network robustness.\nSubsequently, simulations of graph "
              "attacks, both random and targeted at nodes with high centrality, were conducted. The results indicate "
              "a significant vulnerability of the network to targeted attacks, particularly those based on Degree, "
              "Betweenness, Closeness, and Pagerank centrality measures. However, the network proved robust against "
              "random attacks. Metrics such as Strong and Weak Giant Component, along with Average Centrality, "
              "were identified as significant indicators for evaluating the effects of attacks.",
)

fma = dict(
    id="fma",
    name="Factor Models Strategies",
    short_desc="Creation of multiple portfolios strategies based on factor models, inspired by QEPM",
    related_exam="Financial Markets Analytics",
    year="2024",
    page_link="/works/fma",
    dash_link="https://dash-fma-53324966f668.herokuapp.com/",
    git_repo_link="https://github.com/LucaPoli59/fma",
    collaborators=None,
    paper_it_path=os.path.join(PAPER_PATH, "fma_it.pdf"),
    paper_en_path=os.path.join(PAPER_PATH, "fma_en.pdf"),
    long_desc="This project introduces a Factor model applied to a collection of European Stocks, employing both "
              "univariate and multivariate strategies. Factor models aim to capture underlying factors influencing "
              "financial instruments' returns.\nUnivariate strategies on 10 factors were implemented, "
              "and the top-performing ones, including RSI_14D, NORMALIZED_ACCRUALS_CF, NET_DEBT_PER_SHARE, "
              "PX_TO_BOOK_RATIO, and WACC_COST_EQUITY, were identified. While not considered robust, these factors "
              "served as a basis for developing multivariate strategies.\nThe subsequent multivariate analysis "
              "revealed that both simple and weighted versions of the Simultaneous Screening with zscore outperformed "
              "the sequential screening. The z-score approaches exhibited comparable risk and performance, "
              "with the weighted version showing superiority when excluding initial months. Despite lower turnover, "
              "the sequential screening's performance lagged behind the z-score strategies, showcasing the efficacy "
              "of factor models in enhancing investment strategies.",
)

dl = dict(
    id="dl",
    name="Deep Learning Assignments",
    short_desc="Collection of Assignments for the Deep Learning course",
    related_exam="Deep Learning",
    year="2023",
    page_link="/works/dl",
    dash_link=None,
    git_repo_link="https://github.com/LucaPoli59/DeepLearning",
    collaborators=[collab_muko],
    paper_it_path=None,
    paper_en_path=None,
    long_desc="In this course, I undertook the implementation of foundational deep learning models, both from scratch "
              "and using PyTorch for advanced applications. The curriculum covered topics ranging from stochastic "
              "gradient descent algorithms to diverse neural network architectures, including CNNs, RNNs, "
              "transformers, self-supervised methods, and generative models. Specific models, such as Transformer, "
              "CNN (Unet), RNN, Denoising Diffusion, Autoencoders, VAE, GAN, Probabilistic Models (SimCLR, CLIP), "
              "Autoregressive Models, and Flow Models, were explored hands-on.\nBy the course's end, I not only "
              "mastered the practical aspects of implementing and training these models but also developed critical "
              "evaluation skills, enabling me to diagnose issues and make informed decisions for specific use cases."
)

rascal_rover = dict(
    id="rascal_rover",
    name="Lego Mars Rover Project",
    short_desc="Design and implementation of a Lego Mars Rover with a DSL",
    related_exam="Design of Embedded Systems",
    year="2023",
    page_link="/works/rascal_rover",
    dash_link=None,
    git_repo_link="https://github.com/LucaPoli59/rascal_rover",
    collaborators=[collab_razvan],
    paper_it_path=None,
    paper_en_path=None,
    long_desc="The project involves developing a domain-specific language (DSL) using Rascal to program a Lego rover. "
              "This DSL generates the necessary Python code to control the rover through specified missions. Rover "
              "requirements include safely executing missions sequentially, detecting colors, distant objects, "
              "and impacts, as well as utilizing a measurement arm. The DSL allows users to define custom missions, "
              "specify the server's MAC address, and ensures the generation of correct Python code. Additionally, "
              "it is configurable by users for detectable colors, motor speed, movement parameters, and mission "
              "feedback. In summary, the project aims to provide a flexible and user-friendly solution for advanced "
              "programming of a Lego rover through the implementation of an effective DSL.",
)

sarcasm = dict(
    id="sarcasm",
    name="Sarcasm Detection",
    short_desc="Creation of a Deep Learning model to detect sarcasm in reddit comments",
    related_exam="Data Analytics",
    year="2023",
    page_link="/works/sarcasm",
    dash_link=None,
    git_repo_link="https://github.com/LucaPoli59/DA_Sarcasm",
    collaborators=None,
    paper_it_path=os.path.join(PAPER_PATH, "sarcasm_it.pdf"),
    paper_en_path=os.path.join(PAPER_PATH, "sarcasm_en.pdf"),
    long_desc="This project focused on tackling the challenging task of sarcasm detection within the realm of Natural "
              "Language Processing (NLP), employing innovative and experimental approaches such as Transformers, "
              "albeit on a smaller scale. Utilizing a dataset comprising 5 features and over 1 million instances, "
              "a meticulous preprocessing phase enabled various analyses. Information rates were calculated for "
              "different contextual elements and text types. The datasets were then processed based on the insights "
              "gained from the training dataset, leading to the training of a model leveraging BERT and "
              "TransformerEncoder.\nThe analyses conducted in the initial chapters proved instrumental in enhancing "
              "the model's accuracy by excluding redundant data, thereby reducing computational resources and "
              "processing time. While the model demonstrates excellent generalization capabilities, a certain degree "
              "of underfitting is observed. In the future, with improved computational resources, hyperparameter "
              "tuning could be performed to identify the optimal number of neurons in internal layers and the number "
              "of heads in the TransformerEncoder. Furthermore, experimentation with additional inputs or larger BERT "
              "models could be explored."
)

quick_answ = dict(
    id="quick_answ",
    name="Quick Answer",
    short_desc="Java Spring-powered platform connecting students and responders for personalized study assistance",
    related_exam="Software Development Process",
    year="2022",
    page_link="/works/quick_answ",
    dash_link=None,
    git_repo_link="https://gitlab.com/work2gether/2022_assignment3_quickanswer",
    collaborators=[collab_moschi, collab_loddo, collab_rondena],
    paper_it_path=None,
    paper_en_path=None,
    long_desc="The QuickAnswer project was implemented using Java Spring, translating the high-level concept into a "
              "functional application. QuickAnswer serves as an online platform that facilitates interaction between "
              "students (Askers) and responders (teachers, professionals, or fellow students) for private responses "
              "to study-related queries.\nThe implemented project allows Askers to post questions or requests, "
              "and Responders can submit quotes specifying response details such as mode (textual, video, "
              "private lesson), price, depth level, and response time. Askers then select the most suitable quote and "
              "proceed with payment.\nThe system handles the notification and submission process for the chosen "
              "Responder. After the Asker evaluates the response, funds are released to the Responder. The Java "
              "Spring implementation ensures a seamless and efficient interaction flow between Askers and Responders, "
              "enhancing the overall user experience within the QuickAnswer platform.",
)

ml_airline = dict(
    id="ml_airline",
    name="Airline Satisfaction Prediction",
    short_desc="Use of Machine Learning models to predict customer satisfaction for an airline",
    related_exam="Machine Learning",
    year="2022",
    page_link="/works/ml_airline",
    dash_link=None,
    git_repo_link="https://github.com/LucaPoli59/ML_Airline",
    collaborators=[collab_moschi],
    paper_it_path=os.path.join(PAPER_PATH, "airline_it.pdf"),
    paper_en_path=os.path.join(PAPER_PATH, "airline_en.pdf"),
    long_desc="This university project explores the application of machine learning models to predict customer "
              "satisfaction for an airline, utilizing a dataset comprising 5000 instances. Employing preprocessing "
              "techniques, random sampling, and feature reduction through Boruta and PCA strategies, "
              "the study achieved a 74% variance with 7 selected features. The predictive power of Neural Networks, "
              "featuring 7 neurons, and Support Vector Machines (SVM) was harnessed for classification. The models "
              "exhibited high accuracy and precision when evaluated on a test dataset of 500 instances. Confusion "
              "matrix analysis validated the robust performance of the employed models, highlighting the "
              "effectiveness of the applied methodologies in predicting customer satisfaction for airline services."
)

bachelor_thesis = dict(
    id="bachelor_thesis",
    name="Volatility Forecasting for Option Trading",
    short_desc="Application of Recurrent Neural Networks for Volatility Forecasting in Option Trading",
    related_exam="Bachelor Thesis",
    year="2022",
    page_link="/works/bachelor_thesis",
    dash_link=None,
    git_repo_link="https://github.com/LucaPoli59/VFOT",
    collaborators=None,
    paper_it_path=os.path.join(PAPER_PATH, "bachelor_thesis_it.pdf"),
    paper_en_path=os.path.join(PAPER_PATH, "bachelor_thesis_en.pdf"),
    long_desc="This thesis explores the application of Machine Learning, specifically Long Short-Term Memory (LSTM) "
              "neural networks, to predict stock price volatility for short-term options trading. The project "
              "encompasses theoretical foundations, data elaboration, model implementation, trading strategies, "
              "and concluding insights.\nThe initial chapters introduce Machine Learning, Neural Networks, "
              "recurrent variations like LSTM, and concepts related to options and volatility. The project's "
              "objective is to create a predictive system leveraging LSTM to anticipate stock price volatility and "
              "profit from short-term trading with options.\nData elaboration involves downloading, preprocessing, "
              "feature selection, PCA analysis, scaling, lagging, and splitting. Three distinct LSTM models are "
              "implemented and compared based on various hyperparameter configurations, scaler types, and feature "
              "selection strategies.\nTrading strategies are devised based on the neural network predictions, "
              "guiding the system to open long or short positions using four different volatility spreads. These "
              "spreads, designed for implicit volatility exposure, are delta-neutral and adjusted for vega and theta "
              "considerations.\nResults indicate that, despite various attempts and methodologies employed, "
              "the proposed solution struggles to consistently outperform the Naive forecast. Future developments may "
              "explore the potential link between volatility and the Random Walk theory or introduce alternative "
              "approaches, such as isolating a single volatility or incorporating reinforcement learning techniques."
)

bifs = dict(
    id="bifs",
    name="Financial BI Project: Portfolio Optimization & Trading Strategies",
    short_desc="This project explores portfolio optimization and trading strategies in financial services through data analysis and forecasting.",
    related_exam="Business Intelligence for Financial Services",
    year="2021",
    page_link="/works/bifs",
    dash_link=None,
    git_repo_link="https://github.com/LucaPoli59/BISF",
    collaborators=None,
    paper_it_path=os.path.join(PAPER_PATH, "bifs_it.pdf"),
    paper_en_path=os.path.join(PAPER_PATH, "bifs_en.pdf"),
    long_desc="This Business Intelligence project in Financial Services explores data utilization, descriptive "
              "statistics, portfolio analysis, trading strategies, and forecasting. Analyzing data from the first 108 "
              "months, the project constructs a portfolio with 10 months of forecasted data, achieving a high Sharpe "
              "ratio due to reduced volatility. Descriptive statistics delve into returns and their distribution "
              "across various securities, emphasizing specific stocks like Wells Fargo, Tesla, "
              "and Qualcomm.\nPortfolio analysis optimizes through correlations and betas, comparing optimal versus "
              "actual returns, notably impacted by stocks like Tesla. A trading strategy based on the MACD indicator "
              "is outlined, featuring a realistic 14-day lock period between trades.\nForecasting employs a neural "
              "network model for predicting stock prices, demonstrating efficacy. The project concludes with insights "
              "on portfolio optimization, the influence of specific stocks, and a comprehensive evaluation of "
              "financial forecasting and trading strategies."
)

c_project = dict(
    id="c_project",
    name="C++ Project: Implementation of Generic set with pointers, and a graphic tool with Qt",
    short_desc="Implementation of a file system in C",
    related_exam="Operating Systems",
    year="2021",
    page_link="/works/c_project",
    dash_link=None,
    git_repo_link="https://github.com/LucaPoli59/uni_proj_c",
    collaborators=None,
    paper_it_path=os.path.join(PAPER_PATH, "c_project_it.pdf"),
    paper_en_path=os.path.join(PAPER_PATH, "c_project_en.pdf"),
    long_desc="This project involves the implementation in C++ of a generic set with pointers that can perform some "
              "operations.\nThe project also includes the implementation of a graphic tool with Qt that displays some "
              "informations about a selected text file."
)

lp_project = dict(
    id="lp_project",
    name="Prim Algorithm Implementation in Prolog and Lisp",
    short_desc="Implementation of the Prim Algorithm in Prolog and Lisp",
    related_exam="Programming Languages",
    year="2020",
    page_link="/works/lp_project",
    dash_link=None,
    git_repo_link="https://github.com/LucaPoli59/uni_proj_lp",
    collaborators=[collab_moschi, collab_levoci],
    paper_it_path=None,
    paper_en_path=None,
    long_desc="The aim of this project is to implement the Prim's algorithm for solving the Minimum Spanning Tree ("
              "MST) problem in connected, undirected graphs with non-negative weights. To achieve the implementation "
              "of these algorithms, it is essential to create an implementation of a MINHEAP."
)

projects = [bachelor_thesis, trnet, fma, dl, rascal_rover, sarcasm, quick_answ, ml_airline, bifs, c_project, lp_project]
projects_dict = {project["id"]: project for project in projects}
