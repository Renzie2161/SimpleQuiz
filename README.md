----

# Simple Quiz Program

This Python program allows users to answer a quiz based on a set of questions stored in a JSON file. Users can customize the quiz by adding their own questions and answers to the `questions.json` file.

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

Suppose you want to add a question about Chinese letters:

```json
{
    "What is the Chinese word for 'sun'?": "日",
    "Translate 我的妈妈说你做什么？": "My mother said what are you doing?",
}
```

## Contributing

Feel free to contribute to this project by adding more questions or improving the code. Fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
