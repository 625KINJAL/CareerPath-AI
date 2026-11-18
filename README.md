# CareerPath AI – Intelligent Career Guidance & Job Prediction

A beginner-friendly M.Tech AIML academic project that recommends career roles from a student's education, skills, interests, experience and optional resume.

## Features
- Top-three career-role recommendations
- TF-IDF + Logistic Regression text classifier
- Skill matching and skill-gap analysis
- Career learning roadmap
- Indicative India salary bands
- Optional PDF, DOCX and TXT resume text extraction
- CSV career report download
- Streamlit dashboard

## Important academic limitation
This is an educational prototype. The included role profiles and salary bands are curated examples. Training variations are synthetically generated from those profiles. The displayed model score is not the probability of getting hired and is not real-world hiring accuracy. Do not use it for employment decisions.

## 1. Requirements
- Windows 10/11
- Python 3.10–3.12 recommended
- VS Code

## 2. Open the project
Extract the ZIP. In VS Code choose **File → Open Folder** and select `CareerPath_AI`.

## 3. Create and activate virtual environment (PowerShell)
```powershell
python -m venv venv
venv\Scripts\activate
```

## 4. Install libraries
```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 5. Run locally
```powershell
python -m streamlit run app.py
```
Open the Local URL printed in the terminal, usually `http://localhost:8501`.

Stop the app with `Ctrl+C`.

## 6. Upload to GitHub
Create a new repository named `CareerPath-AI` at https://github.com/new.
In the VS Code terminal, from inside the `CareerPath_AI` folder:
```powershell
git init
git add .
git commit -m "Initial CareerPath AI project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/CareerPath-AI.git
git push -u origin main
```
Replace `YOUR_USERNAME` with your GitHub username. Do not upload your `venv` folder. Add this to `.gitignore` if needed:
```
venv/
__pycache__/
.streamlit/secrets.toml
```

## 7. Deploy on Render
1. Push the project to GitHub.
2. Sign in at https://render.com using GitHub.
3. Choose **New → Web Service** and connect `CareerPath-AI`.
4. Render can read `render.yaml`; otherwise use:
   - Build command: `pip install -r requirements.txt`
   - Start command: `streamlit run app.py --server.address 0.0.0.0 --server.port $PORT`
5. Deploy and open the public URL Render provides.

Free hosting availability and sleep limits can change. Never commit API keys, passwords or private resume files to GitHub.

## Project structure
```
CareerPath_AI/
├── app.py
├── career_model.py
├── requirements.txt
├── render.yaml
├── README.md
└── data/
    └── career_roles.csv
```

## Viva explanation
1. User enters education, experience, skills and interests.
2. The app combines this information into a text profile.
3. TF-IDF converts text into numerical features.
4. Logistic Regression ranks likely role labels.
5. The app compares profile terms against each role's curated skill list.
6. It displays role matches, missing skills and a learning roadmap.
