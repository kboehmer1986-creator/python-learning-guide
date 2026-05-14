# Python Learning Guide

A free and open-source Python learning guide for self-learners as well as students that is covering everything from basics to advanced topics. Includes PDFs, Markdown files, code examples, exercises, quizzes and interactive modules.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [How to Use](#how-to-use)
- [PDF Generation](#pdf-generation)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository provides a structured and comprehensive guide to learning Python that is designed for beginners to advanced learners. It includes:

- Theoretical explanations for all Python concepts.
- Practical examples and code snippets.
- Exercises and projects to reinforce learning.
- Quizzes to test your knowledge.
- Interactive modules ( Jupyter Notebooks ) for hands-on practice.

## Features

- Beginner to Advanced: Covers Python from the ground up.
- Multiple Formats: Available as PDF, Markdown and LaTeX.
- Interactive Learning: Includes Jupyter Notebooks for live coding.
- Exercises & Projects: Practical tasks to apply what you learn.
- Quizzes: Test your understanding with multiple-choice questions.
- Free & Open-Source: Licensed under Creative Commons ( CC0-1.0 license ).

## Repository Structure


python-learning-guide/

|       |

|       |-- README.md

|       |-- docker-Compose.yml

|       |-- requirements.txt

|       |__ LICENSE

|

|-- documentation/

|       |

|       |-- ...

|       |-- ...

|

|-- latex/

|       |

|       |__ python-learning-guide.tex

|

|-- markdown/

|       |

|       |__ python-learning-guide.md

|

|-- pdf/

|       |

|       |__ python-learning-guide.pdf

|

|-- code/

|       |

|       |-- basics/

|       |       |-- functions.py

|       |       |-- loops.py

|       |       |__ variables.py

|       |

|       |-- intermediate/

|       |       |-- classes.py

|       |       |__ inheritance.py

|       |

|       |__ advanced/

|               |-- decorators.py

|               |__ generators.py

|

|-- interactive/

|       |__ notebooks/

|               |-- advanced.ipynb

|               |-- basics.ipynb

|               |-- exercises.ipynb

|               |-- intermediate.ipynb

|               |__ solutions.ipynb

|

|-- exercises/

|       |-- advanced/

|       |       |-- decorators_exercise.md

|       |       |__ generators_exercise.md

|       |

|       |-- beginner/

|       |       |-- functions_exercise.md

|       |       |-- loops_exercise.md

|       |       |__ variables_exercise.md

|       |

|       |-- intermediate/

|       |       |-- classes_exercise.md

|       |       |__ inheritance_exercise.md

|       |

|       |__ solutions/

|               |-- decorators_solution.py

|               |-- generators_solution.py

|               |-- classes_solution.py

|               |-- inheritance_solution.py

|               |-- functions_solution.py

|               |-- variables_solution.py

|               |__ loops_solution.py

|

|-- quizzes/

|       |-- advanced_quiz.md

|       |-- basics_quiz.md

|       |__ intermediate_quiz.md

|

|-- resources/

|       |-- cheat_sheets/

|       |       |__ python_cheat_sheet.pdf

|       |

|       |__ images/

|               |__ faq.md


## How to Use

- Clone the Repository with the CLI CMD: `git clone https://github.com/kboehmer1986-creator/python-learning-guide.git`.

### Access the Materials

- PDF: Open "pdf/python-learning-guide.pdf" for a ready-to-read version.
- Markdown: Edit or read the source in "markdown/python-learning-guide.md".
- Code Examples: Run Python scripts in the "code/" directory.
- Exercises: Try the exercises in "exercises/" and check solutions in "solutions/".
- Quizzes: Test your knowledge with "quizzes/".
- Interactive Modules: Open Jupyter Notebooks in "interactive/notebooks/" ( requires JupyterLab ).

### Run Code Examples

- Navigate to the code/ directory and run any Python file with the CLI CMD: `python code/basics/variables.py`.

### Interactive Jupyter Notebooks

- Install JupyterLab with the CLI CMD: `pip install jupyterlab`.
- Launch JupyterLab with the CLI CMD: `jupyter lab`.
- Open the notebooks in the "interactive/notebooks/"  directory.

## PDF Generation

### Option 1: LaTeX

- Install LaTeX ( [TeX Live](https://www.tug.org/texlive/ ) or [MiKTeX](https://miktex.org/) ).
- Compile the LaTeX file with the CLI CMD: `cd latex` and `pdflatex python-learning-guide.tex`.
- The PDF will be generated as "python-learning-guide.pdf".

### Option 2: Pandoc

- Install [Pandoc](https://pandoc.org/installing.html).
- Convert Markdown to PDF with the CLI CMD: `pandoc markdown/python-learning-guide.md -o pdf/python-learning-guide.pdf`.

## Contributing

Contributions are welcome! Here’s how you can help:

- Fork the repository.

- Create a new branch with the CLI CMD: `git checkout -b feature/your-feature`.

- Commit your changes with the CLI CMD: `git commit -m "Add your feature"`.

- Push to the branch with the CLI CMD: `git push origin feature/your-feature`.

- Open a Pull Request.

### Contribution Guidelines:

- Follow PEP 8 for Python code.

- Use clear and descriptive commit messages.

- Add comments to explain complex logic.

- Test your changes before submitting.

## License

This project is licensed under the Creative Commons Attribution CC0-1.0 license.

### You are free to:

- Share: Copy and redistribute the material in any medium or format.
- Adapt: Remix, transform and build upon the material for any purpose.

### Under the following terms:

- Attribution: You must give appropriate credit, provide a link to the license and indicate if changes were made.
- ShareAlike: If you remix, transform or build upon the material, you must distribute your contributions under the same license as the original.

See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by official Python documentation, books and free online resources.
- Thanks to the Python community for their support and contributions.