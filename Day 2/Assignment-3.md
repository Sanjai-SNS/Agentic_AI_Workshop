##Financial Report Analysis**

Financial professionals, investors, and decision-makers often struggle to quickly extract relevant insights from lengthy and complex financial documents such as annual reports, balance sheets, and earnings reports. These documents are filled with jargon, dense numerical data, and intricate details, making it challenging to identify key takeaways efficiently.

Traditional methods of analyzing financial documents, such as manual review or static summaries, are time-consuming and prone to oversight. While some AI tools exist, they cannot often provide context-aware, actionable insights specific to the user’s goals, making them less effective for quick and informed decision-making.

##Objective**

The aim of this project is to build an AI-powered system that:
- Scans and extracts data from financial document images.
- Identifies and highlights key financial metrics, trends, and risks.
- Summarizes the content into easy-to-understand insights tailored to user roles.
- Analyzes charts and graphs embedded within the documents.

##Core Features**
1. Input: Images of financial reports (uploaded or URL-based).
2. OCR: Use of Tesseract to extract text from images.
3. NLP: Use of transformer models to summarize financial content.
4. Output: Clean and structured summary with metrics, insights, and strategic highlights.

##Sample Output Elements**
- **Key Metrics:** Net income, revenue, EPS, cost/income ratio, ROE, CET1.
- **Income & Expenses:** Interest income, operating expenses.
- **Balance Sheet:** Total assets, liabilities, deposits.
- **Credit Quality:** Forbearance ratio, cost of risk, NPL ratio.
- **Strategic Notes:** Sustainability, digital transformation, market outlook.

##Technologies Used**
- Python
- PIL, OpenCV (for image handling)
- pytesseract (for OCR)
- HuggingFace Transformers (for summarization)

##Usage Instructions**
1. Place financial document images into the `sample_inputs/` folder.
2. Run the pipeline via `main.py`.
3. Review the output summary in `sample_outputs/`.

**Conclusion**
This AI-powered system significantly reduces the time and effort required to interpret complex financial documents, providing fast, user-specific, and actionable summaries.

