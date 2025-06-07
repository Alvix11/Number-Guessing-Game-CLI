# Number Guessing Game CLI

This is a simple console game where the user must guess a secret number randomly generated between 1 and 100. The game offers three difficulty levels and provides feedback on whether the entered number is higher or lower than the secret number.

Inspired by the project proposed by [roadmap.sh](https://roadmap.sh/projects/number-guessing-game).

## Features

- Three difficulty levels: Easy, Medium, and Hard.
- Limited attempts based on the selected difficulty.
- Clear and user-friendly messages.
- Option to play again after finishing a round.
- Measures the time taken for each successful attempt.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tu-usuario/Number-Guessing-Game-CLI.git
   cd Number-Guessing-Game-CLI
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

## Usage

Run the game with:

```bash
python number_guessing_game.py
```

Follow the on-screen instructions to select the difficulty and start playing.

## Project Structure

```
number_guessing_game.py   # Main entry point
game.py                  # Main game logic
utils.py                 # Helper and validation functions
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Author

Developed by [Alvix.exe](https://github.com/Alvix11).

---

Have fun playing and feel free to contribute!