# 🚀 Task Decomposition Agent

> *From idea → to execution, one atomic step at a time.*

An AI-powered multi-agent system that converts complex user goals into **atomic, dependency-aware, and execution-ready steps** using **Google ADK** and **Gemini**.

---

## 🧠 Problem

Many users struggle to transform high-level ideas into actionable steps.
Traditional tools:

* Provide vague guidance
* Lack proper sequencing
* Do not handle dependencies

This leads to confusion, delays, and inefficient execution.

---

## 💡 Solution

The **Task Decomposition Agent** solves this by:

* Breaking goals into **smallest possible actionable units (atomic tasks)**
* Maintaining **logical order and dependencies**
* Producing **clear, structured, and executable plans**

---

## ⚙️ How It Works

### 🔄 Workflow

1. User inputs a goal
2. Goal is stored in system state
3. **Task Analyzer** extracts components & dependencies
4. **Task Atomizer** generates atomic micro-steps
5. **Formatter** structures output into clean steps
6. Final plan is returned to the user

---

## 🏗 Architecture

* **Frontend/UI** → User input
* **Root Agent** → Entry point
* **ToolContext** → State management
* **Sequential Agents:**

  * Task Analyzer
  * Task Atomizer
  * Formatter
* **Gemini Model** → Reasoning engine
* **Cloud Run** → Scalable deployment

---

## ✨ Features

* ✅ Atomic task generation
* ✅ Dependency-aware sequencing
* ✅ Clean, structured output
* ✅ Modular multi-agent design
* ✅ Scalable and production-ready

---

## 🚀 Tech Stack

* **Google ADK (Agent Development Kit)**
* **Gemini 2.5 Flash**
* **Python**
* **Cloud Run**
* **dotenv (.env configuration)**

---

## 📦 Project Structure

```
task-decomposition-agent/
│── agents/
│── tools/
│── workflow/
│── main.py
│── .env
│── README.md
```

---

## 🧪 Example

### Input:

```
Build a personal portfolio website and deploy it online
```

### Output:

```
1. Define website purpose
2. Create project folder
3. Create index.html
4. Add HTML structure
5. Create CSS file
6. Style layout
7. Add JavaScript
8. Test locally
9. Push to GitHub
10. Deploy online
```

---

## ☁️ Deployment

### 1. Set Environment Variables

```
PROJECT_ID=your-project-id
MODEL=gemini-2.5-flash
```

### 2. Deploy using ADK

```
uvx --from google-adk==1.14.0 adk deploy cloud_run \
--project=$PROJECT_ID \
--region=europe-west1 \
--service_name=task-decomposition-agent \
--with_ui \
.
```

---

## 🎯 Use Cases

* 📚 Students → Study planning
* 💻 Developers → Project breakdown
* 🎉 Event organizers → Execution planning
* 🚀 Startups → Product roadmap

---

## 🌍 Impact

* Reduces cognitive load
* Improves productivity
* Enables faster execution
* Works across multiple domains

---

## 🔮 Future Enhancements

* ⏱ Time estimation agent
* 📊 Resource planning agent
* ⚠ Risk analysis agent
* 📱 UI dashboard integration

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork, improve, and submit a PR.

---

## 🙌 Acknowledgements

* Google ADK
* Gemini AI
* Hackathon organizers

---
