import React, { useState, useEffect } from "react";
import { v4 as uuidv4 } from 'uuid';
const axios = require("axios");
const Todo = (props) => {
  
  const [changed, setChanged] = useState(false);
  const [body, setBody] = useState("");
  const [done, setDone] = useState(body.done);
  const [reload, setReload] = useState(!props.newTodo);
  let newDate = new Date();
  let finish = new Date(body.end_date);
  let one_day = 1000 * 60 * 60 * 24;
  let diff = Math.round((finish - newDate) / one_day);
  const staff = {
    1: "Adnane",
    2: "Salma",
  };
  useEffect(() => {
    setBody(props.todo)
    setDone(props.todo.done)
  }, [props.todo]);
  const reloadParent = () => {
    props.callback(uuidv4());
    setReload(uuidv4());
  };
  useEffect(() => {
    if(body.id){
      axios
      .get(`${process.env.REACT_APP_API_URL}/todos/${body.id}/`)
      .then((res) => {
        setBody(res.data[0]);
        reloadParent();
      })
      .catch((e) => {
        console.error(e);
      });
    }
  }, [changed]);

  const deleteTodo = (id) => {
    axios
      .delete(`${process.env.REACT_APP_API_URL}/todos/${id}/`)
      .then(() => {
        reloadParent();
      })
      .catch((e) => {
        console.error(e);
      });
  };
  const doTodo = (e) => {
    axios
      .patch(`${process.env.REACT_APP_API_URL}/todos/${body.id}/`, {
        done: !done,
      })
      .then(() => {
        setChanged(!changed);
      })
      .catch((e) => {
        console.error(e);
      });
  };
  return (
    <>
      <li className="list-group-item d-flex justify-content-between align-items-center">
        <span className={body.done ? "done" : ""}>{body.title}</span>
        <span className={body.done ? "done" : ""}>{body.description}</span>
        <span className={body.done ? "done" : ""}>
          {body.priority
            ? [...Array(parseInt(body.priority))].map(() => "😍")
            : body.priority}
        </span>
        <span className={body.done ? "done" : "" || diff <= 1 ? "almostDone" : ""}>
          {diff} left days
        </span>
        <input
          type="checkbox"
          className="form-check-input"
          id="exampleCheck1"
          checked={done}
          value={done}
          onChange={(e) => doTodo(e)}
        />
        <button
          className="btn btn-danger"
          id={body.id}
          onClick={() => deleteTodo(body.id)}
        >
          {staff[body.attributed_to]}
        </button>
      </li>
    </>
  );
};
export default Todo;
