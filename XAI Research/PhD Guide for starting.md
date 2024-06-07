Tools for Help:
- https://researchrabbitapp.com/ ([jayasooryantm2@gmail.com](mailto:jayasooryantm2@gmail.com))
- [https://elicit.org/](https://elicit.org/) ([jayasooryantm2@gmail.com](mailto:jayasooryantm2@gmail.com))

### Tools for Organising and learning:
- **GitHub**: Code versioning
- **GitHub Projects** - Task Management
- https://www.subnetwrk.xyz for Blogging
	- add more features (add LLM expert Bot, in-built text editor)
- **LinkedIn + Twitter** - for networking
	- Once first phase is done (where I understand the path and what to do) start posting
- **Zotero** - for paper management
- **Overleaf** - for paper writing
- **Haystack ([https://haystack.deepset.ai/](https://haystack.deepset.ai/)):** Flexible framework for building question-answering systems on your own data (including research papers). Requires more setup than the ready-to-use options above.
- **Obsidian** - the Star, dump down notes. manage everything, my second brain


**Starting Point: Knowledge Foundations**

- **Week 1: Attention Mechanisms Review**
    - Papers: Look up the original work on attention in neural networks ("Attention is All You Need," etc.)
    - Implementations: Find tutorials on using attention visualisations in Hugging Face or similar.
- **Week 2: Limitations of Attention for XAI**
    - Find critical papers pointing out cases where attention-based explanations fall short. Look for terms like "faithfulness," "reliability," and "causal reasoning" in XAI papers.

**Month 1-2: Literature Deep Dive + Technique Experimentation**

- **Week 3-6: XAI Techniques Beyond Attention**
    - Focus on recent conferences (NeurIPS, ICML, ACL).
    - Search terms: "causal explanations," "concept-based XAI," "counterfactual explanations," "hybrid XAI".
    - Start a well-organised literature list.
- **Week 7-8: Implement & Experiment**
    - Pick 2-3 promising XAI techniques that seem to address attention limitations.
    - Implement them in a simplified setting on a smaller LLM.

**Month 3-4: Developing Your Novel Approach**

- **Week 9-12: Assess and Synthesise**
    - What are the strengths and weaknesses of the techniques you implemented?
    - Draw insights: Can they be combined? What foundational element is missing?
    - Begin formulating your own novel method.
- **Week 13-16: Basic Implementation & Testing**
    - Code up the core of your new XAI method.
    - Design test cases to compare its outputs with both attention and other XAI baselines.

**Month 5-6: Evaluation & Refinement**

- **Week 17-20: Evaluating Faithfulness**
    - Develop a way to measure if your explanations are more accurately reflecting LLM reasoning (this is a challenging area in itself!).
    - Might involve user studies or synthetic tests.
- **Week 21-23: Actionability Focus**
    - Design examples showing how your explanations can be used to intervene with an LLM (guiding it, spotting potential problems).
- **Week 24: Project Write-up**
    - Even without publication, start writing a concise project summary describing your problem focus, novel method, and how it improves on XAI state-of-the-art

**Important Notes:**

- **Collaborate:** Look for online communities interested in LLM XAI. Getting feedback early is essential
- **Datasets:** As you formulate your method, refine how you'll find or create the perfect data to demonstrate its strengths.
- **Flexibility is Key:** Research is iterative; your roadmap will likely change as you progress.