# Text Redundancy Analyzer

This project was built using python3.8.


## Problem description

Sometimes the output of an LLM can have redundant information, this information does not add anything relevant to the result it is just more text and the idea is repeated.

How can we prevent this?



## TODO:

- [x] Analyze the problem and understand input/output
- [] Search for possible solutions (I read time ago about text processing in hugging face, would this work for our case?)
- [] The solution should support German/French/English
- [] Compare quickly the solutions
- [] Build an example with it
- [] Review the solution (test)

### Understanding the problem

Input: Text (with some repetitive ideas on it)

Output: What should be the output? The unique text or what?

Goal: `The goal of this project is to make a plan on how to identify redundancies in the notes and how to tackle the problem.`

So we need a simple implementation and a plan.

Based on the input, we can assume that the Output has been generated already (by an LLM or something else), so we can add a new step into the pipeline, and process the text again.

How big is the information?
From the example text provided, the text has a length ~600 words.

We should support multi languages too.

Following this idea, we can implement something that can be integrated as part of the existing processing pipeline.



### Possible solutions

There are some possible solutions:
1. Generate again the output by asking again to LLM.
2. Create a tool to detect these redundancies and remove them.

#### First

We can ask again to the LLM with a specific prompt, something like:

```python
prompt = """
Analyze this medical note for redundancies:
{note}
"""
```
This might work, but maybe processing again is expensive? and we might just ended up again with the same problem?

#### Second

Create another tool with python to analyze the output and remove the redundancies?
This might be cheaper than sending again the request to the LLM.


Maybe both solutions together are the answer? 
How do we evaluate the solutions?

## Implementation