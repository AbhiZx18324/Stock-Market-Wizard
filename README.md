# Stock Market Wizard

Quickly summarize the content and get the information you need regarding stock market in **real-time** from online finance news streaming platforms, here, [Yahoo Finance](https://finance.yahoo.com/topic/stock-market-news/). The same tool can be used with other news streaming platforms.
## Demo

See how the tool works:

![Stock Market Wizard tool demo](Demo/stock-market-wizard.mp4)

As you can see the LLM App enables AI-powered summarization of multiple news regarding the stock market, and indexes input data in real-time just after getNews.py updates the ./MarketNews folder.

## How to run the tool

### Run with Docker (preferred)

1. Create `.env` file in the root directory of the project, copy and paste the below config. Replace the `OPENAI_API_KEY` configuration value with your key `<Your Token>`

```bash
HOST=0.0.0.0
PORT=8080
EMBEDDING_DIMENSION=1536
EMBEDDER_LOCATOR=text-embedding-ada-002
MODEL_LOCATOR=gpt-3.5-turbo
MAX_TOKENS=200
TEMPERATURE=0.0
OPENAI_API_KEY=<Your Token>
PATHWAY_PERSISTENT_STORAGE=/tmp/cache
```

2. From the project root folder, open your terminal and run `docker compose up`.
3. Navigate to `localhost:8501` on your browser when docker installion is successful.

### Run from the source

#### Prerequisites

1. Make sure that [Python](https://www.python.org/downloads/) 3.10 or above installed on your machine.
2. Download and Install [Pip](https://pip.pypa.io/en/stable/installation/) to manage project packages.
3. Create an [OpenAI](https://openai.com/) account and generate a new API Key: To access the OpenAI API, you will need to create an API Key. You can do this by logging into the [OpenAI website](https://openai.com/product) and navigating to the API Key management page.

Then, follow the easy steps to install and get started using the sample app.

#### Step 1: Clone the repository

This is done with the `git clone` command followed by the URL of the repository:

```bash
git clone https://github.com/AbhiZx18324/Stock-Market-Wizard.git
```

Next,  navigate to the project folder:

```bash
cd Stock-Market-Wizard
```

#### Step 2: Set environment variables

Create `.env` file in the root directory of the project, copy and paste the below config, and replace the `<Your Token>` configuration value with your key.

```bash
HOST=0.0.0.0
PORT=8080
EMBEDDING_DIMENSION=1536
EMBEDDER_LOCATOR=text-embedding-ada-002
MODEL_LOCATOR=gpt-3.5-turbo
MAX_TOKENS=200
TEMPERATURE=0.0
OPENAI_API_KEY=<Your Token>
PATHWAY_PERSISTENT_STORAGE=/tmp/cache
```

#### Step 3 (Optional): Create a new virtual environment

Create a new virtual environment in the same folder and activate that environment:

```bash
python -m venv pw-env && source pw-env/bin/activate
```

#### Step 4: Install the app dependencies

Install the required packages:

```bash
pip install -U pathway
pip install -U requests
pip install -U bs4
pip install -U datetime
pip install -U openai
pip install -U python-dotenv
pip install -U streamlit
pip install -U jsonlines
```

#### Step 5: Run the Pathway API

You start the application by running `main.py`:

```bash
python main.py
```

#### Step 6: Run Streamlit UI

Open ui.py and change the following line:
`api_host = "rag"` to `api_host = "127.0.0.1"`<br>
You can run the UI separately by running Streamlit app
`streamlit run ui.py` command. It connects to the Pathway's backend API automatically and you will see the UI frontend is running on your browser.
