# Global Market Explorer

A Streamlit dashboard for exploratory international market research focused on
Germany and boAt. The dashboard includes market, competitor, SWOT, customer
segmentation, STP, market-entry, and AI-prompt sections.

## Requirements

- Python 3.12
- The packages listed in `requirements.txt`
- A modern browser with WebGL enabled to render the interactive globe

## Run locally

From the project directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

On macOS or Linux, activate the environment with
`source .venv/bin/activate` instead.

## Project files

- `app.py` is the Streamlit entry point and contains the dashboard.
- `assets/earth.jpg` is the bundled satellite Earth texture.
- `data/market_data.csv` and the files under `modules/` are currently empty
  placeholders; the dashboard does not depend on them.

The globe remains a real, interactive 3D sphere. Its Earth texture is included
in the repository, so the texture itself does not need an internet connection.
Three.js and OrbitControls are loaded from jsDelivr with unpkg as a fallback;
the browser therefore needs access to at least one CDN and WebGL for the globe
to render. If the local texture cannot be read, the app displays a visible
status and renders an interactive 3D globe with a procedural fallback texture.
Other dashboard content remains available if browser WebGL is disabled.

## Deploy to Streamlit Community Cloud

1. Review the files you intend to publish and make sure no credentials or
   private data are included. The `.gitignore` excludes virtual environments,
   caches, `.env` files, and Streamlit secrets.
2. Create a GitHub repository named `global-market-explorer` and choose whether
   it should be public or private.
3. From this project directory, initialize and push the project. Replace
   `<YOUR-USERNAME>` with your GitHub username:

   ```powershell
   git init -b main
   git add app.py requirements.txt README.md .gitignore assets data modules
   git status --short
   git diff --cached --name-only
   git commit -m "Prepare Global Market Explorer for deployment"
   git remote add origin https://github.com/<YOUR-USERNAME>/global-market-explorer.git
   git push -u origin main
   ```

   Review the staged file list before committing. Authenticate with GitHub
   using its normal browser or credential-manager flow when prompted.
4. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) and
   connect your GitHub account.
5. Create a new app and select the `global-market-explorer` repository, the
   `main` branch, and `app.py` as the main file path.
6. In the app's advanced settings, select Python 3.12, then deploy.
7. Check the deployed app's logs if installation or startup fails. Future
   commits pushed to `main` will be deployed by Community Cloud.

No secrets are required by the current app. If secrets are added later, store
them in Community Cloud's app secrets settings and never commit them to GitHub.
