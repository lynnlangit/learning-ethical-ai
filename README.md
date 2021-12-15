# Learning Ethical AI
Resources to learn how to implement ethical AI using machine learning.  Mostly focuses on neural networks.  Includes books, papers, talks, videos and tools.

## Book / Papers 
Listed below - also see the academic papers in `/papers` folder of this repo.  

- 📖 Book: "Weapons of Math Destruction" by Cathy O'Neil - [link](https://www.penguinrandomhouse.com/books/241363/weapons-of-math-destruction-by-cathy-oneil/)
- 📖 Book: "The Alignment Problem: Machine Learning and Human Values" by Brian Christian- [link](https://brianchristian.org/the-alignment-problem/)
- 📖 Book: "Invisible Women" by Caroline Perez - [link](https://www.abramsbooks.com/product/invisible-women_9781419735219/)
- 📖 Book: "Hello World - How to be human in the age of the machine" by Hannah Fry - [link](https://hannahfry.co.uk/book/hello-world/)
- 📚 Papers: Collection of Timnit Gebrus published papers - [link](https://paperswithcode.com/search?q=author%3ATimnit+Gebru)

## Guidance / Best Practices
Most major cloud vendors provide guidance and best practices for implementing ethical AI.  I am most familiar with Google's guidance.

- ✨ Google's "People + AI Patterns" Guidebook - [link](https://pair.withgoogle.com/guidebook/patterns/how-do-i-get-started)
- ✨ Google's "Responsible AI Practices" - [link](https://ai.google/responsibilities/responsible-ai-practices/)
- ✨ AWS "Fairness and Explanability in AI" - [link](https://pages.awscloud.com/rs/112-TZM-766/images/Amazon.AI.Fairness.and.Explainability.Whitepaper.pdf)

## Talks / Videos
Authors of the books and papers listed above have also given talks on the focus of their writing.  I prefer to read the book first, then watch the talk.

- 🗣️ Talk: "Weapons of Math Destruction" by Cathy O'Neil in 2016 / 58 min.- [link](https://www.youtube.com/watch?v=TQHs8SA1qpk)
- 🗣️ Talk: "How I am fighting bias in AI" by Joy Buolamwini in 2017 / 9 min. - [link](https://www.youtube.com/watch?v=UG_X_7g63rY)
- 🗣️ Presentation: "Fairness and Explanability in Machine Learning" by AWS (shows SageMaker Clarify tool) in 2021/ 27 min. - [link](https://www.youtube.com/watch?v=EBQOaqhsnqM&t=3s)

## Tools for Data
Google has an extensive set of tools to evaluate bias in data used in models for AI.  Many tools focus on data that will be used in TensorFlow models.

- 🔍 Google's Responsible AI - tools and practices - [link](https://www.tensorflow.org/responsible_ai)
- 🔍 Data Card example - [link](https://research.google/static/documents/datasets/crowdsourced-high-quality-colombian-spanish-es-co-multi-speaker-speech-dataset.pdf)
- ✏️ Datasheet Template - [link](https://github.com/lynnlangit/learning-ethical-ai/blob/main/datasheet-template/Datasheets_Template.pdf)
- 🔍 Know Your Data tool example (celebrity faces) -[link](https://knowyourdata-tfds.withgoogle.com/#tab=STATS&dataset=celeb_a)
- 🔍 TensorFlow Data Validation tools (skew, drift, more...) - [link](https://www.tensorflow.org/tfx/guide/tfdv)
- 🔍 Pair Explorables, Measuring Diversity example -[link](https://pair.withgoogle.com/explorables/measuring-diversity/)
- 🔍 Pair Explorables, Hidden Bias example - [link](https://pair.withgoogle.com/explorables/hidden-bias/)

## Tools for Models
Google's model evaluation tools center around models built with TensorFlow.  Other vendors also support open source tools for model evaluation and more.

- 🔎 Using MinDiff to do model remediation for TensorFlow - [link](https://www.tensorflow.org/responsible_ai/model_remediation)
- 🔎 Model Card tool (provides context and transparency into a model's development and performance)- [link](https://www.tensorflow.org/responsible_ai/model_card_toolkit/guide)
- 🔎 Example Model Card for face detection - [link](https://modelcards.withgoogle.com/face-detection)
- :octocat: Open Source library 'InterpretML' to explain blackbox systems - [link](https://github.com/interpretml/interpret#supported-techniques)
- :octocat: Open Source 'responsible AI toolbox' (from Microsoft) - [link](https://github.com/microsoft/responsible-ai-toolbox)
- 🔎 Google's 'What If' tool for model understanding, faces examples - [link](https://pair-code.github.io/what-if-tool/demos/image.html) - example image shown below.

<img src="https://github.com/lynnlangit/learning-ethical-ai/blob/main/images/what-if-tool.png" width=800>
