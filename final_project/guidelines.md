# PHY 225 Final Project Guidelines

## Overview

The final project is your opportunity to apply the computational skills you've developed this semester to a problem that interests you. You will develop a well-structured, documented software package addressing a scientific or engineering problem, and present your work in a professional computational report. This project accounts for 30% of your final grade.

## Learning Goals

Through this project, you will:

* Formulate physics and engineering problems in computational form by identifying appropriate approximations, boundary conditions, and initial conditions, then implement and validate numerical solutions
* Write well-structured, documented Python code using scientific computing libraries (e.g., NumPy, SciPy) and modern software development practices including version control with Git/GitHub
* Create effective visualizations of computational results, perform data analysis including fitting and statistical methods, and present findings through clearly labeled plots, tables, and written reports that communicate scientific insights
* Demonstrate professional coding practices that would allow others to use, modify, and build upon your work

## Selecting a Good Problem

A successful project balances ambition with feasibility. Here are strategies for identifying appropriate problems:

**Good starting points:**
* Extend or generalize a method from class (e.g., take a 1D solver and adapt it to 2D, or modify boundary conditions)
* Implement a classical algorithm that addresses a problem relevant to your field
* Optimize or modernize an existing implementation (e.g., vectorize slow code, improve documentation for a useful but poorly documented package). You can visit Github repositories of scientific packages and look for open issues tagged with "help wanted" to find opportunities for contribution.
* Apply numerical methods you've learned to a problem from your other coursework or research interests

**Common pitfalls to avoid:**
* **Don't pick something so complex you can't get started.** Choose a problem where you can write working code early, then add features incrementally.
* **Don't simply copy existing code.** Substantial original implementation is required. If you're building on existing work, you should be adding significant new functionality, improving performance, or substantially improving documentation and usability.
* **Be cautious with machine learning projects.** Unless you have prior ML experience, the statistical complexity (validation, hyperparameter tuning, appropriate model selection) can easily become overwhelming. Simpler methods are often more appropriate and demonstrate better understanding. If you are eager to pursue an ML project, I suggest working in a team. There are a few ML projects for my research that I can provide more guidance on, so please reach out if you're interested in working on an ML project but don't have any prior experience.
* **Consider scope carefully.** Better to do a focused problem thoroughly than tackle something sprawling and incomplete.

For inspiration and examples of appropriate project complexity, see `project_inspo.md`.

## Project Parameters

### Individual vs Team Projects

Projects are **individual by default**. If you wish to work with a partner, you must:
1. Discuss your proposed project with me first
2. Ensure the problem scope scales appropriately (a 2-person project should be noticeably more ambitious than an individual project)
3. Use version control practices that clearly document individual contributions

### Problem Requirements

Your project must:
* Address a problem relevant to science or engineering
* Demonstrate sufficient complexity to showcase what you have learned in this course
* Be implemented primarily in Python using appropriate scientific libraries
* Be hosted in a public GitHub repository with evidence of iterative development (i.e., has a commit history showing meaningful progress over time)

### Contributing to Existing Libraries

You may contribute a new feature to an established scientific package (e.g., NumPy, SciPy, Astropy) instead of creating a standalone package, **but you must**:
1. Discuss this option with me before your proposal
2. Verify with the package maintainers that your contribution would be welcome
3. Follow the project's contribution guidelines, coding standards, and testing requirements
4. Be willing to submit a genuine pull request if your code works by the end of the semester.

Note: Contributions to large, widely-used packages require substantial testing and documentation to be accepted, but successful contributions can have significant impact.

## Timeline and Deadlines

| Component | Deadline | Weight |
|-----------|----------|--------|
| Project Proposal | March 23 | 10% |
| Project Update | April 17 | 10% |
| Peer Review | May 7 (in class) | 10% |
| Final Report | Date of final exam (TBA) | 30% |
| Code & Documentation | Date of final exam (TBA) | 40% |

**Total Project Weight: 30% of course grade**

## Grading Rubric

### Project Proposal (10%, Due March 23)

**Length:** 1-2 pages

**Required components:**
* **Problem statement:** What problem are you solving? Why is it interesting or important?
* **Proposed methods:** What numerical methods, algorithms, or computational approaches will you use?
* **Expected challenges:** What technical difficulties do you anticipate?
* **Timeline:** Week-by-week plan from now until the final deadline

Your proposal will be evaluated on clarity, feasibility, and appropriate scope.

---

### Project Update (10%, Due April 17)

**Required components:**
* **Link to public GitHub repository** with your work-in-progress
* **Written statement (max 1 page)** addressing:
  - Where you are relative to your proposed timeline
  - Any changes to your approach or methods
  - Any challenges you've encountered and how you addressed them
  - Problems you're currently stuck on
  - **If behind schedule:** Specific strategies for catching up (reducing scope, allocating more time, seeking help)
  - **If ahead of schedule:** Proposed extensions or additional features to pursue
* **Rough draft of Methods section** of your final report. This can be a rough/incomplete draft and will evolve as you implement your code, but it should include a detailed description of your approach (including any equations!) and the algorithms/numerical methods you will implement.
    - Note that your final report can be in the form of a LaTex paper or a Jupyter notebook with detailed markup. 

This checkpoint ensures you're making progress and identifies where you might need support.

---

### Peer Review (10%, In-Class Activity May 7)

You will review the code and projects of two classmates during class time on May 7. If you cannot attend, you may complete peer reviews outside of class with prior permission.

**What you'll review:**
* Code quality (structure, readability, style)
* Scientific/engineering merit (appropriate methods, correct implementation)
* Usability (can you install and run their code?)
* Documentation (is it clear how to use the software? do you understand what the software is doing?)

**Your grade** (the 10%) reflects the **quality of the reviews you provide** to your peers, not the reviews you receive. You will be provided a rubric to guide your reviews.

**Your code grade** (part of the 40% code component) will incorporate feedback from the peer reviews you receive.

---

### Code and Documentation (40%, Due Date of Final Exam)

Your code must be submitted as a public GitHub repository with evidence of iterative development (meaningful commit history).

#### Breakdown:

**Project Scope (10%)**
* Problem is sufficiently complex and challenging
* Makes a genuine attempt to solve the problem, even if not completely successful
* Demonstrates creativity in application or implementation
* Shows thoroughness in approach

**Code Quality (15%)**
* Logical structure with minimal redundancy
* Appropriate use of functions, classes, and abstractions
* Clear, readable code following Python style conventions
* Includes tests (unit tests or other validation) demonstrating correctness
* Code runs without errors on standard inputs

**Documentation (15%)**
* **README.md** includes:
  - Clear description of what the software does
  - Installation instructions
  - Usage examples with expected outputs
  - (Optional) Results, benchmarks, or validation in a dedicated section
* Major functions and classes include docstrings
* Code comments explain non-obvious logic
* Repository structure is clear and organized
* Repository contains a LICENSE file specifying the terms under which others can use your code (e.g., MIT License, GPL, etc.). Note that if you have used code from other sources, you should choose a license that is compatible with the licenses of the code you have incorporated. For example, if you have included code that is licensed under the GPL, your project must also be licensed under the GPL.

---

### Project Report (30%, Due Date of Final Exam)

You have flexibility in how you present your work. Choose the format that best suits your project:

**Option 1: LaTeX Report**
* Traditional scientific paper format
* Separate code and narrative

**Option 2: Computational Essay (Jupyter Notebook)**
* Interweaves narrative, code, and results
* Executable document demonstrating your work

Both formats are equally valued. Choose based on your project needs and personal preference.

#### Required Sections:

**Introduction/Background**
* Motivation: Why is this problem important?
* Context: What prior work exists? What gap are you filling?
* Goals: What does your software accomplish?

**Methods**
(Advice: This should be the first section you start writing, and you can start drafting it early in the project. It will evolve as you implement your code, but having a detailed methods section will help you clarify your approach and identify any gaps in your understanding.)
* What algorithms or numerical methods did you implement?
* What are the key implementation details?
* Include relevant equations, pseudocode, or code snippets as appropriate
* Remember that a good scientific report will have a methods section that is detailed enough for another competent programmer to understand your approach and potentially reproduce your work.

**Results**
* What did your code produce?
* Include figures, tables, and visualizations with clear captions and labels
* Demonstrate validation (comparison to analytical solutions, benchmarks, or expected behavior; i.e., how do you know your code is working correctly?)

**Discussion**
* Interpret your results in their scientific/engineering context
* What are the strengths and limitations of your implementation?
* What are the pros and cons of the methods you chose?
* What challenges did you encounter and how did you address them?

**Conclusion**
* Briefly summarize what you accomplished
* Future outlook: What are the next steps for this software? What features or extensions would be valuable?

**Disclosure of LLM Usage** (brief unnumbered section)
* Describe if/how you used LLMs (e.g., ChatGPT, Copilot, Claude) during software development and report writing
* If you used an LLM, name the specific model(s) you used
* If you used an LLM, be specific about what tasks you used it for
* If you used an LLM, include a version of the following statement (which should be true): "After using these tools, I have reviewed and edited the content of this report and the code in my repository to ensure it reflects my own understanding and work."

**Optional:**
* Appendices for supplementary material which describe additional technical details not essential to main narrative

#### Grading Breakdown (30% total):

* **Introduction/Background (5%):** Clear motivation, appropriate context, well-defined goals
* **Methods (7%):** Thorough explanation of approach, appropriate technical detail
* **Results (8%):** Clear presentation of outcomes, effective visualizations, evidence of validation
* **Discussion (7%):** Thoughtful interpretation, honest assessment of limitations, demonstrates understanding
* **Conclusion (3%):** Concise summary and reasonable future directions

**Note on length:** There is no strict page requirement. Length will vary based on your project, the number of figures, and whether you include code in the report. Look at example projects for guidance on appropriate scope. You can share drafts with your instructor for feedback on length and content.

## Academic Integrity and Proper Attribution

Following the course academic integrity policy:

* You may use open-source code and build on existing work, **but you must cite your sources**
* You may use LLMs to assist with code generation and debugging, **but you must disclose this usage**
* You may use LLMs to assist with editing your report, **but you must disclose this usage with specific details about the LLMs used and their role in your work**. You must spend significant time on your report and code, which can be demonstrated with version control. While writing can be challenging, it is the act of writing that helps you calrify your thinking and demonstrate your understanding. If you use an LLM to assist with writing, you should review and edit the content to ensure it reflects your own voice and understanding, and you should not rely on LLMs to write large sections of your report for you.
* Your project must demonstrate substantial original work—simply copying or lightly modifying existing implementations is not acceptable
* Code that is not your own must be clearly attributed in comments and/or documentation

When in doubt, cite your sources. Proper attribution is a professional practice. Many Github repositories will have a CITATION file that specifies how to cite the software. If you use code from a repository, follow their citation guidelines and include a reference in your documentation. 

## Getting Help

If you encounter challenges:
* Attend office hours to discuss technical problems
* Use your project update to flag issues early
* Consult the course materials and recommended resources
* Discuss approaches with classmates (but write your own code)
* Use LLMs thoughtfully as coding assistants (with proper disclosure)

Remember: It's acceptable to attempt a challenging problem and not fully solve it. The goal is to write good code with good documentation and demonstrate solid computational thinking.

---

## Citations and Acknowledgments

This document draws inspiration from:
* Project guidelines from UT Austin PHY 329 (Computational Physics), William Gilpin, available at https://github.com/Prof-McDonough/cphy/blob/main/vignettes/project.md 
* Project report structure from "Computational Physics" course materials by Prof. Morten Hjorth-Jensen, available at https://github.com/Prof-McDonough/ComputationalPhysics/tree/master

**Document Development:** This project guidelines document was drafted with substantial assistance from Claude (Anthropic), an AI assistant, based on detailed specifications provided by Prof. Bryanne McDonough. The AI assistant was provided with the structure, learning goals, specifications, and examples. Rubrics and specific guidance was developed through iterative discussion between the instructor and the AI assistant. The final document was reviewed and edited by the instructor to ensure it reflects the course goals and expectations.

