---

# Simple Quiz Program

This Python program allows users to answer a quiz based on a set of questions stored in a JSON file. Users can customize the quiz by adding their own questions and answers to the `questions.json` file.

> [!IMPORTANT]
> This program is no longer actively maintained or supported. Feel free to use it as-is, but there may be bugs or issues that have not been addressed. Consider using alternative solutions for similar functionality.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/Renzie2161/SimpleQuiz.git
   cd SimpleQuiz
   ```

2. Customize the quiz questions:
   - Open the `questions.json` file.
   - Modify the file by adding new questions in the format `"Question": "Answer"`.
   - Save the file.

3. Run the program:
   ```bash
   python main.py
   ```

4. Answer the quiz questions that appear in the terminal. Answers must match exactly, including spaces, symbols, commas, and periods.

## Example

Suppose you want to add a question about Japanese letters:

```json
{
    "What is the Japanese word for 'sun'?": "日",
    "Translate 初めまして to English!": "Nice to meet you",
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
