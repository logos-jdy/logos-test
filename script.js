
const todoInput = document.getElementById('todo-input');
const addButton = document.getElementById('add-todo');
const todoList = document.getElementById('todo-list');

function addTodo() {
    const task = todoInput.value.trim();

    if (task === '') {
        alert('Please enter a task.');
        return;
    }

    const listItem = document.createElement('li');
    listItem.textContent = task;

    listItem.addEventListener('click', () => {
        listItem.classList.toggle('completed');
    });

    todoList.appendChild(listItem);
    todoInput.value = '';
    todoInput.focus();
}

addButton.addEventListener('click', addTodo);

todoInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        addTodo();
    }
});
