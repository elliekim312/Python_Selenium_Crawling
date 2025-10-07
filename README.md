# Google Image Crawler

A Python Selenium script that automates Google Image Search to download images based on keywords.

## Requirements

- Python 3.x
- Selenium library
- Google Chrome browser
- ChromeDriver (matching your Chrome version)

## Installation

### 1. Install Selenium library
```bash
pip install selenium
```

### 2. Move to selenium folder
```bash
cd selenium
```

### 3. Activate the virtual environment
```bash
source bin/activate
```

**Windows:**
```bash
bin\activate
```

## Usage

### Basic Command
```bash
python downloadImgs.py --keyword="your search keyword"
```

### Examples
```bash
# Using full option
python downloadImgs.py --keyword="New York"

# Using shorthand
python downloadImgs.py -k "cat"
```

### Options
- `--keyword` or `-k`: Search keyword for images to download
- `--help` or `-h`: Display help message

## Output

Images are saved in the `img/` folder with the format:
```
img/google_<keyword>_<number>.png
```
