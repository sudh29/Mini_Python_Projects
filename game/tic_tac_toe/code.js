const cells = document.querySelectorAll(".cell");
const status = document.getElementById("status");
const resetButton = document.getElementById("reset-button");

let currentPlayer = "X";
let gameOver = false;

function checkWinner() {
    const winCombos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
        [0, 4, 8], [2, 4, 6]             // Diagonals
    ];

    for (const combo of winCombos) {
        const [a, b, c] = combo;
        if (cells[a].textContent && cells[a].textContent === cells[b].textContent && cells[a].textContent === cells[c].textContent) {
            cells[a].classList.add("win");
            cells[b].classList.add("win");
            cells[c].classList.add("win");
            status.textContent = `Player ${currentPlayer} wins!`;
            gameOver = true;
            setTimeout(() => {
                alert(`Player ${currentPlayer} wins!`);
            }, 100);
        }
    }
}

function checkTie() {
    if ([...cells].every(cell => cell.textContent !== "")) {
        status.textContent = "It's a tie!";
        gameOver = true;
        setTimeout(() => {
            alert("It's a tie!");
        }, 100);
    }
}

function handleClick(event) {
    const cell = event.target;
    if (!cell.classList.contains("cell") || cell.textContent !== "" || gameOver) {
        return;
    }
    cell.textContent = currentPlayer;
    checkWinner();
    checkTie();
    currentPlayer = currentPlayer === "X" ? "O" : "X";
    status.textContent = `Player ${currentPlayer}'s turn`;
}

function resetGame() {
    cells.forEach(cell => {
        cell.textContent = "";
        cell.classList.remove("win");
    });
    currentPlayer = "X";
    gameOver = false;
    status.textContent = "Player X's turn";
}

cells.forEach(cell => cell.addEventListener("click", handleClick));
resetButton.addEventListener("click", resetGame);

resetGame(); // Initialize the game
