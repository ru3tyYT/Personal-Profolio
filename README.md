# Mason's Portfolio Website

A modern, interactive portfolio website showcasing projects with a dynamic typing animation and smooth user experience.

## Features

- 🎨 Modern black and blue theme
- ⌨️ Dynamic typing animation on landing page
- 📱 Fully responsive design
- 🎯 Smooth scrolling and hover effects
- 🚀 Project showcase with descriptions
- 🔗 GitHub profile integration

## Files Included

- `index.html` - Frontend HTML file with embedded CSS and JavaScript
- `backend.py` - Python Flask backend server
- `README.md` - This documentation file

## Prerequisites

Before you begin, make sure you have Python installed on your computer.

- **Python 3.7 or higher** - [Download Python](https://www.python.org/downloads/)

## Step-by-Step Setup Instructions

### Step 1: Install Python Dependencies

Open your terminal or command prompt and run:

```bash
pip install flask flask-cors
```

**What this does:** Installs Flask (web framework) and Flask-CORS (enables frontend-backend communication)

### Step 2: Organize Your Files

Create a new folder for your project and place these files inside:
```
my-portfolio/
├── index.html
├── backend.py
└── README.md
```

### Step 3: Run the Backend Server

1. Open terminal/command prompt
2. Navigate to your project folder:
   ```bash
   cd path/to/my-portfolio
   ```
3. Run the Python backend:
   ```bash
   python backend.py
   ```

You should see:
```
Starting Portfolio Backend Server...
Server will be available at: http://localhost:5000
```

### Step 4: Open the Frontend

**Option A - Through Backend (Recommended):**
1. Keep the backend running
2. Open your web browser
3. Go to: `http://localhost:5000`

**Option B - Direct File Access:**
1. Simply double-click `index.html` to open it in your browser
2. The website will work, but without backend API features

### Step 5: Test the Website

You should see:
- A landing page with "Mason can ___" typing animation
- Smooth scroll down arrow
- Projects section with two project boxes
- GitHub link in the footer
- Hover effects on project boxes

## Troubleshooting

### Problem: "Module not found" error
**Solution:** Make sure you installed the dependencies:
```bash
pip install flask flask-cors
```

### Problem: "Port already in use"
**Solution:** Either:
- Stop other programs using port 5000
- Or change the port in `backend.py` (change `port=5000` to another number like `port=8000`)

### Problem: Website doesn't load
**Solution:** 
- Make sure `index.html` is in the same folder as `backend.py`
- Check that the backend terminal shows no errors
- Try accessing `http://127.0.0.1:5000` instead

## Deployment Options

### Option 1: Deploy to Replit (Easiest)

1. Go to [Replit.com](https://replit.com) and create an account
2. Click "Create Repl"
3. Choose "Python" template
4. Upload your files (`index.html`, `backend.py`)
5. In the Shell, run: `pip install flask flask-cors`
6. Click the "Run" button
7. Your site will be live at the provided Replit URL!

### Option 2: Deploy to Render

1. Create account at [Render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository (create one first with your files)
4. Configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python backend.py`
5. Create a `requirements.txt` file with:
   ```
   flask
   flask-cors
   ```
6. Deploy and get your live URL!

### Option 3: Deploy to PythonAnywhere

1. Sign up at [PythonAnywhere.com](https://www.pythonanywhere.com)
2. Go to "Web" tab → "Add a new web app"
3. Choose "Flask" and Python 3.x
4. Upload your files via "Files" tab
5. Edit the WSGI configuration file to point to your `backend.py`
6. Reload the web app
7. Access your site at `yourusername.pythonanywhere.com`

### Option 4: GitHub Pages (Frontend Only)

Since GitHub Pages only hosts static files, you can deploy just the frontend:

1. Create a GitHub repository
2. Upload `index.html`
3. Rename it to `index.html` (if not already)
4. Go to Settings → Pages
5. Select branch and folder
6. Save and get your GitHub Pages URL!

**Note:** Backend features won't work on GitHub Pages, but the website will display perfectly.

## Customization Guide

### Change Colors
Edit the CSS in `index.html`:
- Background: Look for `background: linear-gradient` lines
- Blue accent: Replace `#00d4ff` with your preferred color
- Update all instances for consistent theming

### Add More Projects
In `index.html`, find the `<div class="projects-container">` section and duplicate a project box:

```html
<div class="project-box">
    <span class="project-icon">🎮</span>
    <h3 class="project-title">Your Project Name</h3>
    <ul class="project-description">
        <li>Feature 1</li>
        <li>Feature 2</li>
    </ul>
    <a href="your-link" class="project-link">View Project →</a>
</div>
```

### Change Typing Animation Words
In `index.html`, find this line:
```javascript
const words = ['code', 'decompile', 'obfuscate', 'and more'];
```
Replace with your own words!

## Support

If you encounter any issues:
1. Check that Python is properly installed: `python --version`
2. Verify all dependencies are installed: `pip list`
3. Make sure all files are in the same directory
4. Check for typos in file names

## License

This project is free to use and modify for personal and commercial purposes.

---

**Created by Mason** | [GitHub: ru3tyYT](https://github.com/ru3tyYT)
