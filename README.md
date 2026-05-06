# Resume Analysis + Job Technology

This project is a single-page website that presents three AI-focused career tools:

- AI Resume Feedback Tool
- AI Job Description Translator
- AI Cover Letter Feedback

The page is designed as a polished frontend project with interactive demos, portfolio-style UI, and lightweight automated tests.

## What This Project Includes

This submission includes all of the following:

- the project code
- automated tests
- a clear README
- instructions for running the project
- instructions for running the tests
- a short explanation of what skill or technology the project was meant to demonstrate

## Project Code

Main files in this project:

- [index.html](index.html) — the full site layout, styling, and browser-side demo logic
- [tests/test_site.py](tests/test_site.py) — automated tests for the project structure and required UI elements
- [README.md](README.md) — project overview and setup instructions

## Automated Tests

The project includes automated tests using Python's built-in `unittest` framework.

The tests check that:

- the main HTML file exists
- the page title is correct
- only the three required project sections are present
- the featured strip contains exactly three cards
- each tool has only the single input field requested
- the navigation points to the three included project sections

## Instructions for Running the Project

1. Open a terminal in the project folder.
2. Start a local static server.
3. Open the local site in the browser.

Example:

```bash
cd "/Users/gunabanka/Desktop/IS219 Resume Analysis + Job Technology"
python -m http.server 8000 --bind 127.0.0.1
```

Then open:

```text
http://127.0.0.1:8000/
```

## Instructions for Running the Tests

Run the automated test suite from the project root:

```bash
cd "/Users/gunabanka/Desktop/IS219 Resume Analysis + Job Technology"
python -m unittest discover -s tests -p "test_*.py"
```

If all tests pass, you should see output showing the test run completed successfully.

## Skills and Technology Demonstrated

This project was meant to demonstrate the following skills and technologies:

- **HTML/CSS frontend development** — building a responsive single-page site with a polished layout
- **JavaScript interaction design** — handling user input and generating dynamic on-page feedback
- **UI recreation and styling** — adapting the look and feel of an existing reference site into a custom project
- **Responsive design** — supporting desktop and mobile layouts, including a mobile navigation menu
- **Automated testing** — validating required project structure and behavior with a repeatable test suite
- **AI product presentation** — showing how AI-oriented tools can be communicated through clean product-style interfaces

## Included Tools

### AI Resume Feedback Tool
Users can paste a resume and receive:

- a simulated score
- rewrite suggestions
- a prioritized fix list

### AI Job Description Translator
Users can enter a job position and receive:

- role highlights
- a plain-language summary
- a short preparation plan

### AI Cover Letter Feedback
Users can paste a cover letter and receive:

- a relevance score
- revision notes
- a revised version of the text

## Notes

- The project intentionally includes only the three required tools.
- The interactive behavior is frontend-only and does not require a backend.
- The automated tests use only Python standard library modules.

## LinkedIn (Resume included)
- https://www.linkedin.com/in/guna-banka-785179269/

## Vercel Link
https://resume-analysis-job-technology-guna.vercel.app/
