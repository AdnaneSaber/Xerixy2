import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import "./App.css";
import Todo from "./Todo";
import { useState, useEffect } from "react";
import { v4 as uuidv4 } from "uuid";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
const axios = require("axios");
const App = () => {
  const [endDate, setEndDate] = useState(new Date());
  const [todos, setTodos] = useState([]);
  const [attributed_to, setAttributed_to] = useState("");
  const [priority, setPriority] = useState("");
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [newTodo, setNewTodo] = useState(uuidv4());
  const [search, setSearch] = useState("");
  const createTodo = (e) => {
    const body = {
      title: title,
      description: description,
      end_date: `${endDate.getFullYear()}-${parseInt(endDate.getMonth()) + 1}-${
        parseInt(endDate.getDate()) + 1
      }`,
      priority: parseInt(priority),
      attributed_to: parseInt(attributed_to),
    };
    axios
      .post(`${process.env.REACT_APP_API_URL}/todos/0/`, body)
      .then(() => {
        setNewTodo(uuidv4());
        setAttributed_to('0');
        setTitle("");
        setDescription("");
        setPriority("0");
        setEndDate(new Date());
      })
      .catch((e) => {
        console.error(e);
      });
    e.preventDefault();
  };
  useEffect(() => {
    axios
      .get(`${process.env.REACT_APP_API_URL}/todos/0/`)
      .then((res) => {
        setTodos(res.data);
      })
      .catch((e) => {
        console.error(e);
      });
  }, [newTodo]);
  let filtered = todos.filter((todowa) => {
    return todowa.title.toLowerCase().indexOf(search.toLowerCase()) !== -1;
  });
  return (
    <>
      <div className="container">
        <header className="text-center text-light my-4">
          <h1 className="mb-4">Xerixy Todo List</h1>
          <form className="search">
            <input
              className="form-control m-auto"
              type="text"
              name="search"
              placeholder="search todos"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
            />
          </form>
        </header>
        <ul className="list-group todos mx-auto text-light">
          {filtered.map((todo) => (
            <Todo
              key={todo.id}
              todo={todo}
              callback={setNewTodo}
              call={newTodo}
            />
          ))}
        </ul>

        <form className="add text-center my-4" onSubmit={(e) => createTodo(e)}>
          <label className="text-light">Add a new todo...</label>
          <div className="form-group row">
            <label className="text-light">To : </label>
            <select
              className="form-control"
              name="attributer_to"
              required
              value={attributed_to}
              onChange={(e) => setAttributed_to(e.target.value)}
            >
              <option value="0">Select someone...</option>
              <option value="1">Adnane</option>
              <option value="2">Salma</option>
            </select>
          </div>
          <div className="form-group row">
            <label className="text-light">Todo Title</label>
            <input
              className="form-control m-auto"
              type="text"
              name="title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
            />
          </div>
          <div className="form-group row">
            <label className="text-light">Todo Description</label>
            <input
              className="form-control m-auto"
              type="text"
              name="description"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
            />
          </div>
          <div className="form-group row">
            <label className="text-light">Priority</label>
            <select
              className="form-control"
              name="priority"
              required
              value={priority}
              onChange={(e) => setPriority(e.target.value)}
            >
              <option value="0">Select Priority...</option>
              <option value="1">😍</option>
              <option value="2">😍😍</option>
              <option value="3">😍😍😍</option>
            </select>
          </div>
          <div className="form-group row">
            <label className="text-light">Select ending date</label>
            <DatePicker
              name="end_date"
              selected={endDate}
              onChange={(date) => setEndDate(date)}
            />
          </div>

          <button className="btn btn-success submit">Submit</button>
        </form>
      </div>
    </>
  );
};
export default App;
