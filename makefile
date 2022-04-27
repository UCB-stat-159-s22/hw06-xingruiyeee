PNG_FILES = $(wildcard figures/*.png)
WAV_FILES = $(wildcard audio/*.wav)

#Build Jupyter Book
.PHONY : html
html: jupyter-book build .

.PHONY : html-hub
html-hub: 
        sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000



# Run Jupyter Notebook to obtain figures, audio files
.PHONY : all
all :
    jupyter execute index.ipynb

# Clean figures, audio, and build book
.PHONY : clean
clean :
    rm -f $(PNG_FILES)
    rm -f $(WAV_FILES)
    rm -rf _build/html/

#Create Environment
.PHONY: env
env:
    mamba env create -f environment.yml -p ~/envs/ligo
    bash -ic 'conda activate ligo
    python -m ipykernel install --user --name ligo --display-name "IPython - hw06ligo"'

.PHONY : variables
variables :
    PNG_FILES: $(PNG_FILES)
    CSV_FILES: $(WAV_FILES)