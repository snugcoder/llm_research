# Persona-Based Bias Detection in LLM Outputs
 
> Analyzing how personalization and user personas shape bias in large language model (LLM) responses.
 
Research project conducted at **Privacy and Security Lab (Professor Umar Iqbal)**, **Washington University in St. Louis**, **[May 2025– December 2025]**. Findings were presented at the **WashU Research Symposium** to 50+ student researchers and faculty, within the WUSEF Program.
My contributions to this project are in this repository, the full repository can be found here: [`https://github.com/sta97/The-Sims-LLM-Persona-Creation`]

## Overview
 
LLMs increasingly tailor their responses to a user's inferred or stated profile (age, gender, occupation, interests, and so on). This personalization can improve helpfulness, but it also raises ethical questions: does the model treat different personas differently, and do those differences reflect harmful stereotypes?
 
This repository contains the full body of work for investigating that question:
 
1. **Persona extraction.** Building realistic user personas from web-scraped Reddit comments.
2. **Prompt generation.** Producing thousands of persona-conditioned chat prompts and collecting LLM outputs.
3. **Bias detection.** Using LangChain-based scripts to identify bias patterns in the generated content.
4. **Pipeline validation.** Benchmarking the detection pipeline with Selenium to measure and improve its accuracy.

## Methodology

 At the time I worked on this project, here is the proposed methodology: 
```
Reddit comments ──► Persona extraction ──► Persona-conditioned prompts
                                                      │
                                                      ▼
                          Bias analysis  ◄──  LLM-generated outputs
                                │
                                ▼
                  Selenium benchmarking & accuracy evaluation
                                │
                                ▼
                    Findings + proposed research pathways
```


## Presentation
 
Presented at the **WashU Research Symposium** to an audience of 50+ student researchers and lecturers.
 
- Poster / slides: [`docs/symposium_poster.pdf`](docs/symposium_poster.pdf)
## Tech Stack
 
- **Language:** Python
- **LLM orchestration:** LangChain
- **Automation and testing:** Selenium
- **Data collection:** Web scraping (Reddit)
- **Analysis:** Pandas, Jupyter Notebooks
## Limitations and Ethical Considerations
 
- Personas derived from Reddit reflect that platform's user base and are not representative of the general population.
- Raw scraped data is excluded from this repository to respect user privacy and platform terms of service. All personas are anonymized.

- ## Acknowledgments
 
Thank you to `Stuart Aldrich`, `Professor Umar Iqbal` and the `Privacy and Security Lab` at Washington University in St. Louis for their guidance and support.
 

