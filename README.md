# 🛠️ TGML Auto-Binding Tool

This project automates the process of binding tag names in TGML (Tridium Graphics Markup Language) files using data from an Excel sheet. It significantly reduces the manual effort and time required to bind tags for DDC (Direct Digital Control) panels.

---

## 🚀 Purpose

In traditional workflows, binding tags in TGML files is a manual and time-consuming task, often taking **up to a full day per DDC panel**. This tool automates the process, completing it in **seconds**, thereby saving valuable engineering time and reducing human error.

---

## 📂 Project Structure

```
├── app.py                  # Main Flask application
├── templates/
│   └── index.html          # HTML form for file upload
├── uploads/                # Temporary storage for uploaded files
├── processed/              # Output folder for processed TGML files
└── README.md               # Project documentation
```

---

## ⚙️ How It Works

1. **Upload Files**: User uploads a `.tgml` file and an Excel sheet containing tag names and their corresponding bind names.
2. **Excel Parsing**: The tool reads the Excel sheet and maps labels (First, Second, Third) to their respective nomenclature.
3. **TGML Parsing**: It parses the TGML XML structure and updates the `<Bind>` elements where the `<Text>` tag matches the label.
4. **Download Output**: The updated TGML file is returned for download.

---

## 🧾 Excel Format

The Excel sheet should contain the following columns:

- `Nomenclature` (Bind name)
- `First Label`
- `Second Label`
- `Third Label`

Each label is matched against the `<Text Name="...">` in the TGML file.

---

## 🖥️ How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/tgml-auto-binding.git
   cd tgml-auto-binding
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app**:
   ```bash
   python app.py
   ```

4. **Open in browser**:
   Navigate to `http://127.0.0.1:5000` and upload your files.

---

## ✅ Benefits

- ⏱️ **Time-saving**: Reduces binding time from hours to seconds.
- 🧠 **Error reduction**: Eliminates manual errors in tag binding.
- 🔁 **Reusable**: Can be used for multiple DDC panels with minimal changes.
- 🧩 **Simple UI**: Easy-to-use web interface for uploading and downloading files.

---

## 📌 Future Enhancements

- Add support for multiple sheets or dynamic sheet detection.
- Include logging and error reporting.
- Deploy as a web service for team-wide access.

---
