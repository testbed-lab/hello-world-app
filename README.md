# Hello World Web Application

A simple, modern web application that displays a friendly "Hello" message.

## Features

- ⚡ Fast loading - zero dependencies
- 🌐 Accessible via local web server
- 📱 Mobile responsive
- 🎨 Modern gradient design
- 🧩 Easy to extend

## Quick Start

### Option 1: Direct File Open
1. Open `index.html` in any web browser
2. Done! No server required for basic use

### Option 2: With Local Web Server
1. Open terminal in the project directory
2. Run one of the following:

**Python 3:**
```bash
python3 -m http.server 8000
```

**Python 2:**
```bash
python -m SimpleHTTPServer 8000
```

**Node.js:**
```bash
npx http-server -p 8000
```

**PHP:**
```bash
php -S localhost:8000
```

3. Open browser to: `http://localhost:8000`

## Project Structure

```
hello-world-app/
├── index.html           # Main HTML file (self-contained)
├── ARCHITECTURE.md      # Architecture documentation
└── README.md            # This file
```

## Technology Stack

- **HTML5** - Semantic markup
- **CSS3** - Modern styling (Flexbox, gradients, animations)
- **Vanilla JavaScript** - No dependencies needed

## Deployment

### Netlify (Drag & Drop)
1. Go to [netlify.com](https://app.netlify.com/drop)
2. Drag the `hello-world-app` folder
3. Done! Get your deploy URL

### Vercel (CLI)
```bash
npm i -g vercel
vercel deploy
```

### GitHub Pages
1. Push to a GitHub repository
2. Go to Settings → Pages
3. Select `gh-pages` branch
4. Save

## Customization

### Change the Message
Edit the `<h1>` tag in `index.html`:
```html
<h1>Your Message Here!</h1>
```

### Change the Colors
Edit the CSS gradient:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

## Browser Support

| Browser | Version |
|---------|---------|
| Chrome | ✅ Latest |
| Firefox | ✅ Latest |
| Safari | ✅ Latest |
| Edge | ✅ Latest |

## License

Public Domain - Feel free to use however you like!

## Support

For questions or issues, see the `ARCHITECTURE.md` file for detailed documentation.
