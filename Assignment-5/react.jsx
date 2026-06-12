import { useState } from "react";

export default function TodoApp() {
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState("");

  const addTodo = () => {
    const text = input.trim();
    if (!text) return;
    setTodos([{ id: Date.now(), text }, ...todos]);
    setInput("");
  };

  return (
    <div style={{ maxWidth: 400, margin: "40px auto", fontFamily: "sans-serif" }}>
      <h1>Todo List</h1>
      <div style={{ display: "flex", gap: 8, marginBottom: 16 }}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && addTodo()}
          placeholder="Add a task..."
          style={{ flex: 1, padding: "8px 12px", fontSize: 15 }}
        />
        <button onClick={addTodo} style={{ padding: "8px 16px" }}>Add</button>
      </div>
      <ul style={{ listStyle: "none", padding: 0 }}>
        {todos.map((todo) => (
          <li key={todo.id} style={{ padding: "8px 0", borderBottom: "1px solid #eee" }}>
            {todo.text}
          </li>
        ))}
      </ul>
    </div>
  );
}